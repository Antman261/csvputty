import click
from . import markup as _markup
from . import diff as _diff

"""bootstrap.__main__: executed when bootstrap directory is called as script."""


@click.group()
def cli():
    pass


@click.command()
@click.argument('cols', nargs=-1, type=int)
@click.argument('csv', nargs=1, type=click.File('r'))
@click.argument('template', nargs=1, type=click.File('r'))
@click.argument('output', nargs=1, type=click.File('w'))
def markup(cols, csv, template, output):
    """
    Mark up data from a CSV file by parsing select columns through a template.

    Passing - to CSV, TEMPLATE, or OUTPUT will read/write stdin/stdout
    """
    _markup.generate(cols=cols, csv_file=csv,
                     template_file=template, output_file=output)


@click.command()
@click.argument('inputcsv', nargs=1, type=click.File('r'))
@click.argument('diffcsv', nargs=1, type=click.File('r'))
@click.argument('output', nargs=1, type=click.File('w'))
@click.option('-d', '--diff-type',
              help='Type of diff operation, choose from subtract, &, |',
              default='subtract')
@click.option('-sc', '--source-col', help='Source comparison column(s)', default=0)
@click.option('-dc', '--diff-col', help='Diff comparison column(s)', default=0)
def diff(inputcsv, diffcsv, output, diff_type, source_col, diff_col):
    """
    Compare the input CSV against a difference file,
    outputting rows matching the condition.

    Passing - to INPUTCSV, DIFFCSV, or OUTPUT will read/write stdin/stdout
    """
    _diff.run(input_csv=inputcsv, out_file=output, diff_file=diffcsv,
              diff_type=diff_type, source_col=source_col, diff_col=diff_col)


cli.add_command(markup)
cli.add_command(diff)
