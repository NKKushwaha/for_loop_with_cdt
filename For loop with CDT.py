# for loop with tuple
'''
T=(11,22,33,'hello')
for i in T:
    print(i)
'''

# for loop with list
'''
L=[11,22,33,'hello']
for i in L:
    print(i)
'''

# for loop with String
'''
S='Nitish'
for i in S:
    print(i)
'''

# for loop with Set
'''
S={11,22,33,('hello',90)}
for i in S:
    print(i)
'''

# For loop with dictionary directly (it will consider key)
'''
d={'name':'Nitish','age':22}
for key in d:
    print(key,d[key])  
'''

# For loop with item method of dictionary 
'''
d={'name':'Nitish','age':22}
for key,value in d.items():
    print(key,value)  
'''

#W.A.P.T. print how many elements are given string
                #or
#W.A.P.T. show the implementation of length function
'''
S=input()
C=0
for ele in S:
    C+=1
print('Number of elementin string is',C)
'''

'''
1. Taking the string from user('12n@')
2. initializing C=0 by assuming the string is not present 
3. Extracting each and every elements
itration:1:
    i='1'
    Increment C value (C=1)
itration:2:
    i='2'
    Increment C value (C=2)
itration:3:
    i='n'
    Increment C value (C=3)
itration:4:
    i='@'
    Increment C value (C=4)
At last print the C value which is 4
'''

#W.A.P.T. print how many times the given sub string is present in specified string
'''
MS=input()
sub=input()
c=0
for i in MS:
    if i==sub:
        c+=1
print(c)
'''

'''
1. Taking the main string from user('Nit')
2. Taking the sub string from user('i')
3. initializing C=0 by assuming the sub string is not present in the main string
Extract each and every element
itration:1:
    i='N'
    Now we are comparing 'N' with 'i'
    it not true so don't increment C value (C=0
itration:2:
    i='i'
    Now we are comparing 'i' with 'i'
    it is true so increment C value (C=1)
itration:3:
    i='t'
    Now we are comparing 't' with 'i'
    it not true so don't increment C value (C=1)
At last print the C value which is 1
'''
#W.A.P.T. print how many vowels are present in given string
'''
S=input()       # Taking input from User
V='aeiouAEIOU'  # Given vowels Element in string
C=0             # Assuming the given string is not present in the elements
for i in S:     # Extracting each and evenry elemsents 
    if i in V:  # Comparing the element from the vowels
        C+=1    # for every element we can add 1
print(C)        # At last we can print the total number of elements

'''

'''
1. Taking the string from user('Nit')
2. Given vowels Element in string
3. Initializing C=0 by Assuming the given string is not present
Extract each and every element
itration:1:
    i='N'
    Now we are comparing 'N' with 'aeiouAEIOU'
    it not true so don't increment C value (C=0)
itration:2:
    i='i'
    Now we are comparing 'i' with 'aeiouAEIOU'
    it is true so increment C value (C=1)
itration:3:
    i='t'
    Now we are comparing 't' with 'aeiouAEIOU'
    it not true so don't increment C value (C=1)
At last print the C value which is 1
'''


#W.A.P.T. print how many Consunent are present in given string

'''
S=input()
A='aeiouAEIOU'
C=0
for i in S:
    if i not in A and i.isalpha():
        C+=1

print(C)

'''

'''
1. Taking the string from user('Ni1$')
2. Given vowels Element in string
3. Initializing C=0 by Assuming the string is not present or empty string
Extract each and every element
itration:1:
    i='N'
    Now we are checking 'N' is not present 'aeiouAEIOU' and the element is alphabets 
    it true so increment C value (C=1)
itration:2:
    i='i'
    Now we are checking 'i' is not present 'aeiouAEIOU' and the element is alphabets 
    it not true so don't increment C value (C=1)
itration:3:
    i='1'
    Now we are checking '1' is not present 'aeiouAEIOU' and the element is alphabets 
    it not true so don't increment C value (C=1)
itration:4:
    i='$'
    Now we are checking '$' is not present 'aeiouAEIOU' and the element is alphabets 
    it not true so don't increment C value (C=1)
At last print the C value which is 1
'''


# W.A.P.T. count even and odd of the given series of number 
'''
N=eval(input())
C=0
for i in N:
    if i%2==0:
        C+=1
print(f'The odd number is {C}')
for i in N:
    if i%2!=0:
        C+=1
print(f'The even number is {C}')
'''

