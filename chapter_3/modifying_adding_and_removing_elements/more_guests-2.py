guest_list = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
print("I found a bigger dinner table, so I can invite more guests!")
guest_list.insert(0, 'Frank')
guest_list.insert(3, 'Grace')
guest_list.append('Heidi')

for guest in guest_list:
    print(f"Hello {guest}, you are invited to the dinner party.")
