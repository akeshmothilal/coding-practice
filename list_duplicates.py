def find_duplicates(lst):
    unique_elements = set()
    duplicates = set()

    for item in lst:
        if item in unique_elements:
            duplicates.add(item)
        else:
            unique_elements.add(item)

    return list(duplicates)

lst = [1, 3, 2, 1, 1]
print("Duplicates are:", find_duplicates(lst))
