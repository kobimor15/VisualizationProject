import os
import csv

def update_recovery_column(file_path = ''):
    # Create a new file name for the updated CSV file
    output_file_path = file_path.replace('.csv', '_updated.csv')

    # Open the CSV file for reading and create a new CSV file for writing
    with open(file_path, 'r+', newline='') as input_file, \
            open(output_file_path, 'w', newline='') as output_file:

        reader = csv.reader(input_file)
        writer = csv.writer(output_file)

        # Read the header row and write it to the output file
        header = next(reader)
        writer.writerow(header)

        # Find the index of the required columns
        confirmed_index = header.index('confirmed')
        deaths_index = header.index('deaths')
        recovered_index = header.index('recovered')

        # Initialize the previous recovered value
        prev_recovered = 0

        # Update the 'recovered' column and write the updated row to the output file
        for row in reader:
            confirmed = int(row[confirmed_index])
            deaths = int(row[deaths_index])

            recovered = confirmed - deaths
            if recovered <= 0:
                recovered = prev_recovered

            row[recovered_index] = recovered
            writer.writerow(row)

            # Update the previous recovered value
            prev_recovered = recovered

    print("Updated file has been created:", output_file_path)


# Specify the directory containing the CSV files
folder_path = 'CountryData'

# Get a list of all files in the directory
file_list = os.listdir(folder_path)

# Iterate over the files and process only the ones with the prefix 'cases_per_day_agg_'
for file_name in file_list:
    if file_name.startswith('cases_per_day_agg_') and file_name.endswith('.csv'):
        file_path = os.path.join(folder_path, file_name)
        update_recovery_column(file_path)