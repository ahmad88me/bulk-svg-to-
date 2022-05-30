import argparse
import os
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPS


def convert_file(src_file, output_format):
    fname = src_file.split(os.sep)[-1]
    base_dir = os.sep.join(src_file.split(os.sep)[:-1])
    fname_base = ".".join(fname.split(".")[:-1])
    dest_file = os.path.join(base_dir, fname_base+".%s" % output_format.lower())
    drawing = svg2rlg(src_file)
    if output_format.lower() == "pdf":
        renderPDF.drawToFile(drawing, dest_file)
    elif output_format.lower() == "eps":
        renderPS.drawToFile(drawing, dest_file)
    else:
        raise Exception("unknown format: %s" % str(output_format))


def parse_arguments():
    """
        Parse command line arguments
    """
    parser = argparse.ArgumentParser(description='Convert SVG files to other formats')
    parser.add_argument('-s', '--svgs', required=True, nargs="+", help="SVG files to be converted")
    parser.add_argument('-f', '--format', required=True, choices=["pdf", "eps"], help="The output format.")
    args = parser.parse_args()

    return args.format, args.svgs


def main():
    output_format, svg_files = parse_arguments()
    for svgf in svg_files:
        convert_file(svgf, output_format)


if __name__ == '__main__':
    main()

