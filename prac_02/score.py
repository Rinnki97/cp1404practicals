import random


SCORE_MINIMUM = 0
SCORE_MIDDLE = 50
SCORE_HIGH = 90
SCORE_MAXIMUM = 100


def main():
    score = generate_random_score()
    print(f"Random score: {score}")
    print(determine_score(score))


def determine_score(score):
    if SCORE_MINIMUM < score < SCORE_MIDDLE:
        level = "bad"
    elif score < SCORE_HIGH:
        level = "pass"
    elif score < SCORE_MAXIMUM:
        level = "excellent"
    else:
        level = "Invalid"
    return level


def generate_random_score():
    return random.randint(SCORE_MINIMUM, SCORE_MAXIMUM)


main()
