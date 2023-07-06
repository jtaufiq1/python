#!/usr/bin/python3

num = 10
while num > 0:
    print(f"\tThere are {num} green bottles hanging on the wall.")
    print(f"\t{num} green bottles hanging on the wall.")
    print("\tAnd if 1 green bottle should accidentally fall")
    num = num -1

    answer = int(input("\n\tHow many green bottles will be hanging on the wall? "))

    if answer == num:
        if answer != 0:
            if num == 1:
                b = "bottle"
            else:
                b = "bottles"
            print (f"There will be {num} green {b} hanging on the wall.")
        else:
            print("There are no more green bottles hanging on the wall.")
    else:
        while answer != num:
            answer = int(input("\tNo, Try Again: "))
