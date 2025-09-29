my_dict = {
"tuple": (
    'uno',
    'dos',
    'tres',
    'cuatro',
    'cinco'
),
"list": [
    'one',
    'two',
    'three',
    'four',
    'five'
],
"dict": {
    'key_one': 'value_one',
    'key_two': 'value_two',
    'key_three': 'value_three',
    'key_four': 'value_four',
    'key_five': 'value_five'
},
"set" : {
    1, 2, 3, 4, 5
}
}

print(my_dict["tuple"][-1])

my_dict["list"].append('six')
print(my_dict["list"])
my_dict["list"].pop(1)
print(my_dict["list"])

my_dict["dict"][('i am a tuple',)] = 'new_tuple'
print(my_dict["dict"])
my_dict["dict"].pop('key_three')
print(my_dict["dict"])

my_dict["set"].add(6)
print(my_dict["set"])
my_dict["set"].remove(6)
print(my_dict["set"])

print(my_dict)
