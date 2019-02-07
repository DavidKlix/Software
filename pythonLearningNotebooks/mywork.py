#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 13:53:48 2018

@author: ios
"""

from random import randrange
def random_choice(first, second) :
    choice = randrange(0,2)
    if choice == 0 : return first
    else : return second
    
def heads_or_tails(count):
    result = []
    for i in range(count):
        result.append(random_choice("H","T"))
    return result

# Only execute if we are the top level
if __name__ == "__main__":
    print(heads_or_tails(10))