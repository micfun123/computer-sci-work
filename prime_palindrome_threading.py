import threading
import time

numbers = []

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for i in range(3, max_divisor, 2):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def find_primes_palindromes(start, end):
    for n in range(start, end):
        if is_prime(n) and is_palindrome(n):
            numbers.append(n)

def main():
    start_time = time.time()
    num_threads = 4  # Adjust the number of threads as needed
    chunk_size = 250000000  # Splitting the range into equal chunks
    threads = []
    for i in range(num_threads):
        start = i * chunk_size
        end = min((i + 1) * chunk_size, 1000000000)
        thread = threading.Thread(target=find_primes_palindromes, args=(start, end))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()


    print("Values: ", numbers)
    print("Total values: ", len(numbers))
    print("Time: ", (time.time() - start_time) / 60)

main()
