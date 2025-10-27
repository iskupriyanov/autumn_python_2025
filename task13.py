# В восточном календаре принят 60-летний цикл, состоящий из 12- летних подциклов,
# обозначаемых названиями цвета: зеленый, красный, желтый, белый и черный.
# В каждом подцикле годы носят названия животных: крысы, коровы, тигра, зайца, дракона,
# змеи, лошади, овцы, обезьяны, курицы, собаки и свиньи. По номеру года вывести его название,
# если 1984 год был началом цикла — годом зеленой крысы.

animals = [
    "monkey",
    "cock",
    "dog",
    "pig",
    "rat",
    "bull",
    "tiger",
    "rabbit",
    "dragon",
    "snake",
    "horse",
    "goat",
]

year = int(input("Enter year: "))
match year % 10:
    case 0 | 1:
        color_year = "white"
    case 2 | 3:
        color_year = "black"
    case 4 | 5:
        color_year = "green"
    case 6 | 7:
        color_year = "red"
    case 8 | 9:
        color_year = "yellow"

print(f"{year} is year of {color_year} {animals[year % 12]}")