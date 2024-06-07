import csv  # Importing the csv module to handle CSV file operations
import random  # Importing the random module to generate random choices
import string  # Importing the string module for string constants

# Function to generate a random email address based on first name and last name
def generate_email(first_name, last_name):
    # List of possible email domains
    domains = ["tech-journey.co.za", "example.com", "test.com", "company.com"]
    # Choose a random domain from the list
    domain = random.choice(domains)
    # Create a username by concatenating the first letter of the first name and the last name
    username = f"{first_name[0].lower()}{last_name.lower()}"
    # Remove any non-alphanumeric characters from the username
    username = ''.join(e for e in username if e.isalnum())
    # Return the formatted email address
    return f"{username}@{domain}"

# Function to generate a random 16-character password
def generate_random_password():
    # Characters to be included in the password
    characters = string.ascii_letters + "!@%^$&*#"
    # Generate a random password of length 16
    return ''.join(random.choices(characters, k=16))

# Read names from a text file
with open('names.txt', 'r') as file:
    names = file.readlines()  # Read all lines from the file

# Prepare the data for CSV
data = []
for name in names:
    name = name.strip()  # Remove leading/trailing whitespace
    if not name:
        continue  # Skip empty lines
    parts = name.split()  # Split the name into parts
    if len(parts) < 2:
        print(f"Skipping invalid line: {name}")
        continue  # Skip lines that don't have at least two parts
    first_name = parts[0]
    last_name = ' '.join(parts[1:])  # Join the rest as the last name
    email = generate_email(first_name, last_name)  # Generate the email
    password = generate_random_password()  # Generate the password
    data.append({"email": email, "password": password})  # Append to data list

# Write the data to a CSV file
with open('generated_email_password_pairs.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["email", "password"])  # Define CSV headers
    writer.writeheader()  # Write the header
    writer.writerows(data)  # Write the data rows

print("Email and password pairs added to generated_email_password_pairs.csv")
