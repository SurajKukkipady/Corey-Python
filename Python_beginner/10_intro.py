#import import_module as mm
#from import_module import *
from import_module import find_index
import sys

courses = ['History', 'Math', 'Physics', 'CompSci']

#index = mm.find_index(courses, 'Math')
index = find_index(courses, 'Math')
print(index)
#print(mm.test)
print(sys.path)