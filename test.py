def check(number):
    if number %3 == 0 and number %5 != 0:
        print("Fizz")
    elif number %3 != 0 and number %5 ==0:
        print("Buzz")
    elif number %3 == 0 and number %5 == 0:
        print("FizzBuzz")
    else:
        print(number)

N = int(input("数字を入力してください:"))

check(N)
