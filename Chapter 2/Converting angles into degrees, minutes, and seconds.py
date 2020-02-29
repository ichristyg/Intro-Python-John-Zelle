def angleConvert():
    print("This program converts a angle to degrees, minutes, and seconds")
    print()
    angle = eval(input("Please input angle with decimal points:  "))
    degrees = int(angle)
    x = angle-int(angle)
    minutes = int(x * 60)
    y = (x*60)-int(x*60)
    seconds = str(round(y*60))
    print("The answer is:",degrees,"°",minutes,"'",seconds,"\"")
angleConvert()


