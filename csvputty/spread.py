import csv
import click
from collections import OrderedDict


def _parse_rows(reader, cols, header):
    split_columns = []
    header_row = ''
    for idx, row in enumerate(reader):
        if idx == 0:
            header_row = row
            continue
        for index, key in enumerate(cols):
            try:
                col_obj = split_columns[index]
            except IndexError:
                split_columns.append({
                    'header': header_row[key],
                    row[key]: 1,
                    'total_rows': 1
                })
            else:
                try:
                    col_obj[row[key]] += 1
                except KeyError:
                    col_obj[row[key]] = 1
                finally:
                    col_obj['total_rows'] += 1
    return split_columns


def _setup(input_csv, cols, header):
    reader = csv.reader(input_csv)
    return _parse_rows(reader, cols, header)


def count(input_csv=None, cols=False, header=False):
    split_columns = _setup(input_csv, cols, header)


def percent(input_csv=None, cols=False, header=False):
    split_columns = _setup(input_csv, cols, header)
    click.echo('Percentages for %s' % input_csv.name)
    click.echo('-------------------------------------------------------------')
    for item in split_columns:
        click.echo(item['header'])
        for key, value in item.items():
            if key in ['header', 'total_rows']:
                continue
            click.echo('{:.0f}%\t{}'.format(value/item['total_rows']*100, key))
        click.echo('- - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    click.echo('Total rows: %s\n\n' % split_columns[0]['total_rows'])


# [{
#     "Header": "Header name"
#     "Value Name": 12,
#     "Other Value Name": 1
# }]
