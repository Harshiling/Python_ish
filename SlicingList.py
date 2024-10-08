names = ["chocolate" , "raspberry" , "vanilla", "strawberry"]
print("The first three items in the list are" , names[:3])
print("The three items from the middle of the list are" , names[1:])
print("All items in the list are", names[1:-2])

#Tuple are immutable lists , lists -> parantheses[] , tuples-> ()

tupleStrings = ("random" , "string")
for tuple in tupleStrings:
    print(tuple)

#values cannot be changed , instead a whole tuple can be reassigned

tupleStrings = ("NotRandom" , "String")
for tuple in tupleStrings:
    print(tuple)