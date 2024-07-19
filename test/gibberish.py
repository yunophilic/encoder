#!/usr/bin/env python3

import os
import sys
import string

def generate_gibberish_text(length):
    # Generate random bytes
    random_bytes = os.urandom(length)
    
    # Define a pool of readable characters
    readable_chars = string.ascii_letters + string.digits + string.punctuation + ' '
    
    # Map random bytes to readable characters
    gibberish_text = ''.join(readable_chars[b % len(readable_chars)] for b in random_bytes)
    
    return gibberish_text

if __name__ == "__main__":
    length_of_text = int(sys.argv[1])  # Specify the length of gibberish text you want
    gibberish = generate_gibberish_text(length_of_text)
    print(gibberish)

# python3 gibberish.py 69420 | tr -d '\n' > sample/4.txt
