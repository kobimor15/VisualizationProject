import os

def remove_updated_suffix(folder_path):
    # Get a list of all files in the directory
    file_list = os.listdir(folder_path)

    # Iterate over the files and remove the suffix '_updated' from the file names
    for file_name in file_list:
        if file_name.endswith('_updated.csv'):
            updated_file_path = os.path.join(folder_path, file_name)
            new_file_name = file_name.replace('_updated', '')
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(updated_file_path, new_file_path)
            print(f"File name updated: {file_name} -> {new_file_name}")


# Specify the directory containing the CSV files
folder_path = 'CountryData'

# Remove the suffix '_updated' from the CSV file names
remove_updated_suffix(folder_path)