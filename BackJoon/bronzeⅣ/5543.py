burger = []
for i in range(3):
    burger.append(int(input()))
drink = []
for i in range(2):
    drink.append(int(input()))

set = min(burger) + min(drink) - 50
print(set)
