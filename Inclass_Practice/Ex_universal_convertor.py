# program to convert units given parameters
# lecture CSC1015F

from_unit = input("What are the units to convert from ? ")
how_many = eval(input("How many input do you want to convert"))
convertin_scale = eval(input("how many", to_units, "are in", from_unit, sep = " "))

# calculating result
result = convertin_scale * from_unit
result_rounded_down = floor(result)
print ("result is", result_rounded_down, to_units)