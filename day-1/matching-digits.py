def match_digit(captcha, distance_to_matching_digit):
   matching_digits_sum = 0
   for digit_index in range(captcha_length):
       other_side_index = (digit_index + distance_to_matching_digit) % captcha_length
       if captcha[digit_index] == captcha[other_side_index]:
           matching_digits_sum += int(captcha[digit_index])
   return matching_digits_sum


if __name__ == "__main__":
    input_file = open("data/input.txt", "r")
    captcha = input_file.read()
    captcha_length = len(captcha)
    other_side_index_distance = int(captcha_length / 2)
    print('Sum of digits matching the next digit in the captcha: ', match_digit(captcha, 1))
    print('Sum of digits matching the digit farthest away from itself in the captcha: ', match_digit(captcha, other_side_index_distance))
