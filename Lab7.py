#x = 1
#
#while (x < 300):
#    print x
#    x = x + 2



#list1 = [0,1,4,5,76,45]
#index = 0
#
#while (index < len(list1)):
#    print list1[index]
#    index = index + 1


import random
rand = random.randint(0,50)
user = -1
tries = 0
print 'please enter a number between 0 and 50'
while (user != rand):
    user = int(raw_input())
    if user < rand:
        print 'higher...'
    if user > rand:
        print 'lower...'
    tries = tries + 1  
print '-----------------'
print 'You got it right!'
print 'and it only took you ' + str(tries) + ' tries!'   