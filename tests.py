from score_card import full_score

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

for test_num, (card, pins) in enumerate(TEST_CARDS.items()):
    try:
        assert full_score(card) == pins
        print(f"Success: {card}")
    except AssertionError as ae:
        print(f"Failed on test {test_num} with card {card}\n{ae}")
        raise
    except Exception:
        print("Unexpected Error")
        raise

    print(f"All {test_num} tests passed.")
