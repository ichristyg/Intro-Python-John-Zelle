print("This program converts Celsius to Fahrenheit.")
def main ():
    celsius = eval(input("What is the Celsius tempature?"))
    fahrenheit =9/5 * celsius +32
    print ("The tempature is", fahrenheit, "degrees Fahrenheit.")

main()


print("This program converts 5 inputs of Celsius to Fahrenheit after each input")
def main ():
    for celsius in range(0, 5):
        celsius = eval(input("What is the Celsius tempature?"))
        fahrenheit =9/5 * celsius +32
        print ("The tempature is", fahrenheit, "degrees Fahrenheit.")

main()


print("This program prints a table of Celsius and Fahrenheit equivalents every 10 degrees from 0 to 100 degrees.")
def main():
    print("Celsius  Fahrenheit")
    print("-------------------")
    print(" 0          32.0")
    for celsius in [10,20,30,40,50,60,70,80,90]:
        fahrenheit = 9.0 / 5.0 * celsius + 32
        print(celsius, "        ", fahrenheit)
    print("100         212.0")

main()


print("This program converts Fahrenheit to Celsius.")
def main ():
    print("This program converts Fahrenheit to Celsius ")
    fahrenheit = eval(input("What is the Fahrenheit tempature?"))
    celsius= (fahrenheit - 32) * 5/9
    print ("The tempature is", celsius , "degrees Celsius.")

main()
