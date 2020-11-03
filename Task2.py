def show_menu():
    print("Choose Operation:\n[1] Check if prime         [2] Check palindrome\n[99] Exit")
    X = int(input())
    if X == 1:
        print("Enter the number")
        is_prime(int(input()))
    elif X == 2:
        print("Enter the word you want to check")
        is_palindrome(input())
    elif X == 99 :
        print("thanks")
    else:
        print("Invalid choice, please try again.\n")
        show_menu()
    return

def is_prime(num):
    if num > 1:
            if (num % 2) == 0:
             print("No, the number isn't prime.")
            else:
             print("Yes, the number is prime.")
    else:
        print("No, the number isn't prime.\n")
    show_menu()
    return num

print("Welcome!")
show_menu()