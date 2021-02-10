"""Main script."""
from gendiff import gendiff, arg_parser


def main():
    """Start main script."""
    args = arg_parser.parse()
    diff = gendiff.generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
