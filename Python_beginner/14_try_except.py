
try:
    f = open('text.txt')
except FileNotFoundError as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executes no matter what")

