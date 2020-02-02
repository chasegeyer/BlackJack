
def func():
    print("Func() in one.py")

print('TOP LEVEL IN one.py')

#__name__ is built in python function
# variable __name__ gets assigned a string
# if name = main if specific py file is being run directly

if __name__ == '__main__':
    print('One.py is being run directly!')

else:
    print('One.py has be imported!')