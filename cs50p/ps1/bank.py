# if the argumen start with h output 20 but if it is hello 0 anything else 100

greeting = input('Greeting: ').lower().strip()

if greeting.startswith('hello'):
    print('$0')
elif greeting.startswith('h'):
    print('$20')
else:
    print('$100')
