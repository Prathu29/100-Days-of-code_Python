# FUNCTION ARGUMENT AND RETURN STATEMENT

# def average(a,b =1):
#     print("The average is: ",(a+b)/2)

# average(a =2) # a is required argument


# Variable length arumment
# Example 1
# def average(*numbers): #numbers -> here this is tuple
#     sum = 0;
#     for i in numbers:
#         sum = sum + i
#     print("Average is: ",sum/len(numbers))

# average(1,5,7)


# Example 2
# def name(**name):
#     print(type(name))
#     print("Hello,", name["fname"],name["mname"],name["lname"])
# name(mname = "Glitch",lname = "prathu", fname = "oneshot")


# Return statement -> used to return the value of the expession back to the calling function

def average(*numbers):  # numbers -> here this is tuple
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)
c = average( 5, 6 ,7, 1)
print(c)
