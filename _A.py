# Finger exercise: Write a program that examines three variables—x, y, and z—and prints the largest odd number among them. If none of them are odd, it should print a message to that effect.

x = 9.1
y = 3.7
z = 4

if x%2 == 0:
        print('X is an even number...')
elif x%2 != 0:
    print('X is an odd number...')
if y%2 == 0:
    print('Y is an even number...')
elif y%2 != 0:
    print('Y is an odd number...')
if z%2 == 0:
    print('Z is an even number...')
elif z%2 != 0:
    print('Z is an odd number...')