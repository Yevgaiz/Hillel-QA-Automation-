num = int(input('Enter n: '))

if num < 1 or num > 9:
    print('n could be in range 1 <= n <= 9')
    exit()

for i in range(1, num + 1):
    for x in range(num - i):
        print("  ", end="")
    for y in range(1, i + 1):
        print(y, end=" ")
    for z in range(i - 1, 0, -1):
        print(z, end=" ")
    print("")