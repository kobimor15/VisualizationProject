import os
import csv

def delete_data_from_date(folder_path, delete_date):
    # Get a list of all files in the folder
    file_list = os.listdir(folder_path)

    # Iterate over each file in the folder
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)

        # Check if the file is a CSV file
        if file_name.endswith(".csv"):
            # Create a temporary file to write the filtered data
            temp_file_path = os.path.join(folder_path, "temp.csv")

            with open(file_path, "r") as file, open(temp_file_path, "w", newline="") as temp_file:
                reader = csv.reader(file)
                writer = csv.writer(temp_file)

                header = next(reader)  # Read and write the header
                writer.writerow(header)

                # Find the index of the "date" column
                date_column_index = header.index("date")

                # Iterate over each row in the CSV file
                for row in reader:
                    # Check if the date is before the delete date
                    if row[date_column_index] < delete_date:
                        writer.writerow(row)

            # Replace the original file with the temporary file
            os.remove(file_path)
            os.rename(temp_file_path, file_path)

    print("Data deletion completed successfully.")

# Example usage
folder_path = "C:/Users/kobim/PycharmProjects/Visuzalization/CountryData"
delete_date = "2021-08-01"

delete_data_from_date(folder_path, delete_date)