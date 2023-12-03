def get_bad_round(input_string):
    max_red = 12
    max_green = 13
    max_blue = 14
    round_number = int(input_string.split(':')[0][5::])
    round_data = input_string.split(':')[1].split(';')
    for round in round_data:
        for cubes in round.split(','):
            cubes = cubes.strip()
            number_cubes = int(cubes.split(' ')[0])
            color = cubes.split(' ')[1]
            if (color == "red" and number_cubes > max_red) or (color == "green" and number_cubes > max_green) or (color == "blue" and number_cubes > max_blue):
                return 0
    return round_number


def main():
    input_file = open('input','r')
    input_lines = input_file.readlines()
    sum = 0
    for line in input_lines:
        sum = sum + get_bad_round(line)

    print(sum)

if __name__ == "__main__":
    main()
