#!/usr/bin/python3
for alphabet_letters in range(97, 123):
    if alphabet_letters == ord('e') or alphabet_letters == ord('q'):
        continue
    print("{:c}".format(alphabet_letters), end="")
