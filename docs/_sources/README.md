# Practical Data Science

The files here are hosted at the domain [here](https://nickeubank.github.io/practicaldatascience_book/intro.html).

## Building Book

- set `cd` to this repo
- run `jupyter-book build .` By default only changed pages. Use `jupyter-book build --all .` to force full build.
- Copy into docs (where github pages looks): `cp -R _build/html/* docs`
- Push to github and it'll update online shortly!
- You can also open `_build/index.html` (just double click!) and it'll open in your browser locally.

For copy-paste ease: `jupyter-book build --all .; cp -R _build/html/* docs; git add .; git commit; git push`

## Syntax

Jupyter books basically use Markdown + some extra features for things like note boxes, or danger boxes, etc.
[Cheatsheet here](https://jupyterbook.org/en/stable/reference/cheatsheet.html)

Here's footnotes: <https://jupyterbook.org/en/stable/content/content-blocks.html#footnotes>
Notes and warnings: <https://jupyterbook.org/en/stable/content/content-blocks.html#notes-warnings-and-other-admonitions>
