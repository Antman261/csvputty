import csv as csv
import click


"""csvdiff: Module for diffing CSV files."""


def _build_diff_values():
    global DIF_COL_NAME
    for idx, row in enumerate(DIF_CSV):
        if idx > 0:
            DIF_VALUES.append(row[DIF_COL].strip().lower())
        else:
            DIF_COL_NAME = row[DIF_COL]


def _setup_env(**options):
    global SRC_CSV, DIF_CSV, OUT_CSV, SRC_COL, DIF_COL, DIF_VALUES, DIF_COL_NAME, DIF_TYPE

    SRC_CSV = csv.reader(options['input_csv'])
    DIF_CSV = csv.reader(options['diff_file'])
    OUT_CSV = csv.writer(options['out_file'])
    SRC_COL = options['source_col']
    DIF_COL = options['diff_col']
    DIF_TYPE = options['diff_type']

    DIF_VALUES = []
    DIF_COL_NAME = ''


def _validate_parameters(input_csv=None, out_file=None, diff_file=None, diff_type=None,
                         source_col=None, diff_col=None):
    if input_csv is None:
        return False
    if out_file is None:
        return False
    if diff_file is None:
        return False
    if diff_type is None:
        return False
    if source_col is None:
        return False
    if diff_col is None:
        return False
    return True


def run(**options):
    if _validate_parameters(**options) is False:
        return
    _setup_env(**options)
    _build_diff_values()
    for idx, row in enumerate(SRC_CSV):
        if idx == 0:
            click.echo('Comparing columns: {} {} {}'.format(
                row[SRC_COL], DIF_TYPE, DIF_COL_NAME
            ))
            OUT_CSV.writerow(row)
            continue
        if check_row(row):
            OUT_CSV.writerow(row)


def check_row(row):
    if DIF_TYPE == 'subtract':
        if row[SRC_COL].strip().lower() in DIF_VALUES:
            return False
        return True
