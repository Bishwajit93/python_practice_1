#countries = ['Bangladesh', 'India', 'Pakistan', 'china', 'Malayasia', 'North Korea', 'South Korea']
# countries = list(('Bangladesh', 2, 'India', 'Pakistan', 'china', False))
# countries[1] = 'hellobello'
# print(countries)
# print(type(countries))
# print(type(countries[0]))
# print(len(countries))



#list methods

list1 = [2,4,1,3,5]

#sorting the array in ascending order
list1.sort()
print(list1)

#reversing the list
list1.reverse()
print(list1)

#copying the list
list3 = list1.copy()
print(list3)

list2 = ['banana', 'apples', 'mango', 'oranges', 'banana']

#finding the index number of the element
#print(list2.index('apples'))

#extend method
#list1.extend(list2)
#print(list1)

#finding the number of an element in the list i.e. mango- 2/3 times
#print(list2.count('banana'))

#append method
#list2.append('cherry')
#print(list2)

#insert method(take 2 parameters)
#list2.insert(2, 'cherry')
#print(list2)

#remove method
#list2.remove('banana')
#print(list2)

#clear method for the whole list
#list2.clear()
#print(list2)

#delete method for removing the last value of the list
list2.pop()
list2.pop(1)
del list2[2]
#del list2
print(list2)
