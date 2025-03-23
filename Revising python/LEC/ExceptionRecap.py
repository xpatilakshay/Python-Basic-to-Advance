def even():
    try:
        n = int(input("Enter a number: "))
        for i in range(1,n+1):
            if i%2 == 0:
                print(i)
    except:
        print("Please dont enter String or text")


def odd():
    try:
        n = int(input("Enter a number: "))
        for i in range(1,n+1):
            if i%2 == 1:
                print(i)
    except:
        print("Please dont enter String or text")


even()
odd()