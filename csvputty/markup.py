import csv

"""markup: Module for generating markup from csv files."""


def _parse_row(cols, row, func=None):
    if func is not None:
        return [func(row[idx], idx) for idx in cols]
    return [row[idx] for idx in cols]


def generate(func=None, cols=None, in_file_path=None, template=None, out_file_path=None):
    html = ''
    for idx, row in enumerate(csv.reader(open(in_file_path, 'r'))):
        html += template.format(*_parse_row(cols, row, func))
    if out_file_path is None:
        print(html)
    else:
        with open(out_file_path, "w") as out_file:
            out_file.write(html)
