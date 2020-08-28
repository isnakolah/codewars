def row_sum_odd_numbers(n):
    odd_numbers = [[-1]]

    for i in range(n):
        odd = [odd_numbers[-1][-1]+2]
        for j in range(i):
            odd.append(odd[-1]+2)

        odd_numbers.append(odd)

    return sum(odd_numbers[n])

    # return n ** 3


if __name__ == "__main__":
    print(row_sum_odd_numbers(7))
