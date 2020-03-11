import os

def write_elements_in_folder(folder, output_file):
    with open(output_file, 'w') as file:
        for element in os.listdir(folder):
            file.write(folder + '\\' + element + '\n')

def write_elements_in_folder_incl_subfolder(folder, output_file):
    with open(output_file, 'w') as file:
        for path, subdirs, files in os.walk(folder):
            for name in files:
                file.write(os.path.join(path, name) + '\n')

def read_first_line(lst):
    for files in lst:
        with open(files, 'r') as file:
            print(file.readline())

def print_email(lst):
    for files in lst:
        with open(files, 'r') as file:
            for line in file:
                if '@' in line:
                    print(line)

def print_md_headlines(lst):
    for files in lst:
        with open(files, 'r') as file:
            for line in file:
                if line.startswith('#'):
                    print(line)
