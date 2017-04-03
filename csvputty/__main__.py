import click
from . import markup as _markup

"""bootstrap.__main__: executed when bootstrap directory is called as script."""


DEF_TEMPLATE = '{0}\n\
<tr>\n\
    <td>{1}</td>\n\
    <td>{2}</td>\n\
    <td>{3}</td>\n\
    <td>{4}</td>\n\
</tr>'


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
    if temp != DEF_TEMPLATE:
        try:
            with open(temp) as tmp_file:
                temp = tmp_file.read()
        except FileNotFoundError:
            click.echo('No template file found, treating as format string.')
    template_str = temp
    _markup.generate(cols=cols, in_file_path=inpf,
                     template=template_str, out_file_path=outf)


cli.add_command(markup)
