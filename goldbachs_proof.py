even_int = 6 #start with first even integer greater than 2 and 4 
prime_numbers = [] #list of all odd prime numbers that are less than current even_int value
success = []

#check to see if largest odd number is a prime number
def is_prime(largest_odd):
    for i in range(2, largest_odd):
        if (largest_odd % i) == 0:
            break
    else:
        prime_numbers.append(largest_odd)

#program will continue to run until Goldbach's Conjecture is proven false
while True:
    largest_odd = even_int - 3
    
    

    for x in range(0, len(prime_numbers)):
        for y in range(x, len(prime_numbers)):
            if prime_numbers[x] + prime_numbers[y] == even_int:
                print(str(even_int) + "=" + str(prime_numbers[x])+"+"+str(prime_numbers[y]))
                success.append(even_int)
                break
    #see whether there was a succesfull proof        
    if len(success) != 0:
        even_int += 2
        success.clear
    else:
        print("proven false at integer: " + str(even_int))
        break