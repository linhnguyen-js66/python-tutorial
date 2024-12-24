# Ex1: Write a program that encrypts a message as follows: 
# * All the occurrences of letter 'a' in the messafe are replaced by 'e'
# * All the occurrences of letter 'e' in the messafe are replaced by 'i'
# * All the occurrences of letter 'i' in the messafe are replaced by 'o'
# * All the occurrences of letter 'o' in the messafe are replaced by 'u'
# * All the occurrences of letter 'u' in the messafe are replaced by 'a'

# Ex: This is the original message used
# => Thos os thi urogonel missegi asid

names = "This is the original message used"
names2 = ""
for i in range(len(names)):
    if names[i] == "a":
        names2 = names2 + "e"
    elif names[i] == "e":
        names2 = names2 + "i"
    elif names[i] == "i":
        names2 = names2 + "o"
    elif names[i] == "o":
        names2 = names2 + "u"
    elif names[i] == "u":
        names2 = names2 + "a"
    else:
        names2 = names2 + names[i]
print(names) #This is the original message used
print(names2) #Thos os thi urogonel missegi asid
print(names2[::-1]) #disa igessim lenogoru iht so sohT

#Ex2: Define a function that takes in a positive integer n as its parameter.
#The function returns a string that contains the intergers from 1 to n in an alternative
#For example, if n is 4, the function returns the string '1-3-2-4'
#If n is 7, the function returns the string '1-3-2-4-3-5-4-6-5-7'

#Note the following special cases:
# * if n is 1, then the finction returns the string '1'
# * if n is 2, then the finction returns the string '1-2'
# * if n is 3, then the finction returns the string '1-3'

#Output: 1-3-2-4
#1-3-2-4-3-5-4-6-5-7


def get_num_str(n):
    chars = []
    if(n > 2):
        for num in range(1, n-1):
            chars.append(str(num))
            chars.append(str(num + 2))
    return "-".join(chars)

get_num_str(6)