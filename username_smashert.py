#!/usr/bin/env python3



#Generate a list of possible usernames from a person's first and last name. 




import sys
import os.path

if __name__ == '__main__': 
    if len(sys.argv) != 2:
        print(f'usage: {sys.argv[0]} names.txt')
        sys.exit(0)

    if not os.path.exists(sys.argv[1]): 
        print(f'{sys.argv[1]} not found')
        sys.exit(0)

    with open(sys.argv[1]) as f:
        for line in enumerate(f): 

            # Eliminate any characters in the given name that are not alphabets or spaces.
            name = ''.join([c for c in line[1] if  c == ' ' or  c.isalpha()])
            tokens = name.lower().split()

            if len(tokens) < 1: 
                # skip lines which are empty
                continue
            
            # assume tokens[0] is the first name
            fname = tokens[0]

            # remaining elements in tokens[] must be the last name
            lname = ''

            if len(tokens) == 2: 
                # assume traditional first and last name
                # e.g. salman khan
                lname = tokens[-1]

            elif len(tokens) > 2: 
                # assume multi-barrelled surname
                # e.g. mc stan

                # remove the first name
                del tokens[0]

                # combine the multi-barrelled surname
                lname = ''.join([s for s in tokens])

            # create possible usernames
            print(fname + lname)           # salmankhan
            print(lname + fname)           # khansalman
            print(fname + '.' + lname)     # mc.stan
            print(lname + '.' + fname)     # stan.mc
            print(lname + fname[0])        # mcs
            print(fname[0] + lname)        # ksalman
            print(lname[0] + fname)        # smc
            print(fname[0] + '.' + lname)  # j.wick
            print(lname[0] + '.' + fname)  # w.john
            print(fname)                   # stan
            print(lname)                   # khan