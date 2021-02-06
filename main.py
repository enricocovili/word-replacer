from pathlib import Path
import argparse

def main():

    input = setup()
    dir_path = Path(input.Path)

    if dir_path.is_dir() and input.recorsive:
        files_to_edit = dir_path.glob('**/*.*')    
        for file in files_to_edit:
            word_replacer(file, input)

    elif dir_path.is_file():
        word_replacer(dir_path, input)

    elif dir_path.is_dir():
        print("Error 2: selected a direcory without -r argument")
        exit(2)

    else:
        print("Error 1: wrong path")
        exit(1)

def word_replacer(file, dir):

    initial_text = file.read_text()
    replacement_text = initial_text.replace(dir.find, dir.replace)
    file.write_text(replacement_text)
    if dir.verbose:
        print(f"modifying file \t {file}")

def setup():
    parser = argparse.ArgumentParser(prog='word_replacer',
                                    description='Change one word with another in a text file (works also with directory recusively')
    parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='path of the folder')
    parser.add_argument('find',
                       metavar='find word',
                       type=str,
                       help='the word/phrase that will be modified')
    parser.add_argument('replace',
                       metavar='replace word',
                       type=str,
                       help='the replace word/phrase')
    parser.add_argument('-v',
                       '--verbose',
                       action='store_true',
                       help='Execute the script verbosely')
    parser.add_argument('-r',
                       '--recorsive',
                       action='store_true',
                       help='Search in a directory (and subdirectoy)')

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main()
