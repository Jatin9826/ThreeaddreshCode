# app.py

from flask import Flask, render_template, request
from lexer import tokenize
from parser import to_postfix, build_ast, save_ast_image
from code_generator import generate_tac, assign_tac, reset_tac, tac, new_label
from representation import generate_quadruples

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    expression = ""
    tokens = []
    tac_code = []
    quads = []
    ast_img_path = None

    if request.method == "POST":
        expression = request.form.get("expression", "").strip()
        if expression:
            reset_tac()
            tokens = tokenize(expression)

            try:
                if tokens[0] == "if":
                    # if (a < b) then x = x + 1 else x = x - 1
                    has_else = "else" in tokens
                    cond_start = 1
                    then_start = tokens.index("then") + 1
                    else_start = tokens.index("else") + 1 if has_else else len(tokens)

                    condition = tokens[cond_start:tokens.index("then")]
                    then_part = tokens[then_start:(tokens.index("else") if has_else else len(tokens))]
                    else_part = tokens[else_start:] if has_else else []

                    cond_postfix = to_postfix(condition)
                    cond_ast = build_ast(cond_postfix)
                    cond_result = generate_tac(cond_ast)

                    l1 = new_label()
                    l2 = new_label()
                    l3 = new_label() if has_else else None

                    tac.append(f"if {cond_result} goto {l1}")
                    tac.append(f"goto {l2}")
                    tac.append(f"{l1}:")

                    # then body
                    assign_index = then_part.index("=")
                    lhs = then_part[0]
                    rhs = then_part[assign_index + 1:]
                    rhs_postfix = to_postfix(rhs)
                    rhs_ast = build_ast(rhs_postfix)
                    result = generate_tac(rhs_ast)
                    assign_tac(lhs, result)

                    if has_else:
                        tac.append(f"goto {l3}")
                    tac.append(f"{l2}:")

                    if has_else:
                        assign_index = else_part.index("=")
                        lhs = else_part[0]
                        rhs = else_part[assign_index + 1:]
                        rhs_postfix = to_postfix(rhs)
                        rhs_ast = build_ast(rhs_postfix)
                        result = generate_tac(rhs_ast)
                        assign_tac(lhs, result)
                        tac.append(f"{l3}:")

                    ast_img_path = f"static/ast_{lhs}.png"
                    save_ast_image(rhs_ast, ast_img_path[:-4])

                elif "=" in tokens:
                    # Normal assignment
                    assign_index = tokens.index("=")
                    lhs = tokens[0]
                    rhs = tokens[assign_index + 1:]
                    postfix = to_postfix(rhs)
                    ast = build_ast(postfix)
                    result = generate_tac(ast)
                    assign_tac(lhs, result)
                    ast_img_path = f"static/ast_{lhs}.png"
                    save_ast_image(ast, ast_img_path[:-4])

                else:
                    tac.append("Unsupported structure")

                tac_code = tac.copy()
                quads = generate_quadruples(tac_code)

            except Exception as e:
                tac_code = [f"Error: {e}"]

    return render_template(
        "index.html",
        expression=expression,
        tokens=tokens,
        tac=tac_code,
        quads=quads,
        ast_img=ast_img_path,
    )

if __name__ == "__main__":
    app.run(debug=True)
