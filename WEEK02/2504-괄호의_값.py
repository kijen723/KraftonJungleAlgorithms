# https://www.acmicpc.net/problem/2504

def bracket():
    string = input()
    stack = []
    count = 1
    answer = 0
    calculate = False

    for i in string:
        if i == '(':
            count *= 2
            stack.append(i)
            calculate = True
        elif i == '[':
            count *= 3
            stack.append(i)
            calculate = True
        else:
            if stack:
                if i == ')' and stack[-1] == '(':
                    if calculate == True:
                        answer += count
                    count //= 2
                    calculate = False
                    stack.pop()
                elif i == ']' and stack[-1] == '[':
                    if calculate == True:
                        answer += count
                    count //= 3
                    calculate = False
                    stack.pop()
                else:
                    return 0
            else:
                return 0

    if not stack:
        return answer
    else:
        return 0


print(bracket())
