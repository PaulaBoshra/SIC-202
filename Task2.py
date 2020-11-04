def is_prime(num):
    if num > 1:
        for i in range (2,num):
            if (num % i) == 0:
                print(num," isn't a prime number.\n")
                break
        else:
            print(num," is a prime number.\n")
    else:
        print(num," isn't a prime number.\n")
    show_menu()
    return num

def is_palindrome():
     word = input("Enter the word you want to check\n")
     if word == word[::-1]:
       print("Yes",word," is palindrome")
       show_menu()
     else:
       print("No",word," isn't palindrome")
       show_menu()
     return()

def show_menu():
    print("Choose Operation:\n[1] Check if prime         [2] Check palindrome\n[99] Exit")
    X = int(input())
    if X != 99:
        if X == 1:
            print("Enter the number")
            is_prime(int(input()))
        elif X == 2:
            is_palindrome()
        else:
            print("Invalid choice, please try again.\n")
            show_menu()
    return()

print("Welcome!")
show_menu()