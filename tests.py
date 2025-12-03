from functools import partial
from score_card import full_score


def in_colour(text: str, colour: int) -> str:
    return f"\033[{colour}m{text}\033[0m"


in_green = partial(in_colour, colour=32)
in_red = partial(in_colour, colour=31)


TEST_CARDS = {
    # perfect game
    "X " * 9 + "XXX": 300,
    #
    # all spares with bonus 1
    "5/ " * 9 + "5/5": 150,
    #
    # all spares with bonus 2
    "-/ " + " ".join(f"{i}/" for i in range(1, 10)) + "X": 155,
    #
    # all gutters 1
    " ".join(["-"] * 10): 0,
    #
    # all gutters 2
    " ".join(["--"] * 10): 0,
    #
    # all gutters 3
    " ".join(["-", "--"] * 5): 0,
    #
    # all frames open
    " ".join(map(lambda x: f"{x:02d}", range(90, 0, -9))).replace("0", "-"): 90,
    #
    # getting better
    (" ".join((f"{i}1" for i in range(9))) + " 9/X").replace("0", "-"): 65,
    #
    # example game
    "X 7/ 9- X -8 8/ - 72 X X81": 140,
}


passed_tests = 0
for test_num, (card, pins) in enumerate(TEST_CARDS.items(), start=passed_tests + 1):
    try:
        returned = full_score(card)
        assert returned == pins
        print(f"{test_num:>2} - {in_green('Success')} with card {card}")
        passed_tests += 1
    except AssertionError:
        print(
            f"{test_num:>2} - {in_red('Failed')} on test {test_num} with card {card}\n\tExpected {in_green(pins)} but got {in_red(returned)}"
        )

    except Exception:
        print("Unexpected Error")
        raise

if passed_tests == test_num:
    print(f"\n{in_green(f'{test_num} tests passed')}.")
