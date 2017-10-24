#!/usr/bin/env python


def count_bits(num):
    counter = 0
    while num:
        counter += num & 1
        num = num >> 1
    return counter


if __name__ == "__main__":
    print(count_bits(15333333333442434))
    count = 0
    for i in list(bin(15333333333442434)):
        try:
            if int(i) == 1:
                count += 1
        except:
            continue
    print(count)
