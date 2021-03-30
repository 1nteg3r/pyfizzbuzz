for i in range(1, 101):
    fizzbuzz = i % 15 == 0
    fizz = i % 5 == 0
    buzz = i % 3 == 0
    if fizzbuzz:
        print(f"fizzbuzz {i} ")
    elif fizz:
        print(f"fizz {i}")
    elif buzz:
        print(f"buzz {i}"
