total = 0

with open('input.txt') as file:
    for line in file:
        digits = [int(char) for char in line.strip()]
        best = 0

        for i in range(len(digits) - 1):
            tens = digits[i]
            ones = max(digits[i+1:])
            value = tens * 10 + ones
            best = max(best, value)

        total += best

print(total)