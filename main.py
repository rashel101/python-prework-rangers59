#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def greeting(name):
    print('hello'+ name.title() + '!')

def greeting_2(name):
    print( 'hello {} !'. format (name.title()))
    print (f'Hello again {name.title()}!')
    
greeting_2('rashel')

#Print first 100 odd numbers in Python
def odd_numbers():
    for i in range(0,101,2):
        print(i)

def odd_numbers2():
    numbers = list (range(0,101))
    for number in numbers:
        if number % 2 != 0:
            print(number)
odd_numbers()


#Please write a Python function, max_num_in_list to return the max number of a given list. 

def max_num_in_list (a_list):
    max_num= max(a_list)
    return max_num

test= max_num_in_list([2,3,5,8,9])
print(max_num_in_list([2,3,5,8,9]))

#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year (a_year):
    if a_year % 4 == 0 and (a_year % 400!= 0 or  a_year % 100 !=0):
        print(True)
    else:
        print(False)

is_leap_year(2019)

#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def is_consecutive (a_list):
    i=0
    status= True
    while i < len(a_list) - 1:
        if a_list[i]+ 1== a_list[ i +1 ]:
            i+= 1
        else :
            status= False
            break 
    print(status)
is_consecutive([1,2,3,4,5])

def welcome(marval_character):
    print(F'welcome to {marvel_character} Vision')
    
welcome('wanda')

  