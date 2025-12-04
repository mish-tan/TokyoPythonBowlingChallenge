"""
    Calculate the full score from a bowling score-card.
"""

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

    frames = score_card.split(' ')

    total_score = 0
    one_roll_before = 0
    two_rolls_before = 0

    # work backwards, maintaining a record of the two rolls following the current roll
    for frame in reversed(frames):
        frame = replace_gutter_balls(frame)

        total_score += calculate_pins(frame)

        if frame == "X":
            total_score += one_roll_before + two_rolls_before

            two_rolls_before = get_roll_value(one_roll_before)
            one_roll_before = get_roll_value(frame[0])
        else:
            if len(frame) == 2 and "/" in frame:
                total_score += one_roll_before

            one_roll_before = get_roll_value(frame[0])
            two_rolls_before = get_roll_value(frame[1], frame[0])

    return total_score


def replace_gutter_balls(frame: str) -> str:
    if frame == "-" or frame == "--":
        return "00"

    if "-" in frame:
        return frame.replace("-", "0")

    return frame


def get_roll_value(roll: str, num_for_spare: int = None) -> int:
    if roll == "X":
        return 10

    if roll == "/":
        return 10 - int(num_for_spare)

    return int(roll)


def calculate_pins(frame: str) -> int:
    if len(frame) > 2:
        return calculate_tenth_frame_pins(frame)

    if frame == "X" or "/" in frame:
        return 10

    return sum(int(char) for char in frame)


def calculate_tenth_frame_pins(frame: str) -> int:
    if frame[1] == "/":
        if (frame[2]) == "X":
            return 20
        return int(frame[2]) + 10

    if frame[2] == "/":
        if (frame[0]) == "X":
            return 20
        return int(frame[0]) + 10

    total = 0
    for char in frame:
        if char == "X":
            total += 10
        else:
            total += int(char)
    return total
