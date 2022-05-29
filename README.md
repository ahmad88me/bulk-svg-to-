# bulk-svg-to
Convert a set of svg files into eps or pdf.

## Convert SVG to another format
### How to use
```
python svg_to.py -f FORMAT -s SVG_FILES

usage: svg_to.py [-h] -s SVGS [SVGS ...] -f {pdf,eps}

```

### Example
`python svg_to.py -f eps -s file1.svg file2.svg file3.svg`

## Generate tex for your figures
```
usage: tex_fig_inc.py [-h] -f FILES [FILES ...] [-t TEMPLATE] [-o OUTPUT]
```
### Example
```
python tex_fig_inc.py -f /data/*to-be-included*.svg -t templates/IEEE-subfig.tex
```