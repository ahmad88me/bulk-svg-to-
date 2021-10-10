import os, sys
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM


def convert_file(src_file):
    fname = src_file.split(os.sep)[-1]
    base_dir = os.sep.join(src_file.split(os.sep)[:-1])
    print
    fname_base = ".".join(fname.split(".")[:-1])
    dest_file = os.path.join(base_dir, fname_base+".pdf")
    # print("dest file: %s" % dest_file)
    drawing = svg2rlg(src_file)
    renderPDF.drawToFile(drawing, dest_file)


if __name__ == '__main__':
    svg_files = sys.argv[1:]
    for sf in svg_files:
        convert_file(sf)
        print("%s is converted successfully" % sf)
