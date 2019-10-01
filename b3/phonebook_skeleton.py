#!/usr/bin/env python

import sys
import os

PHONEBOOK_ENTRIES = "python_phonebook_entries"

def main():
    if len(sys.argv) < 2:
        exit(1)

    elif sys.argv[1] == "new":
        name = sys.argv[2]
        number = sys.argv[3]
        with open(PHONEBOOK_ENTRIES, 'a+') as f:
            f.write(name + ": " + number + "\n")

    elif sys.argv[1] == "list":
        if not os.path.isfile(PHONEBOOK_ENTRIES) or os.path.getsize(
                PHONEBOOK_ENTRIES) == 0:
            print("phonebook is empty")
        else:
            with open(PHONEBOOK_ENTRIES, 'r') as f:
                for line in f.readlines():
                    print line,

    elif sys.argv[1] == "remove":
        name = " ".join(sys.argv[2:])
        with open(PHONEBOOK_ENTRIES, 'r') as f:
            lines = f.readlines()
        with open(PHONEBOOK_ENTRIES, 'w') as f:
            for line in lines:
                entry = line.split(":")
                if entry[0] != name:
                    f.write(line)

    elif sys.argv[1] == "clear":
        with open(PHONEBOOK_ENTRIES, 'w') as f:
            f.close()

    else:
        name = " ".join(sys.argv[1:])
        with open(PHONEBOOK_ENTRIES, 'r') as f:
            for line in f.readlines():
                entry = line.split(":")
                if entry[0] == name:
                    print line,

if __name__ == "__main__":
    main()
