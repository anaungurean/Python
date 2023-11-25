import sys
import os


def count_groups_of_files(directory_path):
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")

        if not os.listdir(directory_path):
            print(f"The directory '{directory_path}' is empty.")
            return

        counter = dict()
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_extension = os.path.splitext(file)[1]
                if file_extension in counter.keys():
                    counter[file_extension] += 1
                else:
                    counter.setdefault(file_extension, 1)

        print("File counts by extension:")
        for extension, count in counter.items():
            print(f"{extension}: {count} files")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Permission error: {e}")
    except Exception as e:
        print(f"Error accessing directory '{directory_path}': {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("You should type: python Exercise_04.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        count_groups_of_files(directory_path)
