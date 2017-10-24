#!/usr/bin/env python


def count_bits(num):

    counter = 0
    if not isinstance(num, int) or num < 0:
        print("Unexcepted value of num: {}".format(num))
        return counter

    while num:
        counter += num & 1
        num = num >> 1
    return counter


if __name__ == "__main__":
    print(count_bits(15333333333442434))

