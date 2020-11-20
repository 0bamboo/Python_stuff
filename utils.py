def find_max(tab):
    _max = tab[0]
    for item in tab:
        if item > _max:
           _max = item
    return _max
