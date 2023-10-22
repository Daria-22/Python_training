def main():
    n = int(input("Input your integer or alternatively enter 0 to quit"))
    while n != 0:    
        prod = i = 1
        i = 2
        while i <= n:
            prod *= i
            i +=1
        print("Factorial of your number equals " + str(prod)+".")
        n = int(input("Enter 0 to quit"))
    print("Bye for now!")
        
main()
