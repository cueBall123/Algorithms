__author__ = 'cue'

def answer(str):
    operands = []
    operators = []

    for i in range(len(str)):
        if str[i].isnumeric():
            operands.append(str[i])
        else:
            if len(operators) == 0:
                operators.append(str[i])
            else:
                last_oper = operators.pop()
                if str[i] == '+' and last_oper == '*':
                    operands.append(last_oper)

                    while len(operators) != 0:
                        pop = operators.pop()
                        if pop == '+':
                            operators.append(pop)
                            break
                        else:
                            operands.append(pop)
                    operators.append(str[i])
                else:
                    operators.append(last_oper)
                    operators.append(str[i])

    while len(operators)!=0:
        operands.append(operators.pop())
    print (''.join(operands))
if __name__ == '__main__':
    answer("2+3*2")
