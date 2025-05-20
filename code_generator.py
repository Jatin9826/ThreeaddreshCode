temp_count = 0
tac = []

def new_temp():
    global temp_count
    temp_count += 1
    return f"t{temp_count}"

def reset_tac():
    global tac, temp_count
    tac = []
    temp_count = 0

def generate_tac(node):
    if not node.left and not node.right:
        return node.value
    left = generate_tac(node.left)
    right = generate_tac(node.right)
    temp = new_temp()
    tac.append(f"{temp} = {left} {node.value} {right}")
    return temp

def assign_tac(lhs, rhs):
    tac.append(f"{lhs} = {rhs}")
    return tac