
print('enter the string:')
str = input()

def string_alternative():
    b=[]

    for i in range(len(str)):
        if (i%2==0):
            x = str[i]
            b.append(x)
    y = ''.join(b)
    print(y)






string_alternative()
