"""
>>> move_tower(2, "A", "C", "B")
"""


def move_tower(height: int, from_pole: str, to_pole: str, with_pole: str) -> None:
    """
    O(2^n)
    """
    if height >= 1:
        # move everything above to the temp pole
        move_tower(height - 1, from_pole, with_pole, to_pole)

        # move the "bottom" disc to final pole
        move_disc(height, from_pole, to_pole)

        # move everything from the temp pole to the final pole
        move_tower(height - 1, with_pole, to_pole, from_pole)


def move_disc(height: int, from_pole: str, to_pole: str) -> None:
    print(f"move disc size {height} from {from_pole} to {to_pole}")
