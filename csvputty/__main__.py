import click
from . import markup as _markup
from . import diff as _diff
from . import rm as _rm


@click.group()
@click.option('-i', '--input', nargs=1, type=click.File('r'), default='-',
              help='FILEPATH: Leave blank to use stdin.')
@click.option('-o', '--output', nargs=1, type=click.File('w'), default='-',
              help='FILEPATH: Leave blank to use stdout.')
@click.pass_context
def cli(ctx, input, output):
    ctx.obj = {'inputcsv': input, 'out': output}


@click.command()
@click.argument('cols', nargs=-1, type=int)
@click.argument('template', nargs=1, type=click.File('r'))
@click.option('-h', '--header', default=False, is_flag=True,
              help='Flag: Treat the first row of a csv as a header. \
              Use column names as template keys. \
              Negates the need to list column indices.')
@click.pass_context
def markup(ctx, cols, template, header):
    """
    Mark up data from a CSV file by passing select columns through a template.

    Passing - to CSV, TEMPLATE, or OUTPUT will read/write stdin/stdout.
    """
    _markup.generate(cols=cols, csv_file=ctx.obj['inputcsv'], use_dict_reader=header,
                     template_file=template, output_file=ctx.obj['out'])


@click.command()
@click.argument('diffcsv', nargs=1, type=click.File('r'))
@click.option('-d', '--diff-type', default='subtract',
              help='Type of diff operation, choose from subtract, &, |')
@click.option('-sc', '--source-col', help='Source comparison column(s)', default=0)
@click.option('-dc', '--diff-col', help='Diff comparison column(s)', default=0)
@click.pass_context
def diff(ctx, diffcsv, diff_type, source_col, diff_col):
    """
    Compare the input CSV against a difference file,
    outputting rows matching the condition.

    Passing - to INPUTCSV, DIFFCSV, or OUTPUT will read/write stdin/stdout.
    """
    _diff.run(input_csv=ctx.obj['inputcsv'], out_file=ctx.obj['out'], diff_file=diffcsv,
              diff_type=diff_type, source_col=source_col, diff_col=diff_col)


@click.group()
def rm():
    """Remove columns or rows."""
    pass


@click.command()
@click.argument('cols', nargs=-1, type=int)
@click.option('-r', '--range', nargs=2, type=int)
@click.pass_context
def column(ctx, cols, range):
    """Remove selected columns and/or range of columns by index position."""
    _rm.remove_columns(ctx.obj['inputcsv'], ctx.obj['out'], cols, range)


@click.command()
@click.argument('rows', nargs=-1, type=int)
@click.option('-r', '--range', nargs=2, type=int)
@click.pass_context
def row(ctx, rows, range):
    """Remove selected rows and/or range of rows by index position."""
    _rm.remove_rows(ctx.obj['inputcsv'], ctx.obj['out'], rows, range)


@click.group()
@click.option('-h', '--header', default=False, is_flag=True,
              help='Flag: Treat the first row of a csv as a header. \
              Header row is automatically included in view')
@click.pass_context
def spy(ctx, header):
    """View a subset of columns/rows."""
    ctx.obj['header'] = header


@click.command()
@click.argument('cols', nargs=-1, type=int)
@click.option('-r', '--col-range', nargs=2, type=int)
@click.pass_context
def column(ctx, cols, col_range):
    """View selected columns and/or range of columns by index position."""
    _rm.view_columns(ctx.obj['inputcsv'], ctx.obj['out'], cols, col_range)


@click.command()
@click.argument('rows', nargs=-1, type=int)
@click.option('-r', '--row-range', nargs=2, type=int)
@click.pass_context
def row(ctx, rows, row_range):
    """View selected rows and/or range of rows by index position."""
    _rm.view_rows(ctx.obj['inputcsv'], ctx.obj['out'], rows, row_range)


rm.add_command(column)
rm.add_command(row)
spy.add_command(column)
spy.add_command(row)
cli.add_command(rm)
cli.add_command(markup)
cli.add_command(diff)
cli.add_command(spy)
