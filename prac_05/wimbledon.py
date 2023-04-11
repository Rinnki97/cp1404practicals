"""
CP1404/CP5632 Practical
Wimbledon

Estimate: 30 minutes
Actual:   24 minutes

"""

FILENAME = "wimbledon.csv"


def main():
    """ """
    data = get_data(FILENAME)
    champions = get_champions(data)
    countries = list(get_countries(data))
    countries.sort()

    print("Wimbledon Champions: ")
    for champions, count in champions.items():
        print(f"{champions} {count}")
    print()
    print(f"These are {len(countries)} countries have won Wimbledon: ")
    print(",".join(countries))


def get_data(filename):
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            row = line.strip().split(',')
            data.append(row)
    return data


def get_champions(data):
    champions = {}
    for row in data:
        champion = row[2]
        if champion in champions:
            champions[champion] += 1
        else:
            champions[champion] = 1
    return champions


def get_countries(data):
    countries = set()
    for row in data:
        countries.add(row[1])
    return countries


main()
