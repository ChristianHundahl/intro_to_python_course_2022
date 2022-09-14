from collections import namedtuple

list = ['Hello', 'World', 'Huston', 'we', 'are', 'here']

print(list[1:5]) #World houston we are
print(list[1 : -1]) #Alternative way of excluding 1st and last letters
print(list[1 : len(list)-1]) #Alternative way of excluding 1st and last letters
#len() naturally counts from 1 and up, as humans usually do
#The list index counts naturally up from 0
#You can cast values as other data tyopes easily by data_type(value)
print(tuple(list))
#Index slicing also applicable to strings as these are also lists of characters
print("Hello world"[0:5]) #Produces 'Hello'

print(list[0:2]) #Hello world

print(list[4::]) #are here

print(list[4]) #are - returns as a string
print(list[4:5]) #are - returns as a list

print(list[0:: 2]) 

print(list[::-1]) #['here', 'are', 'we', 'Huston', 'World', 'Hello']

print(list[1:5]) #['World', 'Huston', 'we', 'are']

t = ('Claus', 51, 'male', 'clbo@kea.dk', 31011970-1313) #Tuple claus
print(t)

list1 = ['Bmw', 'Toyota', 'Hyundai', 'Skoda', 'Fiat', 'Volvo']
list2 = ['Claus', 'Henning', 'Torben', 'Carl', 'Tine']

t2 = ('Hello', 'World', 'Huston', 'we', 'are', 'here')

t3 = ('Rolling Stones', 'Goats Head Soup', 31, 'August 1973', '46:56')

address = namedtuple('address', ['coordinate_y', 'coordinate_x', 'city', 'state', 'country'])

address1 = address(40.730610, -73.935242, 'New York City', 'NY', 'USA') 
address2 = address(31.739847, 65.755920, 'Kandahar', 'Kandahar Province', 'Afghanistan')

print(address1.coordinate_y, address1.city)
print(address2.state, address2.country)

def string_sorter(s):
    characters = [*s] #Splits string s into list of individual characters
    consonants = []
    wovels = ['a', 'e', 'i', 'o', 'u', 'y', ' ']
    for i in characters:
        if i not in wovels:
            consonants.append(i)

    return print(f'Removing wovels from "{s}" leaves the letters: {sorted(consonants)}')
    
string_sorter('hi there bobby')

names = ['Bob', 'Adam', 'Peter']

print(f"Names in alphabetical order: {sorted(names)}")#Sorted(): Does not change original object, works on all iterable objects. sort() changes original, works only on lists
print(f'Names in reverse alphabetical order: {sorted(names, reverse=True)}')
print(f'Names sorted by length: {sorted(names, key=len)}') #Sorted() always from lowest to highest
print(f'Names sorted alphabetically by end letter: {sorted(names, key=lambda x: x[::-1])}')

names.append('Stuart')
print(f'Appended list unsorted: {names}')
def contains_a(s):
    if 'a' in s:
        return False
    return True

print(f'Names sorted alphabetically by names containing the letter \'A\': {sorted(names, key=contains_a)}') #False sorted before True?