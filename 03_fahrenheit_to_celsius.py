def main():
    # Prompt the user for a temperature in Fahrenheit
    degrees_fahrenheit = float(input (" \033[1;3m Enter temperature in Fahrenheit  : \033[1;3m "))
    
    # Convert Fahrenheit to Celsius
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0
    


    print(f"Temperature:  {degrees_fahrenheit}F = {degrees_celsius} C")


if __name__ == "__main__":
    main()