import argparse
import os


def generate_tex(files, template, output=None):
    output_tex = ""
    with open(template) as f:
        template_str = f.read()
    for f in files:
        txt = template_str % f
        output_tex += txt + "\n"

    if output is None:
        print(output_tex)
    else:
        if os.path.exists(output):
            print("Error: the file %s already exists" % output)
            print(output)
        else:
            with open(output, "w") as f:
                f.write(output_tex)


def parse_arguments():
    """
        Parse command line arguments
    """
    parser = argparse.ArgumentParser(description='Generate tex for a given list of figures/paths')
    parser.add_argument('-f', '--files', required=True, nargs="+", help="Files to include")
    parser.add_argument('-t', '--template', default="templates/IEEE-subfig.tex", help="Template to populate")
    parser.add_argument('-o', '--output', default=None,
                        help="The path to the generated template. It will print the text if no output is specified")
    args = parser.parse_args()

    return args.files, args.template, args.output


def main():
    files, template, output = parse_arguments()
    generate_tex(files, template, output)


if __name__ == '__main__':
    main()
