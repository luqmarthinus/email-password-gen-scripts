import csv
import random
import string

# Generate a normalised email using first initial + last name and a random domain
def generate_email(first_name, last_name):
    domains = ["tech-journey.co.za", "example.com", "test.com", "company.com"]
    username = f"{first_name[0].lower()}{last_name.lower()}"
    username = ''.join(e for e in username if e.isalnum())  # sanitize username
    return f"{username}@{random.choice(domains)}"

# Generate a 16-character password using letters and special characters
def generate_random_password():
    characters = string.ascii_letters + "!@%^$&*#"
    return ''.join(random.choices(characters, k=16))

# Read and clean input names
with open('names.txt', 'r') as file:
    names = file.readlines()

data = []
for name in names:
    name = name.strip()
    if not name:
        continue  # skip empty lines

    parts = name.split()
    if len(parts) < 2:
        print(f"Skipping invalid line: {name}")  # enforce first + last name
        continue

    first_name = parts[0]
    last_name = ' '.join(parts[1:])  # support multi-part surnames

    data.append({
        "email": generate_email(first_name, last_name),
        "password": generate_random_password()
    })

# Write results to CSV with fixed schema
with open('generated_email_password_pairs.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["email", "password"])
    writer.writeheader()
    writer.writerows(data)

print("Email and password pairs added to generated_email_password_pairs.csv")
