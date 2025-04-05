#Multiplication table from 1-10
#This program will print the multiplication table from 1 to 10
#The program will use nested for loops to print the table

def multiplication_table(rows, cols):
    #This line defines the column head
    print("   ", end='')
    for col in range(1, cols + 1):
        print(f'{col:4}', end='')
    
    print("\n" + "-" * (4 *(cols + 1)))

    for row in range(1, rows + 1):
        print(f"{row:2} |", end='')
        for col in range(1, cols + 1):
            print(f"{row * col:4}", end='')
        print()


multiplication_table(10, 10)