def generate_quadruples(tac):
    quads = []
    for line in tac:
        if '=' in line:
            result, expr = line.split(' = ')
            parts = expr.split()
            if len(parts) == 3:
                op, arg1, arg2 = parts[1], parts[0], parts[2]
            else:
                op, arg1, arg2 = '=', parts[0], None
            quads.append((op, arg1, arg2, result))
    return quads

def print_quadruples(quads):
    print("\nQuadruple Representation:")
    print("Op\tArg1\tArg2\tResult")
    for q in quads:
        print("\t".join(q if q[2] else (q[0], q[1], '_', q[3])))
