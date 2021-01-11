a = float(input('Please Enter Your Percentage (without % symbol) : '))
name = input('Please tell me your name .')
if a >= 91.00:
    print(name , 'your grade is A.')
elif 81.00 <= a < 90.00:
    print(name , 'your grade is B.')
elif 65.00 <= a < 80.00:
    print(name , 'your grade is C.')
elif 51.00 <= a < 65.00:
    print(name , 'your grade is D.')
elif 33.00 <= a < 51.00:
    print(name , 'your grade is E.')
elif a < 33.00:
    print(name , 'your are failed . Your grade is F.')