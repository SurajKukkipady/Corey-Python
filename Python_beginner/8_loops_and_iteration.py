nums = [1,2,3,4,5]

for num in nums:
    print(num)

print('Break loop')
for num in nums:
    if num == 3:
        print('Found')
        break
    print(num)

print('Continue loop')
for num in nums:
    if num == 3:
        print('Found')
        continue
    print(num)

print('loop in a loop')
for num in nums:
    for letter in 'abc':
        print(num, letter)

print('range function')
for num in range(5):
    print(num)

print('range function with starting value')
for num in range(2, 5):
    print(num)

print('While loop')
i = 0
while i < 5:
    print(i)
    i += 1

print('while loop with break')
i = 0
while i < 5:
    if i == 3:
        print('Found')
        break
    print(i)
    i += 1

print('while loop with continue')
i = 0
while i < 5:
    if i == 3:
        print('Found')
        i += 1
        continue
    print(i)
    i += 1