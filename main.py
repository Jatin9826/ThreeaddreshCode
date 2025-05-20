from lexer import tokenize
from parser import to_postfix, build_ast, save_ast_image
from code_generator import generate_tac, assign_tac, reset_tac, tac
from utils import display_tac
from representation import generate_quadruples, print_quadruples

def process_expression(expression):
    reset_tac()
    tokens = tokenize(expression)

    if tokens[0] == 'if':
        condition = tokens[1:tokens.index('then')]
        assignment = tokens[tokens.index('then') + 1:]

        condition_str = ' '.join(condition).replace('(', '').replace(')', '')
        cond_postfix = to_postfix(condition_str.split())
        cond_ast = build_ast(cond_postfix)
        cond_result = generate_tac(cond_ast)

        tac.append(f"if {cond_result} goto L1")
        tac.append(f"goto L2")
        tac.append("L1:")

        assign_index = assignment.index('=')
        lhs = assignment[0]
        rhs = assignment[assign_index + 1:]
        rhs_postfix = to_postfix(rhs)
        rhs_ast = build_ast(rhs_postfix)
        result = generate_tac(rhs_ast)
        assign_tac(lhs, result)

        tac.append("L2:")
        display_tac(tac)
        quads = generate_quadruples(tac)
        print_quadruples(quads)
        save_ast_image(rhs_ast, f'ast_{lhs}')

    elif '=' in tokens:
        assign_index = tokens.index('=')
        lhs = tokens[0]
        rhs_tokens = tokens[assign_index + 1:]
        postfix = to_postfix(rhs_tokens)
        ast = build_ast(postfix)
        result = generate_tac(ast)
        tac_code = assign_tac(lhs, result)
        display_tac(tac_code)
        quads = generate_quadruples(tac_code)
        print_quadruples(quads)
        save_ast_image(ast, f'ast_{lhs}')
    else:
        print("Invalid expression: No assignment found")

def main():
    print("Enter expressions line by line. Type 'END' to finish:")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == 'END':
            break
        lines.append(line.strip())

    for expr in lines:
        print(f"\nProcessing: {expr}")
        process_expression(expr)

if __name__ == "__main__":
    main()