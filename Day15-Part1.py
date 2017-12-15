





def main():
    a_val = 591
    b_val = 393

    a_factor = 16807
    b_factor = 48271

    divisior = 2147483647

    bitmask = 0xffff

    match_count = 0
    for step in range(0, 40000000):
        a_val = (a_factor * a_val) % divisior
        b_val = (b_factor * b_val) % divisior

        masked_a = bitmask & a_val
        masked_b = bitmask & b_val

        if masked_a == masked_b:
            match_count += 1

    print(match_count)


if __name__ == "__main__":
    main()