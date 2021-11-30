users=['user_0', 'user_1', 'user_2', 'user_3', 'user_4', 'user_5']
ver_users=[]
print(f"Не верефецированые пользователи: {users}")
print(f"Верефецированые пользователи: {ver_users}")
print(f"\t\t\tПроверяем пользователей...")
while users:
    del_users=users.pop()
    ver_users.append(del_users)

print(f"Не верефецированые пользователи: {users}")
print(f"Верефецированые пользователи: {ver_users}")
