import csv
import click
from collections import OrderedDict


def _validate_parameters(col, header):
    is_valid = True
    has_col = True if col > -1 else False
    has_header = True if (isinstance(header, str) and len(header) > 0) else False
    if (has_header and has_col) or (has_header is False and has_col is False):
        is_valid = False
    mode = 'header' if (has_header and has_col is False) else 'col'
    return is_valid, mode


def _setup_header(row, col_key):
    if isinstance(col_key, str):
        for idx, item in enumerate(row):
            if item == col_key:
                col_key = idx
                break
    return row, col_key


def _parse_rows(reader, col_key):
    split_csvs = {}
    header_row = ''
    for idx, row in enumerate(reader):
        if idx == 0:
            header_row, col_key = _setup_header(row, col_key)
            continue
        row_split_value = row[col_key]
        try:
            split_csvs[row_split_value].append(row)
        except KeyError:
            split_csvs[row_split_value] = [header_row, row, ]
    return split_csvs


def run(input_csv=None, col=False, header=False):
    is_valid, mode = _validate_parameters(col, header)
    if is_valid is False:
        click.echo('Split requires one of -h --header or -c --col')
        return False
    col_key = header if mode == 'header' else col
    reader = csv.reader(input_csv)
    split_csvs = _parse_rows(reader, col_key)
    filename = input_csv.name.rsplit('.', maxsplit=1)[0]
    for key, value in split_csvs.items():
        outpath = filename + '-' + key + '.csv'
        with open(outpath, 'w') as f:
            writer = csv.writer(f)
            for row in value:
                writer.writerow(row)
        click.echo('File created: {}\n      # Rows: {:,}'.format(outpath, len(value)))
