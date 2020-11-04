def is_prime(num):
    if num > 1:
            if (num % 2) == 0:
             print("No, the number isn't prime.\n")
            else:
             print("Yes, the number is prime.\n")
    else:
        print("No, the number isn't prime.\n")
    show_menu()
    return num

def is_palindrome():
     word = input("Enter the word you want to check\n")
     if word == word[::-1]:
       print("Yes")
       show_menu()
     else:
       print("No")
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