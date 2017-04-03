import click
from . import markup as _markup

"""bootstrap.__main__: executed when bootstrap directory is called as script."""


@click.group()
def cli():
    pass


@click.command()
@click.argument('cols', nargs=-1, type=int)
@click.option('-t', '--temp', default=DEF_TEMPLATE,
              help='Template file with format string')
@click.option('-i', '--inpf', help='Input csv file')
@click.option('-o', '--outf', help='Output markup file')
def markup(cols, temp, inpf, outf):
    _markup.generate(cols=cols, csv_file_path=inpf,
                     template=temp, out_file_path=outf)


cli.add_command(markup)
