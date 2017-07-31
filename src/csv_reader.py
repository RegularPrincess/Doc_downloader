_MB = 10000000


def _create_map(name_of_columns):
    map_of_columns = {}
    for name in name_of_columns:
        map_of_columns[name] = []
    return map_of_columns


def pars_csv(name):
    file = open(name, "r")
    buff_str = file.read(_MB)
    rows = buff_str.split("\n")
    name_of_columns = rows[0].split(';')
    rows = rows[1:]
    map_col = _create_map(name_of_columns)
    for row in rows:
        cells = row.split(';')
        i = 0
        while i < len(cells):
            map_col[name_of_columns[i]].append(cells[i])
            i = i + 1
    return map_col





