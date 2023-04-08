#Jayden Evans Coding Temple


#Question 1
#Write a function to print "hello_USERNAME!" 
#USERNAME is the input of the function. 
#The first line of the code has been defined as below.

def hello_name(user_name):
    print("hello_"+ user_name.upper()+"!")

#hello_name("Joymink")

#Question 2
#Write a python function
#first_odss that prints the odd numbers
#from 1-100 and returns nothing

def first_odds(): #Prints an odd number of odds per line
    x=1
    y=0
    z=1
    while x < 100:
        if x % 2 == 1:
            print( x, end=" ")
            y+=1
        if y%z==0:
            y=0
            z+=1
            print()
        x+=1
    print()
"""first_odds()"""


#Question 3
#Please write a Pythong Function, max_num_in_list
#to retunr the max number of a given list.

def max_num_in_a_list(a_list):
    x=a_list[0]
    max=0
    for i in a_list:
        if i > x:
            x=i
    max=x
    return max

num_list=[12,-2,1234,15,-100,3,2,1,1]
num_list2=[-31,-23,0,-21]

"""print(max_num_in_a_list(num_list))

print(max_num_in_a_list(num_list2))"""

#Question 4
#Write a function to return if a given year is a leap year
#A leap year is divisible by 4, but not by 100
#unless also divisible by 400
#Returns a boolean

def is_leap_year(a_year):
    answer= False
    x= a_year

    if x % 400 ==0: #checking if divis by 400
       return True
    elif x % 4 == 0 and x % 100 !=0: #divisible by 4 check and not by 100
        answer=True

    return answer

#print(is_leap_year(2000))


#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. 
#For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
#The return should be boolean Type.

def is_consecutive(a_list):
    start= a_list[0]
    check = True
    for num in a_list:
        if num != start:
            check= False
        start +=1
    
    return check

x = [1,2,3,4,5]
y = [1,2,3,5,4,3]
z = [-5,-4,-3,-2,-1]

"""print(is_consecutive(x))
print(is_consecutive(y))
print(is_consecutive(z))"""

while True:
    t=input("Which function would you like to see the output to?"+
      "\nQuestion 1: Greeting Function (1)"+"\nQuestion 2: Odd Number Function (2)"+
      "\nQuestion 3: Max Number Function (3)"+
      "\nQuestion 4: Leap Year Function (4)"+"\nQuestion 5: Consecutive Number Function (5)"+
      "\n----Press Q to Quit---\n")
    if t=="Q" or t=='q':
        print("Thank you for enjoying my code!")
        break
    elif int(t)== 1:
        print("Question 1: Creating a username greeting\n")
        name= input("Type in your username!\n")
        hello_name(name)
    elif int(t)==2:
        print("Question 2: Showing first odds from 1-100:\n")
        first_odds()
    elif int(t)==3:
        print("Question 3: Finding a max number inside a list\n ")
        temp=[]
        while True:
            num=input("Add a number (Press Q to quit) ")
            if(num == 'Q' or num =='q'):
                break
            else:
                temp.append(int(num))

        print("\nHere is your list: ")
        print(temp)
        print("\nHere is the max in your list: ", max_num_in_a_list(temp))
        print()
            
    elif int(t)==4:
        print("Question 4: Checking if year is a leap year.\n")
        while True:
            num=input("Check a year (Press Q to quit) ")
            if(num == 'Q' or num =='q'):
                break
            else:
                print("The answer if " + num +" is a leap year is: " ,is_leap_year(int(num)))
                print()
    
    elif int(t)==5:
        print("Question 5: Is this list consecutive numbers?\n")
        temp=[]
        while True:
            num=input("Add a number (Press Q to quit) ")
            if(num == 'Q' or num =='q'):
                break
            else:
                temp.append(int(num))
        print("\nHere is your list: ")
        print(temp)
        print("\nIs your list consecutive? ", is_consecutive(temp))
        print()
    else:
        print("Something went wrong, input a number from 1-5 or Q to quit\n\n")
    