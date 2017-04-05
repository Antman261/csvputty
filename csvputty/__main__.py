import click
from . import markup as _markup
from . import diff as _diff

"""bootstrap.__main__: executed when bootstrap directory is called as script."""


@click.group()
def cli():
    pass


@click.command()
@click.argument('cols', nargs=-1, type=int)
@click.option('-t', '--temp', help='Template with format string', type=click.File('rb'))
@click.option('-i', '--inpf', help='Input csv file', type=click.File('rb'))
@click.option('-o', '--outf', help='Output markup file', type=click.File('wb'))
def markup(cols, temp, inpf, outf):
    _markup.generate(cols=cols, csv_file_path=inpf,
                     template=temp, out_file_path=outf)


@click.command()
@click.option('-i', '--inpf', help='Input csv file', type=click.File('rb'))
@click.option('-o', '--outf', help='Output csv file')
@click.option('-d', '--difff', help='Difference against csv file')
@click.option('-dt', '--diff-type',
              help='Type of diff operation, choose from subtract, &, |',
              default='subtract')
@click.option('-sc', '--source-col', help='Source comparison column(s)')
@click.option('-dc', '--diff-col', help='Diff comparison column(s)')
def diff(inpf, outf, difff, diff_type, source_col, diff_col):
    _diff.run(input_file_path=inpf, out_file_path=outf, diff_file_path=difff,
              diff_type=diff_type, source_col=source_col, diff_col=diff_col)


cli.add_command(markup)
cli.add_command(diff)
