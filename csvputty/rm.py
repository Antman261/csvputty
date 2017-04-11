import csv
import click


def _invert_cols(cols):
    return [i for i in range(NUM_COLS) if i not in cols]


def _invert_range(col_range):
    return [i for i in range(NUM_COLS) if i not in range(*col_range)]


def remove_columns(csv_file=None, output_file=None, cols=None, col_range=(),
                   use_dict_reader=False):
    reader = csv.reader(csv_file)
    writer = csv.writer(output_file)
    new_data = []
    if cols is not None:
        for idx, row in enumerate(reader):
            new_data.append([d for i, d in enumerate(row) if i not in cols])
    if len(col_range) > 0:
        for idx, row in enumerate(reader):
            row[col_range[0]:col_range[1]] = []
            new_data.append(row)
    writer.writerows(new_data)


def view_columns(csv_file=None, output_file=None, cols=None, col_range=(),
                 use_dict_reader=False):
    global NUM_COLS
    reader = csv.reader(csv_file)
    NUM_COLS = len(next(reader))
    if cols is not None:
        cols = _invert_cols(cols)
    if len(col_range) > 0:
        cols = _invert_range(col_range)
    remove_columns(csv_file, output_file, cols, use_dict_reader=use_dict_reader)
