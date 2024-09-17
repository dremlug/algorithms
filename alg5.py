def conveer_sorting(sort_list_size: int, sort_list: list, template_list_size: int, temlate_list: list) -> str:
    
    untemplated_list = []
    i=0
    while sort_list[i] not in temlate_list:
        untemplated_list.append(sort_list.pop(i))
    i += 1
    while i < len(sort_list):
        if sort_list[i] not in temlate_list:
            untemplated_list.append(int(sort_list.pop(i)))
        else:
            current = sort_list[i]
            prev = i - 1
            while prev >= 0 and temlate_list.index(sort_list[prev]) > temlate_list.index(current):
                sort_list[prev + 1] = sort_list[prev]
                prev-=1
            sort_list[prev + 1] = current
            i += 1
    
    sort_list.extend(sorted(untemplated_list))
    return str.join(' ', map(str, sort_list))




if __name__ == '__main__':
    # print(conveer_sorting(int(input()), list(map(int, input().split())), int(input()), list(map(int, input().split()))))
    with open ('input', 'r') as f:
        resilt = conveer_sorting(int(f.readline()), list(map(int, f.readline().split())), int(f.readline()), list(map(int, f.readline().split())))
    with open ('output', 'w') as f_out:
        f_out.write(resilt)