#list function (converting to list)
listFunc = list(range(2,9,3))
print(listFunc)
print(min(listFunc))
print(max(listFunc))
print(sum(listFunc))

for number in range(1,9):
    listFunc.append(number)
print(listFunc)

for number in range(1,100001):
    print(number,"\n")

#list comprehension
number = [value**3 for value in range(1,20)]
print(number)