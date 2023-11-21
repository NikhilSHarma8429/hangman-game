import random
def isNumber(a):
    if(a == '1' or a == '2' or a == '3' or a == '4' or a == '5' or a == '6' or a == '7' or a == '8' or a == '9' or a == '0'):
        return True
    else:
        return False
a={
    'mango': 'fruit',
    'guava': 'fruit',
    'cricket': 'sports'
}
a,b=random.choice(list(a.items()))
print('Guess The word')
print('Hint : ' + b)
count = len(a)
temp = count
words = {}
print('No of Attempts: ', count)
temp_str = ''
for j in range(len(a)):
    temp_str = temp_str + '_'
for i in range(count):
    while(1):
        print('Enter Your ',i+1, 'Attempt')
        user = input()
        if(user in words):
            print('Enter a Unique word which you did not inserted before ')
        elif(len(user) > 1):
            print('Enter only a Single Alphabet')
        elif(isNumber((user[0]))):
            print('Enter Aplhabets only')
        else:
            words[user] = 1
            break
    
    str = ''
    for j in range(len(a)):
        if(temp_str[j] == '_' and a[j] == user):
            str += user
            temp = temp -1
        elif(temp_str[j] != '_'):
            str += temp_str[j]
        else:
            str += '_'
    temp_str = str
    print(temp_str)
    if(temp == 0):
        break
if(temp == 0):
    print('You Guessed The Word!!')
else:
    print('You Were Not Able to Guess The Word!!')