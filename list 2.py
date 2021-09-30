
favoritefoods = ['beans', 'waakye', 'tuo zaafi']

print ("these are my favourite foods -", favoritefoods)
print ("But i love ", favoritefoods[-2], "more ")

print ("and the last favourite is ",favoritefoods[0].upper())


ages = [2,3,5,6,8,9]
print(ages)
print(ages[1], ages[3])


#modifying a list and adding a list
#change an object at a specific index
favoritefoods[2] = 'gari'
print(favoritefoods)


#to add an object to the end of the list
favoritefoods.append('gabeans')

favoritefoods.insert(2,'wabeans')

print(favoritefoods)

#adding list to a list
favoritefoods.extend(ages)
print(favoritefoods)

#removing objects from list
favoritefoods.remove('beans')
favoritefoods.pop(4)
print(favoritefoods)