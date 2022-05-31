def main():
    userinput = int(input("Enter a number range \n"))
    for i in range(1,userinput+1):
        if i%15 == 0:
            print("Fizzbuzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        elif i>0:
            print(i)
main()
        
