
def get_index_suffix(index: int) -> str:
    """
    Returns the proper suffix for an integer.
    """
    if index % 100 in {11, 12, 13}:  # Special case for 11th, 12th, and 13th
        suffix = "th"
    else:
        last_digit = index % 10
        if last_digit == 1:
            suffix = "st"
        elif last_digit == 2:
            suffix = "nd"
        elif last_digit == 3:
            suffix = "rd"
        else:
            suffix = "th"
    return suffix