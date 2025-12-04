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

    # what if the last roll is a spare?
    "X 7/ 9- X -8 8/ - 72 X X8/": 141,

    # what if the last frame contains a spare? 
    "X 7/ 9- X -8 8/ - 72 X 8/1": 124,
}
