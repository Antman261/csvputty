# csvputty

A set of command line interfaces and python modules for easily manipulating, transforming and dealing with csv files quickly and effectively.

## CLI Usage

All csvputty commands start with `csvputty` and then the command you wish to perform.

For example:

`$ csvputty markdown 0 1 3 -t template.html -i data.csv -o rendered.html`

The above command will render a new html file using `template.html` as a format string for each row of `data.csv` and the columns with index 0, 1, and 3 for format string indices 0 1 2.

In the above example, `template.html` could be the following:

```html
<div class="row">
  <div class="col-sm-4">{}</div>
  <div class="col-sm-4">{}</div>
  <div class="col-sm-4">{}</div>
</div>
```

## Package Usage

Importing csvputty into your project allows you to use some features unavailable via the command line interface.

For example:

```python
import csvputty

def parse_row(row, row_index):
    for idx, col in enumerate(row):
        row[idx] = col.strip().replace("&", "&amp;")
    img_url = row[2].lower().replace(" ", "_").replace('&amp;', 'and')
    insta_url = row[4].replace("@", "")

    return (img_url, row[1], insta_url, row[3], row[6])


csvputty.markup.generate(custom_row_parser=parse_row, csv_file_path='data.csv',
                         template='template.html', out_file_path='rendered.html')
```

The above example allows me to strip whitespace and replace ampersands with html entities on all columns, and perform further processing on other columns.

The template could also be a format string itself, rather than a path to a file. Csvputty will look for a file first, and if it can't find one it will treat the parameter itself as a template string. (This may be re-implemented in 0.2.0)
