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
