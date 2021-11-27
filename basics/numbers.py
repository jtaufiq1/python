# Decimal: base 10

print("Decimal Number")
d = 10
print(d)
print("\n")

# Binary: prefixed with 0b
print("Binary: Base 2")
b = 0b1010
print(bin(b), b)
print("\n")

# Octal: prefixed with 0o
print("Octal: Base 8")
o = 0o136
print(oct(o), o)

print(o / b)
print('\n')

# hexadecimal: prefixed with 0x
print("Hexadecimal: Base 16")
h = 0x12c
print(hex(h), h)
print("\n")

result = d + b + o + h
print("Decimal: ", result)
print("Binary: ", bin(result))
print("Octal: ", oct(result))
print("Hex: ", hex(result))
print('\n')

# complex numbers
