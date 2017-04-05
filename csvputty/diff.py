import csv as csv


"""csvdiff: Module for diffing CSV files."""


def _build_diff_values():
    global DIF_COL_NAME
    for idx, row in enumerate(DIF_CSV):
        if idx > 0:
            DIF_VALUES.append(row[DIF_COL])
        else:
            DIF_COL_NAME = row[DIF_COL]


def _setup_env(**options):
    global SRC_CSV, DIF_CSV, OUT_CSV, SRC_COL, DIF_COL, DIF_VALUES, DIF_COL_NAME

    SRC_CSV = csv.reader(open(options['input_file_path']))
    DIF_CSV = csv.reader(open(options['diff_file_path']))
    OUT_CSV = csv.writer(open(options['out_file_path'], 'w'))
    SRC_COL = options['source_col']
    DIF_COL = options['diff_col']

    DIF_VALUES = []
    DIF_COL_NAME = ''


def _validate_parameters():
    if input_file_path is None:



def run(**options):
    if _validate_parameters(**options) is False:
        return
    _setup_env(**options)
    _build_diff_values()
    for idx, row in enumerate(SRC_CSV):
        if idx == 0:
            print('Comparing columns: {} {} {}'.format(
                row[SRC_COL], options['diff_type'], DIF_COL_NAME
            ))
            OUT_CSV.writerow(row)
            continue
        if check_row(row):
            OUT_CSV.writerow(row)


def check_row(row):
    if options['diff_type'] == 'subtract':
        if row[SRC_COL] in DIF_VALUES:
            return False
        return True
