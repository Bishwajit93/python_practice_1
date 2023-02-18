try:
    x = int(input('enter a number: '))
    print(x)

except ValueError:
    print('value is not an integer')

else:
    print('nothing went wrong')

finally:
    print('try and except finished')
