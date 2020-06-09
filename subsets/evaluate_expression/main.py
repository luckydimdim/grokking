def diff_ways_to_evaluate_expression(input):
    '''
    Given an expression containing digits and operations (+, -, *),
    find all possible ways in which the expression can be evaluated by
    grouping the numbers and operators using parentheses.
    '''
    result = []

    if '+' not in input and '-' not in input and '*' not in input:
        result.append(int(input))
    else:
        for i in range(len(input)):
            curr = input[i]
            if not curr.isdigit():
                left_part = diff_ways_to_evaluate_expression(input[0:i])
                right_part = diff_ways_to_evaluate_expression(input[i+1:])

                for part1 in left_part:
                    for part2 in right_part:
                        if curr == '+':
                            result.append(part1 + part2)
                        elif curr == '-':
                            result.append(part1 - part2)
                        elif curr == '*':
                            result.append(part1 * part2)
    return result


def main():
    print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("1+2*3")))

    print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("2*3-4-5")))


main()

# 1+2*3
# (1+2)*3 (1+2*3) (1)+(2)*(3) 1+(2*3)
#
# 2*3-4-5
# ((2*3)-4)-5 2*((3-4)-5)