import csv
import click

"""markup: Module for generating markup from csv files."""


def _prep_template_str(template):
    try:
        template_str = template.read()
        if len(template_str) == 0:
            raise
    except:
        template_str = ('{},' * len(cols)).strip(',') + '\n'
    finally:
        return template_str


def _parse_row(cols, row, func=None):
    if func is not None:
        return func(row[idx], idx)
    return [row[idx] for idx in cols]


def generate(custom_row_parser=None, cols=None, csv_file=None, template_file=None,
             output_file=None):
    try:
        template_str = _prep_template_str(template_file)
        html = ''
        for idx, row in enumerate(csv.reader(csv_file)):
            html += template_str.format(*_parse_row(cols, row, custom_row_parser))
        output_file.write(html)
    except FileNotFoundError:
        click.echo('File not found.')
        return False
