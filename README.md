# Astro tools

## `xisf-strip`

Remove rejection maps from a XISF file and use compression to reduce
its size.

## `rename-filters`

Rename filter names into XISF files.

## `extract-metadata`

Compute total integration time for various filters.

## `find-videos`

Read an HTML file from disk and print video URLs from its `<video>` elements,
including nested `<source>` elements. Relative source values are printed as
they appear in the file. For example:

```sh
python3 src/find-videos.py page.html
```
