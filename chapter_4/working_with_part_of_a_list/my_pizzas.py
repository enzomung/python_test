my_pizzas = ['pepperoni', 'hawaiian', 'veggie']  # cheese chicken
friend_pizzas = my_pizzas[:]

my_pizzas.append('cheese')
friend_pizzas.append('chincken')

print("My favorite pizzas are: ")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)
