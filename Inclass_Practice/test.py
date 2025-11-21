# Program to calculate pressure given the other inputs to van da waals equation.
# Vincent T Mukwevo MKWVIN004
# 20/02/2024

# Obtaining other inputs to van da waals equation from user.
V = eval(input('Enter the value of V:\n'))
Temp = eval(input('Enter the value of T:\n'))
a = eval(input('Enter the value of a:\n'))
b = eval(input('Enter the value of b:\n'))
R = 8.3145

# Calculating pressure using van da waals equation.
if V !=0  and (V-b) != 0 :
  pressure = round((R*Temp)/ (V- b )) - (a/(V*V))
  print('The Pressure, P, is %.0f' %pressure, end='.')