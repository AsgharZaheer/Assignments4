def main():
    # Prompt the user for a number
    number = float(input("Type a number to see its square: "))
    
    # Calculate the square of the number
    square = number * number
    
    # Print the result
    print(f" \033[1;3m {number} squared is {square} \033[1;3m")

if __name__ == "__main__":
    main()