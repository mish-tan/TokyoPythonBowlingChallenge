from functools import partial

from data_for_tests import TEST_CARDS
from score_card import full_score


def in_colour(text: str, colour: int) -> str:
    return f"\033[{colour}m{text}\033[0m"


in_green = partial(in_colour, colour=32)
in_red = partial(in_colour, colour=31)


def run_tests(func_to_test):
    passed_tests = 0
    for test_num, (card, pins) in enumerate(TEST_CARDS.items(), start=passed_tests + 1):
        try:
            returned = func_to_test(card)
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


if __name__ == "__main__":
    run_tests(full_score)
