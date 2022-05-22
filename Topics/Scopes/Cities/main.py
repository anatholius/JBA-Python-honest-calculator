def change_city(new_user_city):
    global user_city
    user_city = new_user_city


user_city = None
change_city("Paris")
print(user_city)
