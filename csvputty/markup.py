import csv

"""markup: Module for generating markup from csv files."""


DEF_TEMPLATE = '\
<tr>\n\
    <td>{0}</td>\n\
    <td>{1}</td>\n\
    <td>{2}</td>\n\
    <td>{3}</td>\n\
</tr>'


def _parse_row(cols, row, func=None):
    if func is not None:
        return func(row[idx], idx)
    return [row[idx] for idx in cols]


def generate(custom_row_parser=None, cols=None, csv_file_path=None, template=DEF_TEMPLATE,
             out_file_path=None):
    if template != DEF_TEMPLATE:
        try:
            with open(template) as tmp_file:
                template = tmp_file.read()
        except FileNotFoundError:
            click.echo('No template file found, treating as format string.')
    template_str = template
    html = ''
    for idx, row in enumerate(csv.reader(open(in_file_path, 'r'))):
        html += template_str.format(*_parse_row(cols, row, func))
    if out_file_path is None:
        print(html)
    else:
        with open(out_file_path, "w") as out_file:
            out_file.write(html)
