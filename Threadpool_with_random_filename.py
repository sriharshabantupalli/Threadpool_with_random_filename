import concurrent.futures
# This module provides interface for asynchronously executing functions using threads
import random
# This module generates random numbers


# This script generates 5 random file names each consisting of prefix "file_" as i mentioned in filename


# It creates a set called  'used_filenames' to know filename that have already been used
# This function takes  a set  'used_filenames' as input and generates a new random  file name and it also checks
# the file name is already used or not
def generate_random_filename(used_filenames):
    while True:
        filename = f'file_{random.randint(1, 100)}.txt'
        if filename not in used_filenames:
            used_filenames.add(filename)
            return filename

# This function takes a filename as input and generates a random integer and writes the integer to the file
# as string
def worker(filename):
    content = str(random.randint(1, 100))
    with open(filename, 'w') as f:
        f.write(content)

# It creates an empty set,and generates a random generate_random_filename
# it uses the 'executer.map()' method to asynchronous execution using threadpoolexecuter
def main():
    used_filenames = set()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        filenames = [generate_random_filename(used_filenames) for i in range(5)]
        executor.map(worker, filenames)

if __name__ == '__main__':
    main()