from numberutils import analyzer

if __name__ == '__main__':
    nu = analyzer.NumberAnalyzer()
    print("\nhi!! this program finds a number is even or not. 0 to exit\n")
    while True:
        try:
            num = int(input("Number: "))
            if num == 0:
                break
            if nu.is_even(num) == True:
                print("{} is even".format(num))
            else:
                print("{} is odd".format(num))
        except Exception as e:
            print("enter a valid number. try again...")