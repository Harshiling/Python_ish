member_detail = {
    'name' : "Harshitha",
    'age' : 24,
    'email': "harshiling@gmail.com"
}

print(member_detail)
print(member_detail['name'])
print(f"We have a new member {member_detail['name']}")

# delete 
'''
This is a multiline comment
'''

# key error (exception when the key isn't present )
# print(member_detail['address'])
# Traceback (most recent call last):
#   File "Dictionary.py", line 17, in <module>
#     print(member_detail['address'])
# KeyError: 'address'

address_value = member_detail.get('address' , 'No value assigned')
print(address_value)

for info in member_detail:
    print(info.title())

#sorted
print("---sorted_dictionary------")
for info in sorted(member_detail):
    print(info.title())    

for info in member_detail.values():
    print(info)

# set
print("---set----")
member_detail_set = {'name' , 'address' , 'email', 'name'}
print(member_detail_set)

a = 4
b = 5

print(a / b)
