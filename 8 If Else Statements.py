#================================================
# 8 - Conditional Statements - If-Else Statements
#================================================
a = 10
b = 20
c = 30

print('a --> 10')
print('b --> 20')
print('c --> 30')

#-------------------------------------------------
print("\n--------- If Else Statement ---------\n")

if(a==10):
    print('a = 10')
elif(b==20):
    print('b = 20')
else:
    print('a != 10 & b != 20')

#-------------------------------------------------
print("\n--------- If Else Statement ---------\n")
 
if(a==10):
    print('a = 10')
    if(b==20):
        print('a = 20')
        if(c==30):
            print('a = 30')
