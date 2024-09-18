# ID 118350048
import string


def string_decrypt(encrypted_string: str) -> str:
    if encrypted_string == '':
        return ''
    index = 0
    decrypted_string = ''
    while index < len(encrypted_string):
        if encrypted_string[index] in string.digits:
            index_left = index
            while encrypted_string[index + 1] in string.digits:
                index += 1
            multiplier = int(encrypted_string[index_left:index+1])
            index += 1
        else:
            multiplier = 1

        if encrypted_string[index] == '[':
            start_index = index + 1
            count = 1
            while count > 0:
                index += 1
                if encrypted_string[index] == '[':
                    count += 1
                if encrypted_string[index] == ']':
                    count -= 1
            finish_index = index
            decrypted_string += multiplier * string_decrypt(encrypted_string[start_index:finish_index])
        else:
            decrypted_string += multiplier * encrypted_string[index]
        index += 1
    return decrypted_string


if __name__ == '__main__':
    # with open('input.txt', 'r') as f:
    #     result = string_decrypt(f.readline().strip())
    # with open('output.txt', 'w') as f_out:
    #     f_out.write(result)
    print(string_decrypt(input()))
