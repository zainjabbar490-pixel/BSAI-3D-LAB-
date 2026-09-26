movies = [
    ("Avatar", 250),
    ("Titanic", 200),
    ("Joker", 55),
    ("Avengers", 356)
]

average = sum(budget for title, budget in movies) / len(movies)

print("Average Budget:", average)

for title, budget in movies:
    if budget > average:
        print(title, budget)

count = sum(budget > average for title, budget in movies)
print("Movies above average:", count)