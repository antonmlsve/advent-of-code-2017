def match_next_digit(captcha):
    match_sum = 0
    previous_digit = captcha[0]
    for digit_index in range(1, len(captcha)):
        if(previous_digit == captcha[digit_index]):
            match_sum += int(previous_digit)
        previous_digit = captcha[digit_index]
    if(captcha[0] == captcha[-1]):
        match_sum += int(captcha[0])
    return match_sum

def match_other_side_of_list_digit(captcha):
    match_sum = 0
    captcha_length = len(captcha)
    other_side_distance = int(captcha_length / 2)
    for digit_index in range(captcha_length):
        other_side_index = (digit_index + other_side_distance) % captcha_length
        if(captcha[digit_index] == captcha[other_side_index]):
            match_sum += int(captcha[digit_index])
    return match_sum


if __name__ == "__main__":
    input_file = open("data/input.txt", "r")
    captcha = input_file.read()

    print('Sum of digits matching the next digit in the captcha: ', match_next_digit(captcha))
    print('Sum of digits matching the digit farthest away from itself in the captcha: ', match_other_side_of_list_digit(captcha))
