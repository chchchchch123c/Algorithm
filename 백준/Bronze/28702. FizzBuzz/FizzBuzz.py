for i in range(3, 0, -1):
    String = input()
    if String not in ['FizzBuzz', 'Fizz', 'Buzz']:
        num = int(String) + i
if (num % 3 == 0 and num % 5 == 0):
    print('FizzBuzz')
elif (num % 3 == 0):
    print('Fizz')
elif (num % 5 == 0):
    print('Buzz')
else:
    print(num)