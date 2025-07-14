"""Formatter for 3DM ini files."""

import sys
import argparse
from pathlib import Path
from ini import INI_file


def main():
    """Main function to parse command line arguments and format the ini file."""
    parser = argparse.ArgumentParser(description="Formatter for 3DM ini files")
    parser.add_argument(
        "--filename", type=Path, help="Path to the input 3DM ini file to be formatted."
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Path to the output file where the formatted content will be saved.",
    )
    parser.add_argument(
        "--encoding",
        type=str,
        default="utf-8",
        help="Encoding to use for reading and writing files.",
    )
    # TODO: add arguments for indentation style, line endings, etc.

    args = parser.parse_args()

    if args.filename is None:
        lines = sys.stdin.readlines()
        file_content: INI_file = INI_file(lines)
        file_content.format_content()
        formatted_content: str = str(file_content)
        if args.output is None:
            print(formatted_content)
        else:
            with open(args.output, "w", encoding=args.encoding) as outfile:
                outfile.write(formatted_content)
    else:
        output_file: Path = args.filename if args.output is None else args.output
        with open(args.filename, "r", encoding=args.encoding) as infile:
            lines: list[str] = infile.readlines()
            file_content = INI_file(lines)
            file_content.format_content()
        with open(output_file, "w", encoding=args.encoding) as outfile:
            outfile.write(str(file_content))


if __name__ == "__main__":
    main()
