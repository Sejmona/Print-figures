
def print_shape(choice, size):
    if choice == 'a':
        for i in range(size):
            for j in range(size):
                if i >= j:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
    elif choice == 'b':
        for i in range(size):
            for j in range(size):
                if i <= j:
                    print('*', end='')
                else:
                    print(' ', end='')
            print() 
    elif choice == 'c':
        for i in range(size):
            for j in range(size):
                if i + j >= size - 1:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
    elif choice == 'd':
        for i in range(size):
            for j in range(size):
                if i + j <= size - 1:
                    print('*', end='')
                else:
                    print(' ', end='')
    else:
        print("Invalid choice")

def main():
    while True:
        print("Choose a shape to print (a-j) or 'q' to quit:")
        choice = input().strip().lower()
        if choice == 'q':
            break
        size = int(input("Enter the size of the shape: ").strip())
        print_shape(choice, size)
        print()

if __name__ == "__main__":
    main()

