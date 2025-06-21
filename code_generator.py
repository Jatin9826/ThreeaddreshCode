# code_generator.py

temp_count = 0
label_count = 0
tac = []

def new_temp():
    global temp_count
    temp_count += 1
    return f"t{temp_count}"

def new_label():
    global label_count
    label_count += 1
    return f"L{label_count}"

def reset_tac():
    global tac, temp_count, label_count
    tac = []
    temp_count = 0
    label_count = 0

def generate_tac(node):
    if node is None:
        return ""
    
    if not node.left and not node.right:
        return node.value

    if node.left and not node.right:
        operand = generate_tac(node.left)
        temp = new_temp()
        tac.append(f"{temp} = {node.value}{operand}")
        return temp

    left = generate_tac(node.left)
    right = generate_tac(node.right)
    temp = new_temp()
    tac.append(f"{temp} = {left} {node.value} {right}")
    return temp

def assign_tac(lhs, rhs):
    tac.append(f"{lhs} = {rhs}")

""" # Test code to run manually
if __name__ == "__main__":
    from parser import to_postfix, build_ast  # reuse parser functions

    # Example expression
    expression = "x = a + b * c"

    # Manually tokenize (like lexer would do)
    tokens = ['x', '=', 'a', '+', 'b', '*', 'c']

    # Extract RHS tokens (after '=')
    rhs_tokens = tokens[2:]

    # Step 1: Convert to postfix
    postfix = to_postfix(rhs_tokens)
    print("Postfix:", postfix)

    # Step 2: Build AST
    ast = build_ast(postfix)

    # Step 3: Reset TAC
    reset_tac()

    # Step 4: Generate TAC
    result = generate_tac(ast)

    # Step 5: Final assignment
    assign_tac(tokens[0], result)

    # Step 6: Display TAC
    print("\nThree Address Code:")
    for line in tac:
        print(line)
 """
