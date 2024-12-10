def part_a(data):
    disk = []
    for i, v in enumerate(list(data.raw)):
        btype = i // 2 if i % 2 == 0 else None
        disk += [btype] * int(v)

    for i in range(len(disk) - 1, -1, -1):
        if disk[i] and disk.index(None) < i:
            gap = disk.index(None)
            disk[gap], disk[i] = disk[i], disk[gap]

    return sum(i * v for i, v in enumerate(disk) if v)


def checksum(disk):
    i = 0
    checksum = 0
    for b, l in disk:
        for _ in range(l):
            if b is not None:
                checksum += i * b
            i += 1

    return checksum


def part_b(data):
    disk = []
    for i, v in enumerate(list(data.raw)):
        btype = i // 2 if i % 2 == 0 else None
        disk += [(btype, int(v))]

    for i in range(len(disk) - 1, -1, -1):
        b1, l1 = disk[i]
        if b1 is not None:
            for j, (b2, l2) in enumerate(disk):
                if i > j and b2 is None and l2 >= l1:
                    disk[i] = (None, l1)
                    disk = disk[:j] + [(b1, l1), (None, l2 - l1)] + disk[j + 1 :]
                    break

    return checksum(disk)
