
#Python program that displays Fibonacci sequence

def fibonacci2(n):
    a = 0
    b = 1
    for i in range(0, n):
        # Display the current Fibonacci number.
        print(a)
        temp = a
        a = b
        b = temp + b
    return a

# Directly display the numbers.
fibonacci2(15)
