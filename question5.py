def print_primes(start, end):
    for num in range(start, end+1):
        if num > 1: # all primes are greater than 1
            for i in range(2, num):
                if (num % i) == 0: # if the modulo is zero then the number can be divided by another number
                    break
            else:
                print(num)

print_primes(2, 100)
