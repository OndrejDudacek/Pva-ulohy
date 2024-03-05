
for i in range(6):
    with open(f"./tets/000{i}_in.txt", "r") as file:
        content = file.read()
        print(content)
        print(i)
        print("")