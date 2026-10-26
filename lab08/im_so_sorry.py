def print_count_down(n):
    for count in range(n, 0, -1):
        print(count)
    print("BOOM")



print_count_down(10)


def print_count_up(n):
    if n <= 11:
        print("BOOM")
    else:
        print(n)
        print_count_up(n + 1)

print_count_up(0)
