# File Objects

f = open('text.txt', 'r')
print(f.name)
f.close()

print('######## Using Context Managers #########')

with open('text.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)
    f.seek(0) # Because the curor will be in the end of the file
    f_contents = f.readlines()
    print(f_contents)
    f.seek(0)
    print('######### Using for loop ########')
    for line in f:
        print(line, end='')

    f.seek(0)

    print(f.tell())

with open ('text.txt', 'w') as f:
    f.seek(10)
    f.write('Test')


