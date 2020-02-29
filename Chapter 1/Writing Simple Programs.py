print("This program converts Celsius to Fahrenheit.")
def main ():
    celsius = eval(input("What is the Celsius tempature?"))
    fahrenheit =9/5 * celsius +32
    print ("The tempature is", fahrenheit, "degrees Fahrenheit.")

main()

def grades():
    print("This program computes the average of three exam scores.")
    score1, score2, score3 = eval(input("Enter three scores separated by a comma: "))
    average = (score1+score2+score3)/3
    print("The average of the scores is: ", average)

grades()

def main ():
    for celsius in range(0, 5):
        celsius = eval(input("What is the Celsius tempature?"))
        fahrenheit =9/5 * celsius +32
        print ("The tempature is", fahrenheit, "degrees Fahrenheit.")

main()

def main():
    print("Celsius  Fahrenheit")
    print("-------------------")
    print(" 0          32.0")
    for celsius in [10,20,30,40,50,60,70,80,90]:
        fahrenheit = 9.0 / 5.0 * celsius + 32
        print(celsius, "        ", fahrenheit)
    print("100         212.0")

main()

def main ():
    print("This program converts Fahrenheit to Celsius ")
    fahrenheit = eval(input("What is the Fahrenheit tempature?"))
    celsius= (fahrenheit - 32) * 5/9
    print ("The tempature is", celsius , "degrees Celsius.")

main()


def main():
    print("This program calculates the future value of an investment.")
    print()

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annualized interest rate: "))
    years = eval(input("Enter the number of years: "))

    for i in range(years):
        principal = principal * (1 + apr)

    print("The amount in", years, "years is:", principal)


main()
