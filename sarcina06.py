def find_min_max(values):
    """
    Print the minimum and maximum of a list
    """

    # Eroare era in faptul ca valorile min si max erau None, dar trebuie sa
    # fie o valoare oarecare din lista de valori, pentru a putea face comparatia
    # cu restul valorilor din lista
    min_value = values[0]
    max_value = values[0]

    for value in values:
        if value > max_value:
            max_value = value
        if value < min_value:
            min_value = value

    print("Minimum value from list: {0}".format(min_value))
    print("Maximum value from list: {0}".format(max_value))
    return min_value, max_value


values = [45, 3, 56, 123, 433, -45, -123, 23, 566]
min_max_values = find_min_max(values)
