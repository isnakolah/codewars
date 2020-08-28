# def find_outlier(integers):
#     odd, even = [0, 0]
#     for i in range(len(integers)):
#         if integers[i] % 2 == 0:
#             even += 1
#         else:
#             odd += 1

#     if odd > even:
#         for i in range(len(integers)):
#             if integers[i] % 2 == 0:
#                 return integers[i]
#     else:
#         for i in range(len(integers)):
#             if integers[i] % 2 != 0:
#                 return integers[i]

# def find_outlier(integers):
#     parity = [n % 2 for n in integers]
#     return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]

def find_outlier(integers):
    odd = [x for x in integers if x % 2 != 0]
    even = [x for x in integers if x % 2 == 0]
    return odd[0] if len(even) > len(odd) else even[0]


if __name__ == "__main__":
    print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
