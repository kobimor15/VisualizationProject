import os
import csv

def process_csv_files(folder_path):
    # Get a list of all files in the folder
    file_list = os.listdir(folder_path)

    # Iterate over each file in the folder
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)

        # Check if the file is a CSV file
        if file_name.endswith(".csv"):
            # Create a temporary file to write the updated data
            temp_file_path = os.path.join(folder_path, "temp.csv")

            with open(file_path, "r") as file, open(temp_file_path, "w", newline="") as temp_file:
                reader = csv.DictReader(file)
                writer = csv.DictWriter(temp_file, fieldnames=reader.fieldnames)

                writer.writeheader()

                # Iterate over each row in the CSV file
                for row in reader:
                    confirmed = int(row["confirmed"])
                    deaths = int(row["deaths"])
                    active = int(row["active"])

                    # Calculate the recovered value as the difference between confirmed, deaths, and active

                    # = (confirmed > 0 ? confirmed: 0) - (deaths > 0 ? deaths:0) - (active > 0 ? active:0)
                    recovered = (confirmed if confirmed > 0 else 0) - (deaths if deaths > 0 else 0) - (active if active > 0 else 0)

                    #recovered = confirmed - deaths - active
                    row["recovered"] = str(recovered)

                    # Write the updated row to the temporary file
                    writer.writerow(row)

            # Replace the original file with the temporary file
            os.remove(file_path)
            os.rename(temp_file_path, file_path)

    print("Data processing completed successfully.")

# Example usage
folder_path = "C:/Users/kobim/PycharmProjects/Visuzalization/CountryData"

process_csv_files(folder_path)