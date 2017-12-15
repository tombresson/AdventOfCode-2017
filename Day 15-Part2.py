
def main():
    a_val = 591
    b_val = 393

    a_factor = 16807
    b_factor = 48271

    divisior = 2147483647

    bitmask = 0xffff

    match_count = 0
    for step in range(0, 5000000):
        multiple_found = False
        while not multiple_found:
            a_val = (a_factor * a_val) % divisior
            multiple_found = (a_val % 4) == 0

        multiple_found = False
        while not multiple_found:
            b_val = (b_factor * b_val) % divisior
            multiple_found = (b_val % 8) == 0

        masked_a = bitmask & a_val
        masked_b = bitmask & b_val

        if masked_a == masked_b:
            match_count += 1

    print(match_count)


if __name__ == "__main__":
    main()