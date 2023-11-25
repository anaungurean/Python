import sys
import os


def list_searched_files(directory_path, file_extension):
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Directory '{directory_path}' not found.")

        if not file_extension.startswith('.') or len(file_extension) < 2:
            raise ValueError("Invalid file extension. It should start with a dot (.) and not be empty.")

        searched_files = []

        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if os.path.splitext(file)[1] == file_extension:
                    searched_files.append(os.path.join(root, file))

        if not searched_files:
            print(f"There is no file with extension '{file_extension}' in directory '{directory_path}' and its subdirectories")
        else :
            for file in searched_files:
                try:
                    with open(file, 'r') as f:
                        print(f"\nContents of {file}:")
                        for line in f:
                            print(line.strip())
                except Exception as file_access_error:
                    print(f"Error accessing file '{file}': {file_access_error}")

    except FileNotFoundError as dir_not_found_error:
        print(dir_not_found_error)
    except ValueError as value_error:
        print(value_error)
    except Exception as e:
        print(f"An error has happened: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("You should type: python Exercise_01.py <directory_path> <file_extension>")
    else:
        directory_path = sys.argv[1]
        file_extension = sys.argv[2]
        list_searched_files(directory_path, file_extension)
