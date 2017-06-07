import csv
import click
from string import Formatter

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


def _parse_row(cols, row, row_index, func=None):
    if func is not None:
        return func(row, row_index)
    if isinstance(row, list):
        return [row[idx] for idx in cols]
    if isinstance(row, dict):
        return {key: row[key] for idx, key in enumerate(row.keys()) if key in cols}


def generate(custom_row_parser=None, cols=None, csv_file=None, template_file=None,
             output_file=None, use_dict_reader=False):
    template_str = _prep_template_str(template_file)
    html = ''
    try:
        if use_dict_reader:
            reader = csv.DictReader(csv_file)
            cols = [i[1] for i in Formatter().parse(template_str)]
        else:
            reader = csv.reader(csv_file)
        for idx, row in enumerate(reader):
            parsed = _parse_row(cols, row, idx, custom_row_parser)
            try:
                html += template_str.format(*parsed)
            except KeyError:
                html += template_str.format(**parsed)
        output_file.write(html)
    except FileNotFoundError:
        click.echo('FileNotFoundError: File not found.')
        return False
    except KeyError as err:
        click.echo('KeyError: Template key %s not found in %s' % (err, csv_file.name))
