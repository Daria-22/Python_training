def main():
    user_input = int(input("Please type the number you want to reach for Fibonacci sequence"))
    a = b = 1
    sum = 0
    while a < user_input:
        a, b = a + b, a
        print(a, end = '   ')
        ratio = a/b
        print(f"Ratio between the last two numbers is",ratio)
main()