'''
1. Taking the list from user(['N',1,2])
2. Initializing C=0 by Assuming the list is not present or empty empty list
Extract each and every element
itration:1:
    i='N'
    Now we are comapre 'N' with i%2==0
    its not true so don't increment C value(C=0)
itration:2:
    i='1'
    Now we are comapre '1' with i%2==0
    its not true so don't increment C value(C=0)
itration:3:
    i='2'
    Now we are comapre '2' with i%2==0
    its true so increment C value(C=1)
AT last print the C value which is 1

Extract each and every element
itration:1:
    i='N'
    Now we are comapre 'N' with i%2!==0
    its not true so don't increment C value(C=0)
itration:2:
    i='1'
    Now we are comapre '1' with i%2!==0
    its true so increment C value(C=1)
itration:3:
    i='2'
    Now we are comapre '2' with i%2!==0
    its nor true so don't increment C value(C=1)
AT last print the C value which is 1
'''

# W.A.P.T. find the program that accept a string and calculatethe number of digit and letter
'''
N=input()
C=0
for i in N:
    if i.isalpha():
        C+=1
print(f'The letter is {C}')
for i in N:
    if i.isdigit():
        C+=1
print(f'The digit is {C}')    
'''        

'''
1. Taking the string from user(N1)
2. Initializing C=0 by Assuming the list is not present or empty empty list
Extract each and every element
itration:1:
    i='N'
    Now check the elements are alphabets or not
    it is true so increment C value (C=1)
itration:1:
    i='1'
    Now check the elements are alphabets or not
    it is not true so don't increment C value (C=1)
At last print the C value which is 1

Extract each and every element
itration:1:
    i='N'
    Now check the elements are number or not
    it is not true so increment C value (C=1)
itration:1:
    i='1'
    Now check the elements are number or not
    it is true so increment C value (C=1)
At last print the C value which is 1
'''
#W.A.P.T find distintic element of array
'''
S=[1,2,2,3]
el=list()
for i in S:
    if i not in el:
        el.append(i)
print(el)
'''

'''
1. Taking the list
2. Takeing the empty list
Extract each and every element
itration:1:
    i=1
    Now Check the 1 is present in the el or not
    it is true so add the element in el([1])
itration:2:
    i=2
    Now Check the 2 is present in the el or not
    it is true so add the element in el([1,2])
itration:3:
    i=2
    Now Check the 2 is present in the el or not
    it is not true so don't add the element in el([1,2])
itration:4:
    i=3
    Now Check the 3 is present in the el or not
    it is true so add the element in el([1,2,3])
At last print the el is [1,2,3] 

'''

#W.A.P.T. find how many digits in a given string
'''
N=input()
C=0
for i in N:
    if i.isdigit():
        C+=1
print(f'The digit is {C}')
'''

'''
1. Taking the string from user('12n@')
2. initializing C=0 by assuming the digits are not present in the string
3. Extracting each and every elements
itration:1:
    i='1'
    now we check the element is digit or not ('1' is digit)
    it true so increment C value (C=1)
itration:2:
    i='2'
    now we check the element is digit or not ('2' is digit)
    it true so increment C value (C=2)
itration:3:
    i='n'
    now we check the element is digit or not ('n' is not digit)
    it not true so don't increment C value (C=2)
itration:4:
    i='@'
    now we check the element is digit or not ('@' is not digit)
    it not true so don't increment C value (C=2)
At last print the C value which is 2
'''

#W.A.P.T. find how many digits in a given string(without using isdigit methos)
'''
N=input()
num='1234567890'
C=0
for i in N:
    if i in num:
        C+=1
print(f'The digit is {C}')
'''
'''
1. Taking the string from user('12n@')
2. Taking the string from programer which is pre define ('1234567890')
3. Initializing C=0 by assuming the digits agre not present in the string
4. Extracting each and every elements
itration:1:
    i='1'
    now we compare '1' with '1234567890'
    it true so increment C value (C=1)
itration:2:
    i='2'
    now we compare '2' with '1234567890'
    it true so increment C value (C=2)
itration:3:
    i='n'
    now we compare 'n' with '1234567890'
    it not true so don't increment C value (C=2)
itration:4:
    i='@'
    now we compare '@' with '1234567890'
    it not true so don't increment C value (C=2)
At last print the C value which is 2
'''


