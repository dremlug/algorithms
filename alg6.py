def block_sort(array_size: int, array: list) -> int:
    max_number = array_index = count = 0
    target = 0

    while True:
        switch = False
        # start_index = array_index
        # while (switch is False or array_index < max_number + 1 - start_index) and array_index < len(array):
        while (switch is False or array_index < max_number + 1) and array_index < len(array):
            if array[array_index] == target:
                switch = True
            if array[array_index] > max_number:
                max_number = array[array_index]
            array_index += 1
        count += 1
        target = max_number + 1
        if array_index == len(array):
            break
    return count


if __name__ == '__main__':
    with open('input.txt', 'r') as f_input:
        result = block_sort(int(f_input.readline()), list(map(int, f_input.readline().split())))
    with open('output.txt', 'w') as f_output:
        f_output.write(str(result))
