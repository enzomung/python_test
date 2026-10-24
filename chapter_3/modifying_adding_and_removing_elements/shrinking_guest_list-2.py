guest_list = ['Frank', 'Alice', 'Bob', 'Grace',
              'Charlie', 'David', 'Eve', 'Heidi']
print("Sorry! I can only invite two people to dinner.")

while len(guest_list) > 2:
    guest = guest_list.pop()
    print(f"Sorry {guest}, you are not invited to dinner.")

for guest in guest_list:
    print(f"Hello {guest}, you are still invited to dinner.")

del guest_list[0]
del guest_list[0]
print(guest_list)
