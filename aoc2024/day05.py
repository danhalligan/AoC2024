def parse(data):
    rules, orders = data.raw.split("\n\n")
    rules = [x.split("|") for x in rules.splitlines()]
    orders = [x.split(",") for x in orders.splitlines()]
    return rules, orders


def check_order(x, rules):
    return not any(a in x and b in x and x.index(a) > x.index(b) for a, b in rules)


def mid(x):
    return int(x[len(x) // 2])


def part_a(data):
    rules, orders = parse(data)
    return sum(mid(x) for x in orders if check_order(x, rules))


def fix_order(x, rules):
    for a, b in rules:
        if a in x and b in x:
            i1 = x.index(a)
            i2 = x.index(b)
            if i1 > i2:
                x[i2], x[i1] = x[i1], x[i2]
                return fix_order(x, rules)
    return x


def part_b(data):
    rules, orders = parse(data)
    orders = [fix_order(x, rules) for x in orders if not check_order(x, rules)]
    return sum(mid(x) for x in orders)
