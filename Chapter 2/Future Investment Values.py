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

print()

def main():
    print("This program calculates the total accumulation of your investment")
    print("after investing a fixed amount every year.")
    print()

    payment= eval(input("Enter the annual investment: "))
    apr = eval(input("Enter the annualized interest rate: "))
    years = eval(input("Enter the number of years: "))

    principal = 0.0
    for i in range (years):
        principal = (principal + payment)*(1+apr)

    print("Total accumulation of your investment is: ", principal, "after", years, "years.")


main()


