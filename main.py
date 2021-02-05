from pathlib import Path

def main():
    
    dir_path = Path(input("path to the folder -> "))
    target_string = input("insert the word/phrase that will be modified -> ")
    replacement_string = input("insert the replace word/phrase -> ")

    if Path(dir_path).is_dir():
        files_to_edit = dir_path.glob('**/*.*')    
        for file in files_to_edit:
            word_replacer(file, target_string, replacement_string)

    elif Path(dir_path).is_file():
        word_replacer(dir_path, target_string, replacement_string)

    else:
        print("incorrect path")

def word_replacer(file, target_string, replacement_string):
    initial_text = file.read_text()
    replacement_text = initial_text.replace(target_string, replacement_string)
    file.write_text(replacement_text)

if __name__ == "__main__":
    main()