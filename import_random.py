import random
print("Random float:",random.random())
print("random integer btwn 1 and 10:",random.randint(1,10))
print("random choice from a list:",random.choice(["apple","banana","cheery"]))

# shuffilng a list

my_list = [1,2,3,4,5]
random.shuffle(my_list)
print(my_list) 

# selecting a sample form a population
population = range(1, 11)
sample = random.sample(population,5)
print("Random sample form populatoin :",sample)