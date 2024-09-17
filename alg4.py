def schitalka(n,m,start=0):
    if len(n) == 1:
        return int(n[0])
    index_to_out = m % len(n) - 1 if m % len(n) != 0 else len(n) - 1
    # print(index_to_out)
    if (index_to_out + start <= len(n) - 1):
        index_to_out = index_to_out + start 
    else:
        index_to_out = index_to_out + start - len(n)
    start = index_to_out
    n.pop(index_to_out)
    schitalka(n,m,start=start)

    return int(n[0])


if __name__ == '__main__':
    print(schitalka(list(range(1,int(input())+1)), int(input())))
