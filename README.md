# Practical Data Science

The files here are hosted at the domain [here](https://nickeubank.github.io/practicaldatascience_book/intro.html).

## Installs

To be able to run (for building — this doesn't cover exercise libraries), install:

```
conda install jupyter-book=1
pip install sphinx_markdown_tables
```

(Jupyter-book has a version 2.0, but it's not feature-complete, so this is all still building off jupyter `1.0.4.post1`)

## Organization

This repo is primarily organized around the "notebooks" directory — which is home to all the instructional readings, three `ids[course number]_specific` directories with things like class schedules, and an `exercises` directory with course exercises.

Note that the contents of the exercises directory are just for local hosting — the MASTER version of all exercises is in a private `solutions_and_quizzes` repo. Email me if you need access for some reason.

How notebooks are built into the site is determined by the `_toc.yml` table-of-contents file.

You can complete ignore `_build` — that's where builds of the site land — and `docs`, which is where they need to be copied for github pages to serve up the actual website. But you shouldn't edit anything there yourself.

## Building Book

- set `cd` to this repo
- run `jupyter-book build .` By default only changed pages. Use `jupyter-book build --all .` to force full build.
- Copy into docs (where github pages looks): `cp -R _build/html/* docs`
- Push to github and it'll update online shortly!
- You can also open `_build/index.html` (just double click!) and it'll open in your browser locally.

For copy-paste ease:

```bash
jupyter-book build --all .; cp -R _build/html/* docs; git add .; git commit; git push
```

## Syntax

Jupyter books basically use Markdown + some extra features for things like note boxes, or danger boxes, etc.
[Cheatsheet here](https://jupyterbook.org/en/stable/reference/cheatsheet.html)

Here's footnotes: <https://jupyterbook.org/en/stable/content/content-blocks.html#footnotes>
Notes and warnings: <https://jupyterbook.org/en/stable/content/content-blocks.html#notes-warnings-and-other-admonitions>
