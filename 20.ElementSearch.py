a = [1, 2, 3, 4, 5, 5, 6, 6, 7, 8]


def find(ordered_list, element_to_find):
    for element in ordered_list:
        if element == element_to_find:
            return True
    return False
