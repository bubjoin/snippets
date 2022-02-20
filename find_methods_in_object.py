# eval() function returns the result of executing the expression given.
# eval(expression)
# getattr() function returns the attribute or the method in an object,
# with the name given.
# getattr(object, name[, default])
# if there is no thing with the name, it returns the default value.

attributes = []
methods = []

obj_name = str(input("Input the name of object: "))

for name in dir(eval(obj_name)):
    if callable(getattr(eval(obj_name), name)):
        methods.append(name)
    else:
        attributes.append(name)

for name in attributes:
    print(f'{obj_name}\'s attribute: {name}')

for name in methods:
    print(f'{obj_name}\'s method: {name}')