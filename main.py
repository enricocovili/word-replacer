from pathlib import Path
import argparse

class colors:
    WARNING = '\033[93m'
    # FAIL = '\033[91m'
    ENDLINE = '\033[0m'

def _parse_args():
    parser = argparse.ArgumentParser(
        prog='word_replacer',
        description='Change one word with another in a text file (works also with directory recusively',
    )
    parser.add_argument('path',
                        metavar='path',
                        type=Path,
                        help='path to file or folder')
    parser.add_argument('find',
                        metavar='find-word',
                        type=str,
                        help='the word/phrase that will be modified')
    parser.add_argument('replace',
                        metavar='replace-word',
                        type=str,
                        help='the replace word/phrase')
    parser.add_argument('-v',
                        '--verbose',
                        action='store_true',
                        help='Execute the script verbosely')
    parser.add_argument('-d',
                        '--directory',
                        action='store_true',
                        help='Modify files in a directory')
    parser.add_argument('-r',
                        '--recursive',
                        action='store_true',
                        help='Search all subdirectories recursively. Requires "-d"')

    args = parser.parse_args()
    _validate_args(args)
    return args

def _validate_args(args: argparse.Namespace):
    if not args.path.exists():
        print('Path does not exist')
    elif args.directory and not args.path.is_dir():
        print('Not a directory path. Remove the "-d" flag to work with a single file')
    elif not args.directory and args.path.is_dir():
        print('Not a file path. Use the "-d" flag to work with a directory')
    elif args.recursive and not args.directory:
        print('Recursive mode cannot be used when working with a single file. '
              'Use the "-d" flag to work with a directory')
    else:
        return
    exit(1)


def _replace_in_file(file: Path, target: str, replacement: str, verbose: bool):
    if verbose:
        print(f"modifying file \t {file}")
    try:
        initial_text = file.read_text()
        replacement_text = initial_text.replace(target, replacement)
        file.write_text(replacement_text)
    except (UnicodeDecodeError, PermissionError) as err:
        if verbose:
            print(f"{colors.WARNING}failed to modify file {file}:\n{err}, skipping{colors.ENDLINE}")
        return

def main():
    args = _parse_args()

    if args.directory:
        files_to_edit = args.path.glob('**/*.*' if args.recursive else '*.*')
    else:
        files_to_edit = [args.path]

    for file in files_to_edit:
        if file.is_dir(): continue
        _replace_in_file(
            file,
            target=args.find,
            replacement=args.replace,
            verbose=args.verbose,
        )

if __name__ == "__main__":
    main()