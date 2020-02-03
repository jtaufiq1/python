# Dynamic variable
# Primitive type: Integers, floats and string

print("*" * 10)
print("variables in python".upper())
students_count = 1000
rating = 4.99
is_published = False
 
course_name = "Python" # String can be in double or single quotes
 
# Multiline String 
multiline_string = """
    This string spans
    multiple line
    """
# One line initialization of variables
x, y = 3, 4

# Determine type of variables
print("\ndetermining type of variables".title())
print("*" * 10)
print(type(students_count))
print(type(rating))
print(type(is_published))

type(True)
type(4)
type("text")
type(4.2)

# Type Annotation
is_bool:bool = True
age:int = 20
rate: float = 4.5
name: str = "type annotation".title()
print("*" * 10)
# print(name)
print(is_bool)
print(age)
print(rate)


# Mutable and Immutable types
print("*" * 10)
print("mutable and immutable type\n".title())

# primitive types are immutable
print("primitive types")
print("all primitive types are immutable".title())
x = 1
print(id(x))
x = x + 1
print(id(x)) # prints memory location of vars

# List are mutable
y = [1, 2, 3]
print(id(y))
y.append(4)
print(id(y))
