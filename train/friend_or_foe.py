def friend(x):
    friends = [friend for friend in x if len(friend) == 4]
    return friends


if __name__ == "__main__":
    print(friend(["Ryan", "Kieran", "Mark"]))
