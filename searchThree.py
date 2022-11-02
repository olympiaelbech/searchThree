import sys

# Given a sorted list 'a' containing a series of even numbers
# followed by a series of odd numbers, return the
# index of the first odd number (or len(a) if there are
# no odd numbers)

def search(a, x):
    lo = 0
    hi = len(a) - 1
    while lo <= hi: # range is non-empty
        mid = (lo + hi) // 2
        if a[mid] % 2 == 0: # even
            lo = mid +1
        else: # off
            hi = mid - 1
    return lo

f = open('words')
words = []
for word in f:
    words.append(word.strip())
s = input('Word to find: ')
print(search(words, s))