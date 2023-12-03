def get_calibration_value(messed_up):
    digit_one = ""
    digit_two = ""
    for i in range(0, len(messed_up)-1):
        if messed_up[i].isdigit():
            digit_one = messed_up[i]
            break

    for i in range(len(messed_up)-1,-1,-1):
        if messed_up[i].isdigit():
            digit_two = messed_up[i]
            break

    concat = digit_one + digit_two
    return int(concat)



def main():
    input_file = open('input_file','r')
    input_lines = input_file.readlines()
    sum = 0
    for line in input_lines:
        sum = sum + get_calibration_value(line)

    print(sum)

if __name__ == "__main__":
    main()