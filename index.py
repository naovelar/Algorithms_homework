#Reverse the list below in-place using an in-place algorithm.

words = ['this' , 'is', 'a', 'sentence', '.']

def Reverse(words):
    words.reverse()
    return words
    
print(words.reverse)

#Create a function that counts how many distinct words are in the string below, then outputs a dictionary with the words as the key and the value as the amount of times that word appears in the string.
#Should output:
#{'a': 5,
#'abstract': 1,
#'an': 3,
#'array': 2, ... etc...

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'




#Write a program to implement a Linear Search Algorithm. Also in a comment, write the Time Complexity of the following algorithm.

#Hint: Linear Searching will require searching a list for a given number.

nums_list = [10,23,45,70,11,15]
#If target not inside list, return -1

def linSearch(array,target):
