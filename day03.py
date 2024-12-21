from aocd import data

# state machine approach, since regex would make this boring
def get_multiplies(enable_do_dont_triggers):
    enabled = True
    multiplies = []
    stack = None
    for c in data:
        match c:
            case "d" if enable_do_dont_triggers:
                stack = "d"
            case "o" if enable_do_dont_triggers:
                stack = "do" if stack == "d" else None
            case "n" if enable_do_dont_triggers:
                stack = "don" if stack == "do" else None
            case "'" if enable_do_dont_triggers:
                stack = "don'" if stack == "don" else None
            case "t" if enable_do_dont_triggers:
                stack = "don't" if stack == "don'" else None
            case "m":
                stack = "m"
            case "u":
                stack = "mu" if stack == "m" else None
            case "l":
                stack = "mul" if stack == "mu" else None
            case "(":
                if isinstance(stack, str) and stack in {"mul", "do", "don't"}:
                    stack += "("
                else:
                    stack = None
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
                if enable_do_dont_triggers and stack == "do(":
                    enabled = True
                elif enable_do_dont_triggers and stack == "don't(":
                    enabled = False
                elif (
                    enabled
                    and isinstance(stack, list) and len(stack) == 2 and stack[1] != ""
                ):
                    cmd = f"mul({stack[0]},{stack[1]})"
                    assert cmd in data, cmd
                    multiplies.append(int(stack[0]) * int(stack[1]))
                print(stack)
                stack = None
            case _:
                stack = None
    return multiplies


print(sum(get_multiplies(False)))
print(sum(get_multiplies(True)))
