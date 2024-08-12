import csv  # Import the csv module to work with CSV files

# Define a list of dictionaries, each representing a user
users = [
    {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"}, 
    {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"}, 
    {"name": "Charlie Grey", "username": "greyc", "department": "Development"}
]

# Define the keys that will be used as column headers in the CSV file
keys = ["name", "username", "department"]

# Open a new file named 'by_department.csv' in write mode
with open('by_department.csv', 'w') as by_department:
    # Create a DictWriter object
    writer = csv.DictWriter(by_department, fieldnames=keys)

    
    # Write the headers (keys) as the first row in the CSV file
    writer.writeheader()
    
    # Write all user data to the CSV file
    # Each dictionary in 'users' will become a row in the file
    writer.writerows(users)

# The file is automatically closed when we exit the 'with' block

with open ('by_department.csv', 'r') as file:
    print(file.readlines())