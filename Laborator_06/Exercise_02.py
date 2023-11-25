import os
import sys

def rename_files(directory_path):
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")

        k = 1
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_extension = os.path.splitext(file)[1]
                new_name = f"{os.path.splitext(file)[0]}_{k}{file_extension}"
                k += 1

                full_path_old = os.path.join(root, file)
                full_path_new = os.path.join(root, new_name)

                try:
                    os.rename(full_path_old, full_path_new)
                    print(f"File '{full_path_old}' renamed to '{full_path_new}'.")
                except FileNotFoundError:
                    print(f"Error: File '{full_path_old}' not found.")
                except Exception as e:
                    print(f"Error renaming file '{full_path_old}': {e}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Permission error: {e}")
    except Exception as e:
        print(f"Error accessing directory '{directory_path}': {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("You should type: python script_name.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        rename_files(directory_path)
