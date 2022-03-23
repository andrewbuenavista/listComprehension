# numbers 0 thru 9
x = [i for i in range(10)]
print(x)

# adding an expression - square of each number
squares = [i**2 for i in range(10)]
print(squares)

# multiply each element by 3
list1 = [3,4,5]
multiplied = [item * 3 for item in list1]
print(multiplied)

# word manipulation
listOfWords = ['this','is','a','list','of','words']
words = [i[0] for i in listOfWords]
print(words)

# transform letters to lowercase
letters = ['A','B','C']
lowered = [i.lower() for i in letters]
print(lowered)

# adding an if condition
newrange = [i * i for i in range(5) if i%2 == 0]
print(newrange)

# selecting only certain items
string = 'Hello 12345 world'
numbersOnly = [i for i in string if i.isdigit()]
print(numbersOnly)
lettersOnly = [i for i in string if i.isalpha()]
print(lettersOnly)

# using a file
myfile = open('test.txt','r')
result = [i.rstrip('\n') for i in myfile if 'line3' in i]
print(result)

# using functions
def double(x):
    return x*2

print(double(10))

myNumbers = [double(x) for x in range(10) if x%2 == 0]
print(myNumbers)

# you can add more arguments
twoargs = [x + y for x in[10,30,50] for y in [20,40,60]]
print(twoargs)