from package.dependencies import *


# Function to check if the csv file we will create exists, if yes, delete it
def delete_csv_if_exists():
    if os.path.exists('tags.csv') and os.path.isfile('tags.csv'):
        os.remove('tags.csv')


# Function to write in the csv file
def write_csv(*argv) -> object:
    fields = []
    for arg in argv:
        fields.append(arg)
    with open('tags.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
