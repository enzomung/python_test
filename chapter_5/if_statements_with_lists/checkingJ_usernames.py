current_users = ['admin', 'jane', 'john', 'alice', 'bob']
new_users = ['Jane', 'mike', 'alice', 'sarah', 'bob']

current_users_lower = []

for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user} is alrady taken. choose another username.")
    else:
        print(f"{new_user} is available.")
