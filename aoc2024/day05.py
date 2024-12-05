def parse(data):
    rules, orders = data.raw.split("\n\n")
    rules = [x.split("|") for x in rules.splitlines()]
    orders = [x.split(",") for x in orders.splitlines()]
    return rules, orders


def check_order(order, rules):
    for rule in rules:
        if all([x in order for x in rule]):
            if order.index(rule[0]) > order.index(rule[1]):
                return False
    return True


def mid_sum(orders):
    return sum(int(x[len(x) // 2]) for x in orders)


def part_a(data):
    rules, orders = parse(data)
    return mid_sum(x for x in orders if check_order(x, rules))


def fix_order(order, rules):
    for rule in rules:
        if all([x in order for x in rule]):
            i1 = order.index(rule[0])
            i2 = order.index(rule[1])
            if i1 > i2:
                order[i2], order[i1] = order[i1], order[i2]
                return fix_order(order, rules)
    return order


def part_b(data):
    rules, orders = parse(data)
    orders = [fix_order(x, rules) for x in orders if not check_order(x, rules)]
    return mid_sum(orders)
