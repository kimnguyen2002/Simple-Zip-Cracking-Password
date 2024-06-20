import zipfile
import itertools
import string

print("\n\nStart.........\n\n")

# Create a list of characters to use in the password
characters = string.ascii_lowercase + string.digits

# Define the ZIP file to be opened
zip_file_path = 'test.zip'

# Function to generate all possible passwords
def generate_passwords(max_length):
    for length in range(1, max_length + 1):
        for password in itertools.product(characters, repeat=length):
            yield ''.join(password)

# Open the ZIP file
with zipfile.ZipFile(zip_file_path) as the_zip_package:
    found_password = False
    for current_password in generate_passwords(6):
        try:
            print(f"Trying to extract '{the_zip_package.filename}' with the password '{current_password}'")
            the_zip_package.extractall(pwd=current_password.encode())
            found_password = True
            print(f"\n\nThe correct password is '{current_password}'.")
            break
        except (RuntimeError, zipfile.BadZipFile) as e:
            print(f"'{current_password}' is not the correct password", end='\n\n')

    if not found_password:
        print("\n\nNone of the generated passwords is correct.")

print("\n\nEnd.......\n\n")
