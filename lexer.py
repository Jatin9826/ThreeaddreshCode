def tokenize(expression):
    tokens = []
    i = 0
    while i < len(expression):
        if expression[i].isspace():
            i += 1
        elif expression[i].isalnum() or expression[i] == '_':
            var = ''
            while i < len(expression) and (expression[i].isalnum() or expression[i] == '_'):
                var += expression[i]
                i += 1
            tokens.append(var)
        elif expression[i] in '+-*/=()<>':
            if expression[i] in ['<', '>'] and i + 1 < len(expression) and expression[i + 1] == '=':
                tokens.append(expression[i] + '=')
                i += 2
            else:
                tokens.append(expression[i])
                i += 1
        else:
            raise ValueError(f"Invalid character: {expression[i]}")
    return tokens