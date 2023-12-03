def get_round_power(input_string):
    min_cubes = {"red":0,"green":0,"blue":0}
    round_number = int(input_string.split(':')[0][5::])
    round_data = input_string.split(':')[1].split(';')
    for round in round_data:
        for cubes in round.split(','):
            cubes = cubes.strip()
            number_cubes = int(cubes.split(' ')[0])
            color = cubes.split(' ')[1]
            if number_cubes > min_cubes[color]:
                min_cubes[color] = number_cubes

    return min_cubes['red']*min_cubes['green']*min_cubes['blue']


def main():
    input_file = open('input','r')
    input_lines = input_file.readlines()
    sum = 0
    for line in input_lines:
        sum = sum + get_round_power(line)

    print(sum)

if __name__ == "__main__":
    main()
