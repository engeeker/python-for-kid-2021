import random

num = random.randint(1, 100)   # integer 1-100

a = random.random()  # 0-1 float

choice = (1, 2, 3, 4, 5, 6)

b = random.choice(choice)  # chose one item from sequence

c = random.sample(choice, 3) # chose three items from sequence

num_list = [1,2,3,4,5,6,7,8,9]
random.shuffle(num_list)   # shuffle

print(num_list)