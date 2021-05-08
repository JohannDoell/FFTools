def to_matrix(list_to_convert, n):
    return [list_to_convert[i:i + n] for i in range(0, len(list_to_convert), n)]


def has_duplicates(array):
    set_array = set(array)
    return len(array) != len(set_array)


def too_many_elements(array, max_elements):
    return len(array) > max_elements
