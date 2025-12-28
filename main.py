from code_structure_extractor import code_structure_of_file, print_symbols
import sys
from markdown_generator import generate_markdown

def main():
    if len(sys.argv) >= 2:
        file_path = sys.argv[1]
        symbols = code_structure_of_file(file_path)
        # print_symbols(symbols)
        generate_markdown(file_path, symbols)


if __name__ == "__main__":
    main()