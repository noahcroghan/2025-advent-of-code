count_0 = 0
current_dial_value = 50

with open('input.txt') as file:
    for line in file:
        direction = line[0]
        amount = int(line[1:])

        if direction == 'L':
            current_dial_value = (current_dial_value - amount)  % 100
        else:
            current_dial_value = (current_dial_value + amount) % 100
        if current_dial_value == 0:
            count_0 += 1

print(count_0)