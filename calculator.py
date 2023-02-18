num1 = int(input('please enter the first number: '))
num2 = int(input('please enter the secons number: '))
operator = input('please enter the operation you want: ')

if operator == '+':
    print ('the summation of', num1, 'and', num2, 'is', num1 + num2)
elif operator == '-':
    print ('the subtraction of', num1, 'and', num2, 'is', num1 - num2)
elif operator == '*':
    print ('the multiplication of', num1, 'and', num2, 'is', num1 * num2)
elif operator == '/':
    print ('the division of', num1, 'and', num2, 'is', num1 / num2)
