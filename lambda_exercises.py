''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''
from multiprocessing.context import set_spawning_popen
from ssl import VerifyFlags


originalList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evenNums = list(filter(lambda num: num % 2 == 0, originalList))
print(evenNums)

oddNums = list(filter(lambda num: num % 2 != 0, originalList))
print(oddNums)


''' 2)
find which days of the week have exactly 6 characters.
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

sixChars = list(filter(lambda day: len(day) == 6, weekdays))
print(sixChars)


''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

'''

words = ['orange', 'red', 'green', 'blue', 'white', 'black']

newWords = list(filter(lambda words: words != 'orange' and words != 'black',words))
print(newWords)



''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

list3 = list(filter(lambda n: n not in list2,list1))
print(list3)


''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

'''

colors = ['red', 'black', 'white', 'green', 'orange']

substring = 'ack'
substring2 = 'abc'

search = list(filter(lambda n: substring in n,colors))
print(search)

search2 = list(filter(lambda n: substring2 in n,colors))
print(search2)




''' 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''

password = 'thisIsmypassword1'
password = list(password)

verifier = lambda i: i.isupper()

print(any(filter(verifier,password)))



''' 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''
