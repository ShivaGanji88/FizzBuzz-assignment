count = 0
for each_number  in range(1, 101):
    if (each_number % 3 == 0) and (each_number % 5 == 0):
        print("FizzBuzz")

    elif each_number % 3 == 0:
        print("Fizz")

    elif each_number % 5 == 0:
        print("Buzz")        
    else:
        count = each_number
        print(count)