# W.A.P.T. find how many even digits are present in the given string

#1st way
'''
N=input()
C=0
for i in N:
    if i in '02468':
        C+=1
print(f'The even number is {C}')
'''
'''
1. Taking the string from user('12n@')
2. Initializing C=0 by assuming the digits agre not present in the string
3. Extracting each an every elements
itration:1:
    i='1'
    now we compare '1' with '02468'
    it not true so don't increment C value (C=0)
itration:2:
    i='2'
    now we compare '2' with '02468'
    it true so increment C value (C=1)
itration:3:
    i='n'
    now we compare 'n' with '02468'
    it not true so don't increment C value (C=1)
itration:4:
    i='@'
    now we compare '@' with '02468'
    it not true so don't increment C value (C=1)
At last print the C value which is 1
'''

#2nd way
'''
N=input()
C=0
for i in N:
    if i.isdigit():
        if int(i)%2==0:
            C+=1
print(f'The even number is {C}')
'''

'''
1. Taking the string from user('12n@')
2. Initializing C=0 by assuming the digits agre not present in the string
3. Extracting each an every elements
itration:1:
    i='1'
    Now to check the extract element are digit or not
    it is true then we compare '1' with 'int(i)%2==0'
    it not true so don't increment C value (C=0)
itration:2:
    i='2'
    Now to check the extract element are digit or not
    it is true then we compare '2' with 'int(i)%2==0'
    it true so increment C value (C=1)
itration:3:
    i='n'
    Now to check the extract element are digit or not
    it is not true the we not compare 'n' with 'int(i)%2==0'
    it not true so don't increment C value (C=1)
itration:4:
    i='@'
    Now to check the extract element are digit or not
    it is not true the we not we compare '@' with 'int(i)%2==0'
    it not true so don't increment C value (C=1)
At last print the C value which is 1
'''

# W.A.P.T. find the sum of digits present in given string
'''

S=input()
C=0
for i in S:
    if i.isdigit():
        C+=int(i)
print(C)

'''


'''
1. Taking the string from user('143N$')
2. Initializing C=0 by assuming the digits are not present in the string
3. Extracting each an every elements
itration:1:
    i='1'
    Now to check the extract element are digit or not
    it is true the C value can add the i after changing the string to the number (C=0+1=1)
itration:2:
    i='4'
    Now to check the extract element are digit or not
    it is true the C value can add the i after changing the string to the number (C=1+4=5)
itration:3:
    i='3'
    Now to check the extract element are digit or not
    it is true the C value can add the i after changing the string to the number (C=5+3=8)
itration:4:
    i='N'
    Now to check the extract element are digit or not
    it is not true the C value can't add  (C=8)
itration:5:
    i='$'
    Now to check the extract element are digit or not
    it is not true the C value can't add  (C=8)    
At last print the C value which is 8
'''


# W.A.P.T. print how many spacial character in the given string
'''
S=input()
C=0
for i in S:
    if not i.isalnum():
        C+=1
print(C)
'''


'''
1. Taking the string from user('$@N1')
2. Initializing C=0 by assuming the spacial character are not present in the string
3. Extracting each an every elements
itration:1:
    i='$'
    Now to check the extract element are not alphanumaric
    it true so increment C value (C=1)
itration:2:
    i='@'
    Now to check the extract element are not alphanumaric
    it true so increment C value (C=2)
itration:3:
    i='N'
    Now to check the extract element are not alphanumaric
    it not true so don't increment C value (C=2)
itration:4:
    i='1'
    Now to check the extract element are not alphanumaric
    it not true so don't increment C value (C=2)
At last print the C value which is 2
    
'''

# W.A.P.T print sum of numbers in a given list
'''
L=eval(input('Enter the list:'))
C=0
for i in L:
    if type(i)==int:
        C+=i
print(f'the sum of number in a given list is {C}')
'''
'''
1. Taking the list from user([1,2,3,'hello',[10,20]])
2. Initializing C=0 by assuming the list is not present any number and empty list
Extracting each an every elements
itration:1:
    i='1'
    Now it check the type of the elements if it is intizer
    it is true so add the C value with i (C=1)
itration:2:
    i='2'
    Now it check the type of the elements if it is intizer
    it is true so add the C value with i (C=1+2=3)
itration:3:
    i='3'
    Now it check the type of the elements if it is intizer
    it is true so add the C value with i (C=3+3=6)
itration:4:
    i='hello'
    Now it check the type of the elements if it is intizer
    it is not true so don't add the C value with i (C=6)
itration:5:
    i='[10,20]'
    Now it check the type of the elements if it is intizer
    it is not true so don't add the C value with i (C=6)
At last print the C value which is 6
'''

