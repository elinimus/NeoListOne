# NeoListOne

Experiments with custom indexing in Python.

Use cases:

x - index
y - value

## INITIALIZATION

####creates an empty list
a = NeoListOne()

####creates list with 5 elements filled with zero
a = NeoListOne(5)

####creates list [1,2,3,4,5]
a = NeoListOne([1,2,3,4,5])

####creates list of 5 elements filled with number 7
a = NeoListOne(5,'7')

#### creates list of 5 elements [0,1,4,9,16]
a = NeoListOne(5,'x**2')

#### creates list of 6 elements [1,2,9,28,65,126]
a = NeoListOne(6,'x**3 + 1')


## STANDARD OPERATIONS

#### writes a value 9 at index 4
a[4] = 9

#### reads the value from index 5
a[5]


## APPEND

#### appends number 5 to the list
a['append'] = 5
a['append:'] = 5

#### appends 99 four times to the list
a['append: x < 4'] = 99

#### appends a number (y), but only if it satisfies the
#### conditions. In this case, because 101 is bigger than
#### 24, it will not be appended
a['append: y > 20 and y <24'] = 101

#### number 23 will be appended
a['append: y > 20 and y <24'] = 23

#### appends all numbers (y) from the list, which satisfy the
#### condition. In this case: 21, 22
a['append: y > 20 and y <24'] = [101,21,234,22]

#### appends all numbers with indexes (x) satisfying the
#### conditions. In this case: 26, 27
a['append: x > 2 and x < 5'] = [23,24,25,26,27,28,29,30]

#### appends entire list
a['append: x '] = [0,1,2,3,4,5,6,7]

#### appends values returned from function. In this case
#### three numbers 222 will be appended to the list
a['append: x < 3'] = lambda x,y: 222

#### 5,6 will be appended to the list
a['append: 1 < x and x < 4'] = lambda x,y: [3,4,5,6,7,8][x]

#### to the list will be appended 2**2+y and 3**2 + y, where
#### y is the value with the corresponding index x
a['append: 1 < x and x < 4'] = lambda x,y: x**2 + y


## COUNT

#### returns the number of occurrences of the number 4
a['count: 4']


## DELETE

#### deletes the entire content of the list
a['delete']
a['delete: :']
a['delete:::']

#### deletes elements with values equal to 4
a['delete: y == 4']

#### deletes all values bigger than 2
a['delete: y > 2']

#### deletes all values smaller than 3
a['delete: y < 3']

#### deletes all values between 2 and 4
a['delete: 2 <= y and y < 4']

#### deletes every second number starting from index 2 to 6
#### including
a['delete: 2:7:2']


## INDEX

#### returns the smallest index from the list with value equal to 3
a['index: 3']


## INSERT

#### inserts value 9 at index 0
a['insert: 0'] = 9

#### inserts value 9 at index 5
a['insert: 5'] = 9

#### inserts value 9 before the last element of the list
a['insert: -1'] = 9

#### appends 9 to the list if index is bigger than the index of
#### the last element of the list
a['append: 8'] = 9


## LEN

#### returns the length of the list
a['len']


## POP

#### returns the value of the last element from the list and deletes the
#### element
a['pop']


## POPLEFT

#### returns the value of the first element from the list and deletes the
#### element
a['popleft']


## PUSH

#### appends the value 9 to the list
a['push'] = 9


## SORT / ASCEND

#### sorts the list in ascending order of the values
a['sort']
a['ascend']

## REVERSE/DESCEND

#### sorts the list in descending order of the values
a['reverse']
a['descend']


## READ IN-PLACE INDEX:VALUE FILTER

#### returns a list of values if the index x satisfies
#### the conditions

#### returns the values with index less than 3
a[' x < 3'] 

#### returns the values with index bigger than 3
a[' x > 3'] 

#### returns values with index less than 3 or bigger than 5
a[' x < 3 or x > 5']

#### even more complicated statements could be written
a[' x < 3 or x > 5 and x%2']


#### returns a list of values if the value y satisfies
#### the conditions

#### returns a list with values bigger than 3
a['y > 3']

#### returns a list with values smaller than 3
a['y < 3']

#### returns a list with values bigger than 3, but
#### smaller than 9
a['3 < y and y < 9']

#### combination of the previous two techniques:
#### returns a list of the elements with index less than 8,
#### which have values bigger than 2

a['x < 8: y > 2']


## WRITE IN-PLACE INDEX:VALUE FILTER

#### writes value 5 into all elements with index less than 3
a[' x < 3'] = 5

#### with string variables
filter1 = ' x < 3'
filter2 = 'or x > 8'
a[filter1 + filter2] = 5

#### sets to 5 the value of all elements with value 4
a[' y == 4'] = 5

#### sets to 5 the value of all elements with value bigger than 4
a[' y > 4'] = 5

#### sets to 11 the value of all elements with index
#### less than 5 and value bigger than 3
a['x < 5: y > 3'] = 11

#### for every x and y which satisfies the conditions the function
#### is called and the returned value is written into the position
#### with index x
a['x < 5: y > 3'] = lambda x, y: x**2 + y


## FUNCTION INDEX:VALUE FILTERS

#### the same as in-place index filters, but the code is moved to 
#### functions

def filter1(x,y):
    return x < 5 and y > 25
    
def filter2(x,y):
    return x%2

#### because each filter is returning a boolean value,
#### the filters are combined with the logical operators (and, or, not)
def filter(x,y):
    return filter1(x,y) and filter2(x,y)

#### for writing
a[filter] = '2'
#### or
a[filter] = lambda x, y: x**2 + 2*y + 1

#### for reading
a[filter]
