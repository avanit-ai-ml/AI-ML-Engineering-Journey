# 3. String Formatting - f-string & format()

a = 5
b = 15
c = a+b

#----------- Format Function -----------
print("Sum {}".format(c))

print("Sum of {}, {}, is: {}".format(a, b, c))

# Index based formatting
print("Sum of {1}, {0}, is: {2}".format(a, b, c))

# Value based formatting
print("Sum of {a}, {b}, is: {c}".format(a = 9, b = 90, c = a+b)) # Here value oc c = 20 instead of 99

#----------- f-string -----------
print(f"Average of {a} & {b} : {(a+b)/2}")