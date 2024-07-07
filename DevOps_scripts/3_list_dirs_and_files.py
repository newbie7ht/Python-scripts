import os

def list_files_and_directories(path):
    try:
        for root, dirs, files in os.walk(path):
            print(f"Directory: {root}")
            for dir in dirs:
                print(f"  Sub-directory: {dir}")
            for file in files:
                print(f"  File: {file}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    path = input("Please enter the path to list directories and files: ")
    if not os.path.exists(path):
        print("The path does not exist.")
    elif not os.path.isdir(path):
        print("The path is not a directory.")
    else:
        list_files_and_directories(path)

if __name__ == "__main__":
    main()

