weight = input('Please type your weight:')
Height = input('Please type your height:')
weight = float(weight)
Height = float(Height)
BMI = weight/((Height/100) *(Height/100))
print('BMI:', BMI)
if BMI < 18.5:
    print('Weight too low')
elif BMI >= 18.5 and BMI < 24:
    print('Keep your weight')
elif BMI >= 24 and BMI < 27:
    print('little bit heavy')
elif BMI >= 27 and BMI < 30:
    print('light fat')
elif BMI >= 30 and BMI < 35:
    print('middle fat')
else:
    print('too fat')
