import math
import os

#question1
def question1(a_string):
    lowercase = a_string.lower()
    vowel_counts = {} #storage to sum every vowel I encounter
    for vowel in "aeiou": #indicate what I consider vowels
        count = lowercase.count(vowel) # change to lowercase because uppercase is treated differently
        vowel_counts[vowel] = count # sum each vowel instance
    print(vowel_counts)

    counts = vowel_counts.values()

    total_vowels = sum(counts)
    total_char = len(a_string) #find the length of the string
    total_consonant = total_char - total_vowels # calculate the number of consonants

    print(total_char)
    print(total_vowels)
    print(total_consonant)

    if total_vowels > total_consonant:
        print("True")
    elif total_consonant > total_vowels:
        print("False")
    elif total_consonant == total_vowels:
        print("Null")

#question2
def question2(radius,height):
    pie = math.pi #3.14
    
    new_radius = radius*radius #square the radius
    
    print("volume =", end = " ")
    print(pie*new_radius*height) #volume = pi * radius^2 * height

#question3
def question3(c_list):
    comma_separated = ",".join(c_list)#adds a comma between each item in the list
    print(comma_separated)

#question4
def question4(my_list):
    #my_list=["apple", "orange", "grapes", "tangerine"]
    #print(my_list)
    comma_separated = ",".join(my_list) 
    
    #print(comma_separated)
    x=[]
    her_list = []
    long_list = []
    your_list=["yellow", "blue", "purple", "red"]
    long_list.append(your_list)
    her_list = ["shoes", "socks", "coat"]
    long_list.append(her_list)
    long_list.append(my_list)
    
    for i in long_list:
        x=i
        y= ",".join(x) #.join takes all items in an iterable and makes a single string
        #print(y, end = ",")
        f = open("demo.txt", "a")
        f.write(y) #writes text to a file
        f.close()
        
        f = open("demo.txt", "r") #open & read "r" the file
        #print(f.read())
path = os.path.abspath("demo.txt") #store the path of the file to a variable
print(path)

#question5
def question5 (filename):
    from csv import reader
    # read csv file as a list of lists
    with open(filename, 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)
        print(list_of_rows)
       

#question6
def divide(first, second):
    answer = first/second
    print(answer)
    
def division_error(first,second):
    try:
        divide(first,second)
    except ZeroDivisionError:
        print("warning")

#question7
def question7(l):
    print(l)
    print(list(set(l))) #casting the set(no duplicates) into a list form

#question8   
def question8():
    os.mkdir('hw3-folder') #creates a directory in the current directory



#question1("Monica")
#question2(2,3)
#question3(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
#question4(["apple", "orange", "grapes", "tangerine"]) 
#question5() 
#division_error(9,0) 
#question7([1,2,3,4,5,6,1,2,3]) 
#question8()