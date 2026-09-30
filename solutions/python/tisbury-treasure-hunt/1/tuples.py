"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    Parameters:
        record (tuple): A (treasure, coordinate) pair.

    Returns:
        str: The extracted map coordinate.
    """

    return record[1]


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    Parameters:
        coordinate (str): A string map coordinate.

    Returns:
        tuple: The string coordinate split into its individual components.
    """
    c = coordinate
    return (c[0], c[1])



def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    Parameters:
        azara_record (tuple): A (treasure, coordinate) pair.
        rui_record (tuple): A (location, tuple(coordinate_1, coordinate_2), quadrant) trio.

    Returns:
        bool: Do the coordinates match?
    """

    a_coord = convert_coordinate(get_coordinate(azara_record))
    return a_coord == rui_record[1]


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    Parameters:
        azara_record (tuple): A (treasure, coordinate) pair.
        rui_record (tuple): A (location, coordinate, quadrant) trio.

    Returns:
        tuple or str: The combined record (if compatible), or the string "not a match" (if incompatible).
    """

    if compare_records(azara_record, rui_record):
        return (azara_record[0], azara_record[1], rui_record[0], rui_record[1], rui_record[2])
    else:
        return 'not a match'


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    Parameters:
        combined_record_group (tuple): Everything from both participants.

    Returns:
        str: Everything "cleaned", excess coordinates and information are removed.

    Note:
        The return statement is a multi-lined string with items separated by newlines.
        (see HINTS.md for an example).

    """

    results = []
    for c in combined_record_group:
        results.append(f"('{c[0]}', '{c[2]}', {c[3]}, '{c[4]}')\n")

    result = "".join(results)
    return result

input_data = ['2A', '4B', '1C', '6D', '7E', '7F',
                      '6A', '8A', '5B', '8C', '1F', '3D', '4E']
