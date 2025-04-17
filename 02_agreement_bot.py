def main():
    # Get user input
    user_input = input("What's your favorite animal ? ")
    
    # Respond the user input in bold italic (using ANSI escape codes)
    print(f"My favorite animal is also \033[1;3m{user_input}\033[0m!")

# Call the main function
if __name__ == "__main__":
    main()