def full_score(score_card: str) -> int:
    """
    Calculate the full score from a bowling score-card.

    Args:
        score-card: str
        A space-separated string of 10 frames.

    Returns: int
        Representing the score of the game.

    Possible frame scores:
        "X": strike (10 + following 2 rolls, unless 10th frame then 10)
        "i/": spare (10 + following roll, unless 10th frame then 10)
        "ij": open frame (i+j)
        "-": gutter ball(s) (0)

        * where i,j are between 1 and 9 and i+j < 10

    Example input:
        "X X X X X X X X X XXX" - the perfect game, scores 300.
        "X 7/ 9- X -8 8/ - 72 X X81" has a score of 140.

    Note:
        You may assume all score-cards are valid.
        A single frame scoring "-" means two gutter balls were rolled.
        A strike or spare in the 10th frame unlocks a bonus roll, but scores 10 only.
    """
    total_score = -1

    return total_score
