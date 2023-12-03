import re

def get_calibration_value(messed_up):
    relations = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
    regex = "(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
    answers = re.findall(regex,messed_up)
    digit_one = answers[0]
    digit_two = answers[-1]
    if len(digit_one) != 1:
        digit_one = relations[digit_one]
    if len(digit_two) != 1:
        digit_two = relations[digit_two]
    concat = digit_one + digit_two
    return int(concat)

def main():
    input_file = open('input','r')
    input_lines = input_file.readlines()
    sum = 0
    for line in input_lines:
        sum = sum + get_calibration_value(line)

    print(sum)

if __name__ == "__main__":
    main()