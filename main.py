#import random
#x = random.randint(1,10)
#print(x)

#my_list = [1,2,3]
#random.shuffle(my_list)
#print(my_list)


from random import shuffle as shuffle_my_list
my_list = [1, 2, 3]
shuffle_my_list(my_list)
print(my_list)
