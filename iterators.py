# Iterable / Container vs Iterator vs Generator
# See: http://nvie.com/posts/iterators-vs-generators/

# Let's write a counter -------------------------------------------------------
# This code demonstrates how you write the same thing using
# loops, iterators and generators
# But this is not really how iterators and generators are used

# No Iterator / Generator -----------------------------------------------------
# A simple counter
count1 = 13
for i in range(10):
    count1 += 1

print('Count1', count1)

# Iterator --------------------------------------------------------------------
# A value factory!
# TODO Write code for Counter 2
class Counter2:
    def __init__(self, start):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass

from itertools import islice
# counter can keep counting infinitely in a while loop
# three ways to limit it

# 1
counter2 = Counter2(start=13)
for i in range(10):
    count2 = next(counter2)

print('Count2', count2)

# 2
counter2 = Counter2(start=13)
for i in counter2:
    if i > 23:
        break
    count2 = i

print('Count2', count2)

# 3
counter2 = Counter2(start=13)
limited = islice(counter2, 0, 10)
count2 = list(limited)[-1]
print('Count2', count2)


# Generator -------------------------------------------------------------------
# TODO Write code for counter3
def counter3(start):
    pass

c3 = counter3(13)
for i in range(10):
    count3 = next(c3)

print('Count3', count3)

# -----------------------------------------------------------------------------
# A valid use case of reading large files

import time

# Common functions ------------------------------------------------------------
def count_number_of_lines(lines):
    count = 0
    for line in lines:
        if len(line) > 40:
            count += 1
    return count


# List / Iterables ------------------------------------------------------------
def read_file_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.readlines()


def without_iterators():
    start = time.time()

    sherlock_content = read_file_lines('sherlock.txt')
    print(type(sherlock_content))
    print('# of lines =', count_number_of_lines(sherlock_content))

    sherlock_big_content = read_file_lines('sherlock.big.txt')
    print(type(sherlock_big_content))
    print('# of lines =', count_number_of_lines(sherlock_big_content))

    end = time.time()
    print('Execution time =', end - start)
    print()


# Iterator --------------------------------------------------------------------
# An iterator is an object that defines a __next__(self) method
# TODO Write code for ReadFileLines
class ReadFileLines:
    def __init__(self, file_path):
        # open the file here and store it in file object
        pass

    def __iter__(self):
        '''Should return an iterator object that has the __next__ method'''
        pass

    def __next__(self):
        # get the next line of the file
        pass


def with_iterators():
    start = time.time()
    sherlock_content = ReadFileLines('sherlock.txt')
    print(type(sherlock_content))
    print('# of lines =', count_number_of_lines(sherlock_content))

    sherlock_big_content = ReadFileLines('sherlock.big.txt')
    print(type(sherlock_big_content))
    print('# of lines =', count_number_of_lines(sherlock_big_content))

    end = time.time()
    print('Execution time =', end - start)
    print()


# Generator -------------------------------------------------------------------
# A generator uses 'yield' statement instead of __next__
# TODO Write generator code for file_lines_reader
def file_lines_reader(file_path):
    pass


def with_generators():
    start = time.time()
    sherlock_content = file_lines_reader('sherlock.txt')
    print(type(sherlock_content))
    print('# of lines =', count_number_of_lines(sherlock_content))

    sherlock_big_content = file_lines_reader('sherlock.big.txt')
    print(type(sherlock_big_content))
    print('# of lines =', count_number_of_lines(sherlock_big_content))

    end = time.time()
    print('Execution time =', end - start)
    print()


# TODO Uncomment these one by one ---------------------------------------------
# See memory use (Activity Monitory / Task Manager) and execution time

# without_iterators()
# with_iterators()
# with_generators()
