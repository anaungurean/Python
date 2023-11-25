import os
import sys


def calculate_total_size(directory_path):
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")

        sum = 0
        for (root, directories, files) in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)

                try:
                    if os.path.isfile(file_path):
                        sum += os.path.getsize(file_path)
                except (PermissionError, FileNotFoundError) as e:
                    print(f"Error accessing file '{file_path}': {e}")

        print(f"Total size of all files in '{directory_path}' is: {sum} bytes")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Permission error: {e}")
    except Exception as e:
        print(f"Error accessing directory '{directory_path}': {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("You should type: python Exercise_03.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        calculate_total_size(directory_path)
