# return masked string
def maskify(cc):
    card = [i for i in cc]
    if len(card) > 4:
        return ''.join(['#' for i in card[:-4]]) + ''.join(card[-4:])
    else:
        return cc


if __name__ == "__main__":
    print(maskify("4556364607935616"))
