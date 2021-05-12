def to_matrix(list_to_convert, n):
    """
    Converts a list to an n by n matrix.
    :param list_to_convert: The list to convert.
    :param n: The dimensions of the matrix.
    :return: The converted matrix.
    """
    return [list_to_convert[i:i + n] for i in range(0, len(list_to_convert), n)]


def has_duplicates(list_to_check):
    """
    Checks if a list has any duplicates.
    :param list_to_check: The list to check.
    :return: TRUE if has duplicates, FALSE otherwise.
    """
    set_array = set(list_to_check)
    return len(list_to_check) != len(set_array)


def too_many_elements(list_to_check, max_elements):
    """
    Checks if a list has more elements than max_elements.
    :param list_to_check: The list to check.
    :param max_elements: The number of elements to check.
    :return: TRUE if more elements than max_elements, FALSE otherwise.
    """
    return len(list_to_check) > max_elements
