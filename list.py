#list
#class example with square
kodvara=["Haresh", "Manish", "Kiran", "Manthan", "Naman"]
#adding one more member in family
kodvara.append("Harshit")
#kodvara.remove("Jay")
#tupple example with roucne brace, it cant be append
bhanushali=("Mange", "kodvara", "Gajra")

new_list=kodvara[0:4]
print("new list is ", new_list)
print(type(kodvara))
print(type(bhanushali))

print(kodvara)
print(bhanushali)

#printing 1st element from list
print(kodvara[0])

#printing 2nd element from tupple
print(bhanushali[1])


#print length

print(len(kodvara))
print("Total Surname of Bhanushali is", len(bhanushali))


#sorting
numbers=[11, 9, 90, 23]
print(numbers)
numbers.sort()
print("sorted number: ", numbers)

names=["met", "amal", "ziya"]
names.sort()
print(names)
random_string=[3, "Meet", 4, "Kodi"]
print(random_string)
