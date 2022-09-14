print('1. Model an organisation of employees, management and board of directors in 3 sets.')

#Put names into sets and do union/disjoint/difference to find overlap
board = {'Benny', 'Hans', 'Tine', 'Mille', 'Torben', 'Troels', 'Søren'}
management = {'Tine', 'Trunte', 'Rane'}
employees = {'Niels', 'Anna', 'Tine', 'Ole', 'Trunte', 'Bent', 'Rane', 'Allan', 'Stine', 'Claus', 'James', 'Lars'}

def set_formatter(set):
    nicely_formatted = ''
    for i in set:
        nicely_formatted = nicely_formatted + f'{i} '
    return print(nicely_formatted)

print(f'Board: {set_formatter(board)}')
print(f'Management: {set_formatter(management)}')
print(f'Employees: {set_formatter(employees)}')

def check_overlap(board, management, employees):
    print('Searching...')
    print('Who in the board of directors is not an employee?')
    #find diff directors, employee
    set_formatter(board - employees)

    print('\nWho in the board of directors is also an employee?')
    #find union directors, employees
    set_formatter(board & employees)

    print('\nHow many of the management is also member of the board?')
    #find union managment, board, then print as number
    print(f'{len(management & board)}, they are {board & management}')

    print('\nAll members of the managent also an employee')
    set_formatter(management & employees)

    print('\nAll members of the management also in the board?')
    set_formatter(management & board)

    print('\nWho is an employee, member of the management, and a member of the board?')
    set_formatter(management & board & employees)

    print('\nWho of the employee is neither a memeber or the board or management?')
    set_formatter(employees - board - management)
    return 'Search done.'
        
check_overlap(board, management, employees)

print('\n2. Using a list comprehension create a list of tuples from the folowing datastructure')
dict = {'a': 'Alpha', 'b' : 'Beta', 'g': 'Gamma'}
print(dict)

#Solution:
list = [(a, b) for a, b in dict.items()]
print(list, ' ', '\nThis data type is a: ', type(list))

print('\n3. From these 2 sets:')
print('{\'a\', \'e\', \'i\', \'o\', \'u\', \'y\'}')
print('{a\', \'e\', \'i\', \'o\', \'u\', \'y\', \'æ\' ,\'ø\', \'å}')
print('Create Union, Symmetric difference, difference, disjoint')

#Solution:
set1 = {'a', 'e', 'i', 'o', 'u', 'y'}
set2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}

print('Union: ' , set1 & set2) #return set
print('Symmetric difference: ', set1 ^ set2) #returns set of difference
print('Difference: ', set2 - set1) #returns set
print(f'Disjoint: {set1.isdisjoint(set2)}, The similarities between the sets are: {set1 & set2}') #bool 


print('\n4. Date Decoder.')
#A date of the form 8-MAR-85 includes the name of the month, which must be translated to a number.
#Create a dict suitable for decoding month names to numbers.
#Create a function which uses string operations to split the date into 3 items using the "-" character.
#Translate the month, correct the year to include all of the digits.
#The function will accept a date in the "dd-MMM-yy" format and respond with a tuple of ( y , m , d ).
def decode_date():
    date = input('input date in format dd-MMM-yy or dd-mmm-yy please. Otherwise the program returns an error.\n')
    print(f'Your input: {date}')

    months = {'JAN':1, 'FEB':2, 'MAR':3, 'APR':4, 'MAY':5, 'JUN':6, 'JUL':7, 'AUG':8, 'SEP':9, 'OCT':10, 'NOV':11, 'DEC':12}

    date_as_list = date.split('-')
    year = str('20' + date_as_list[2])
    month = str(months.get(date_as_list[1].upper()))
    day = str(date_as_list[0])
    date_reformatted = year + ', ' + month + ', ' + day
    print('Your input reformatted: ' + date_reformatted)


decode_date()