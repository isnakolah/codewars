def nb_year(population, percent, aug, target):
    years = 0
    while population < target:
        population += population * percent/100 + aug
        years += 1
    return years


if __name__ == "__main__":
    print(nb_year(1500000, 2.5, 10000, 2000000))
