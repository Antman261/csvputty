# csvputty

_Command-fu with csv files_

A set of command line interfaces and python modules for easily manipulating, transforming and dealing with csv files quickly and effectively.

## CLI Usage

All csvputty commands start with `csvputty` and then the command you wish to perform.

For example:

`$ csvputty markup 0 1 3 data.csv template.html rendered.html`

The above command will render a new html file using `template.html` as a format string for each row of `data.csv` and the columns with index 0, 1, and 3 for format string indices 0 1 2.

In the above example, `template.html` could be the following:

```html
<div class="row">
  <div class="col-sm-4">{}</div>
  <div class="col-sm-4">{}</div>
  <div class="col-sm-4">{}</div>
</div>
```

However csvputty really becomes useful in the full context of the command line. Take the following example:

`cat data1.csv data2.csv | csvputty markup 0 1 - template.html rendered.html`

This passes `data1.csv` and `data2.csv` through the same template and renders them together in a single file.

`csvputty markup 0 1 data.csv - -`

This opens stdin allowing you to enter the template via command line and prints the results to stdout.


## Package Usage

Importing csvputty into your project allows you to use some features unavailable via the command line interface.

For example:

```python
import csvputty

input = open('data.csv', 'r')
out = open('rendered.html', 'w')
template = open('template.html', 'r')

def parse_row(row, row_index):
    for idx, col in enumerate(row):
        row[idx] = col.strip().replace("&", "&amp;")
    img_url = row[2].lower().replace(" ", "_").replace('&amp;', 'and')
    insta_url = row[4].replace("@", "")

    return (img_url, row[1], insta_url, row[3], row[6])


csvputty.markup.generate(custom_row_parser=parse_row, csv_file='data.csv',
                         template_file='template.html', out_file='rendered.html')
```

The above example allows me to strip whitespace and replace ampersands with html entities on all columns, and perform further processing on other columns.
