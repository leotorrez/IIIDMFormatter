"""Formatter for 3DM ini files."""

import sys
import argparse
from pathlib import Path


def format_file(lines: list[str]) -> str:
    def format_line(line):
        stripped = line.strip()
        if stripped.startswith(";"):
            return stripped  # Keep comments as they are
        stripped = stripped.replace("=", " = ")
        stripped = stripped.replace("  ", " ")
        stripped = stripped.replace("= =", "==")
        stripped = stripped.replace("! =", "!=")
        return stripped

    def format_section(lines):
        formatted = []
        indent = 0
        for line in lines:
            formatted_line = format_line(line)
            if formatted_line.startswith("if "):
                formatted.append("    " * indent + formatted_line)
                indent += 1
            elif formatted_line.startswith("else") or formatted_line.startswith("elif"):
                sub1_indent = max(indent - 1, 0)
                formatted.append("    " * sub1_indent + formatted_line)
            elif formatted_line == "endif":
                indent = max(indent - 1, 0)
                formatted.append("    " * indent + formatted_line)
            else:
                formatted.append("    " * indent + formatted_line)
        return formatted

    sections = []
    current_section = []
    for line in lines:
        if line.strip() == "":
            continue  # Skip empty lines
        if line.strip().startswith("[") and current_section:
            sections.append(current_section)
            current_section = [line]
        else:
            current_section.append(line)
    if current_section:
        sections.append(current_section)

    formatted_sections = []
    for section in sections:
        header = section[0]
        body = section[1:]
        formatted_body = format_section(body)
        formatted_sections.append([header.rstrip()] + formatted_body)

    formatted_content = (
        "\n\n".join("\n".join(sec).rstrip() for sec in formatted_sections) + "\n"
    )

    return formatted_content


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

    args = parser.parse_args()

    if args.filename is None:
        lines = sys.stdin.readlines()
    else:
        with open(args.filename, "r", encoding="utf-8") as file:
            lines = file.readlines()

    formatted_content = format_file(lines)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as output_file:
            output_file.write(formatted_content)
    else:
        print(formatted_content)


if __name__ == "__main__":
    main()
