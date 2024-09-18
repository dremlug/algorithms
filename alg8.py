def stones_matcher(stones_ordered_qty: int, stones_ordered: list[int],
                   stones_delivered_qty: int, stones_delivered: list[int]) -> int:
    stones_ordered = sorted(stones_ordered, reverse=True)
    stones_delivered = sorted(stones_delivered, reverse=True)
    count = 0
    i = 0
    j = 0
    while i < len(stones_delivered):
        if stones_delivered[i] >= stones_ordered[j]:
            count += 1
            i += 1
        j += 1
        if j == len(stones_ordered):
            break
    return count


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        result = stones_matcher(int(f.readline()), list(map(int, f.readline().split())), int(f.readline()),
                                list(map(int, f.readline().split())))
    with open('output.txt', 'w') as f_out:
        f_out.write(str(result))
