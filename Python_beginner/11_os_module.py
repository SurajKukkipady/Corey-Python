import os
from datetime import datetime

#print(dir(os))
print(os.getcwd())
os.chdir("C:/Users/suraj/OneDrive/Documents/Corey_Python")
print(os.getcwd())

print(os.listdir())

print(os.stat('Python_beginner'))
mod_time = os.stat('Python_beginner').st_mtime
print(mod_time)
print(datetime.fromtimestamp(mod_time))

os.walk()
