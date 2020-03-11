import csv


def print_file_content(file):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(row)


def write_list_to_file(output_file, *lst):
    with open(output_file, "w") as f:
        f.write('\n'.join(str(s) for s in lst))


def read_csv(input_file):
    lst = []
    with open(input_file) as file:
        reader = csv.reader(file)
        for row in reader:
            lst.append(row)
    return lst


