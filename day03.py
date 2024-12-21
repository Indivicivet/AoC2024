from aocd import data

# state machine approach, since regex would make this boring
multiplies = []
stack = None
for c in data:
    match c:
        case "m":
            stack = "m"
        case "u":
            stack = "mu" if stack == "m" else None
        case "l":
            stack = "mul" if stack == "mu" else None
        case "(":
            stack = "mul(" if stack == "mul" else None
        case "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9":
            if isinstance(stack, list):
                stack[-1] = stack[-1] + c
            elif stack == "mul(":
                stack = [c]
            else:
                stack = None
        case ",":
            if isinstance(stack, list) and len(stack) == 1:
                stack.append("")
            else:
                stack = None
        case ")":
            if isinstance(stack, list) and len(stack) == 2 and stack[1] != "":
                cmd = f"mul({stack[0]},{stack[1]})"
                assert cmd in data, cmd
                multiplies.append(int(stack[0]) * int(stack[1]))
            print(stack)
            stack = None
        case _:
            stack = None
print(sum(multiplies))
