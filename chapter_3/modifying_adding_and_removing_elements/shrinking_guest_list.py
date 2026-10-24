guest_list = ['Frank', 'Alice', 'Bob', 'Grace',
              'Charlie', 'David', 'Eve', 'Heidi']
print("Sorry! I can only invite two people to dinner.")

guest = guest_list.pop()
print(f"Sorry {guest}, you are not invited to dinner.")

guest = guest_list.pop()
print(f"Sorry {guest}, you are not invited to dinner.")

guest = guest_list.pop()
print(f"Sorry {guest}, you are not invited to dinner.")

guest = guest_list.pop()
print(f"Sorry {guest}, you are not invited to dinner.")

guest = guest_list.pop()
print(f"Sorry {guest}, you are not invited to dinner.")

guest = guest_list.pop()
print(f"Sorry {guest}, you are not invited to dinner.")

print(f"Hello {guest_list[0]}, you are still invited to dinner.")
print(f"Hello {guest_list[1]}, you are still invited to dinner.")

del guest_list[0]
del guest_list[0]
print(guest_list)
