user_data = [
    ("Alice", 30, "Roma"),
    ("Bob", 25, "Milano", "IT"),
    ("Charlie", 35, "Napoli"),
]


def print_user_info(users):
    for record in users:
        if len(record) == 3:
            name, age, city = record
            print(f"Complete user: {name}, {age} y.o., from {city}.")
        elif len(record) > 3:
            name, age, city, *extra = record
            print(f"User with extra: {name}, {age} y.o., from {city}. Extra: {extra}.")


print_user_info(user_data)