'''
L=eval(input('Enter the list:'))
C=0
for i in L:
    if isinstance(i,int):
        C+=i
print(f'the sum of number in a given list is {C}')
'''

'''
1. Taking the list from user([1,2,3,'hello',[10,20]])
2. Initializing C=0 by assuming the list is not present any number and empty list
Extracting each an every elements
itration:1:
    i='1'
    Now it check the elements is isinstance (element, class)
    it is true so add the C value with i (C=1)
itration:2:
    i='2'
    Now it check the elements is isinstance (element, class)
    it is true so add the C value with i (C=1+2=3)
itration:3:
    i='3'
    Now it check the elements is isinstance (element, class)
    it is true so add the C value with i (C=3+3=6)
itration:4:
    i='hello'
    Now it check the elements is  isinstance (element, class)
    it is not true so don't add the C value with i (C=6)
itration:5:
    i='[10,20]'
    Now it check the elements is isinstance (element, class)
    it is not true so don't add the C value with i (C=6)
At last print the C value which is 6
'''

#W.A.P.T print the frequency of each and every character is a given string

# Using Set and count method
'''
S=input('Enter the String:')
for i in set(S):
    print(i,S.count(i))
'''

'''
1. Taking the string from user 'Nitish'
Extracting each an every elements
itration:1:
    i='N'
    Now it store in set [in set we can't store duplicate element)
    print the i and count the i [N=1]
itration:2:
    i='i'
    Now it store in set [in set we can't store duplicate element)
    print the i and count the i [N=1,i=1]
itration:3:
    i='t'
    Now it store in set [in set we can't store duplicate element)
    print the i and count the i [N=1,i=1,t=1]
itration:4:
    i='i'
    Now it store in set [in set we can't store duplicate element)
    print the i and count the i [N=1,i=2,t=1]
itration:5:
    i='s'
    Now it store in set [in set we can't store duplicate element)
    print the i and count the i [N=1,i=1,t=1,s=1]
itration:6:
    i='h'
    Now it store in set [in set we can't store duplicate element)
    print the i and count the i [N=1,i=1,t=1,s=1,h=1]
'''

# Using Dictonary and Count method
'''
S=input('Enter the String:')
d={}
for i in S:
    d[i]=S.count(i)
print(d)
'''

'''
1. Taking the string from user 'Nitish'
2. Taking the empty dicitonary
Extracting each an every elements
itration:1:
    i='N'
    Now extarct the value using the key and count the key and put the value ({'N':1})
itration:2:
    i='i'
    Now extarct the value using the key and count the key and put the value ({'N':1,'i':1})
itration:3:
    i='t'
    Now extarct the value using the key and count the key and put the value ({'N':1,'i':1,'t':1})
itration:4:
    i='i'
    Now extarct the value using the key and count the key and put the value ({'N':1,'i':2,'t':1})
itration:5:
    i='s'
    Now extarct the value using the key and count the key and put the value ({'N':1,'i':2,'t':1,'s':1})
itration:6:
    i='h'
    Now extarct the value using the key and count the key and put the value ({'N':1,'i':2,'t':1,'s':1,'h':1})
At last print the dictionary d value is {'N':1,'i':2,'t':1,'s':1,'h':1}
'''

# Using Dictonary

'''
S=input('Enter the string:')
d={}
for i in S:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)
'''

'''
1. Taking the string from user 'Niti'
2. Taking the empty dicitonary
Extracting each an every elements
itration:1:
    i='N'
    Now check i is not present in d
    it is true than i is 1 [{'N':1}]
itration:2:
    i='i'
    Now check i is not present in d
    it is true than i is 1 [{'N':1,'i':1}]
itration:3:
    i='t'
    Now check i is not present in d
    it is true than i is 1 [{'N':1,'i':1,'t':1}]
itration:4:
    i='i'
    Now check i is not present in d
    it is not true [{'N':1,'i':1,'t':1}]
    then got else i is present in d
    it is true than add d vallue with 1 [{'N':1,'i':2,'t':1}]
At last print the d value which is {'N':1,'i':2,'t':1}
'''   
