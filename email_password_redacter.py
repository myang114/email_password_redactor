import re
import sys
import random
import string

'''
Hello!

Welcome to the email password redacter. This program takes a text file
of emails along with their passwords and will redact the password.
It uses sys.argv so you will input 

python email_password_redactor <filename> <email type>

The program will search through the file for the type of email you
input whether it is gmail, yahoo, or terpmail
and will hide the passwords for those emails.
'''

def redact_password(match):
    # Function to redact a password in the format "<email>: <password>"
    # based on a regular expression match. It replaces the password with
    # random characters of the same length.
    # this will change them to random letters
    return match.group(1) + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(len(match.group(2))))

def redact_file(filename, email):
    # Function to redact passwords in a given file based on the specified
    # email provider (Gmail, Terpmail, or Yahoo) using regular expressions.
    # the modified content back to the file.

    try:
        # Read the content of the file
        with open(filename, 'r') as file:
            content = file.read()

        # Define the regular expression pattern based on the specified email
        if email == 'gmail':
            pattern = r'(\bgmail\.com\b)(\s*:\s*\S+)'
        elif email == 'terpmail':
            pattern = r'(\bterpmail\.umd\.edu\b)(\s*:\s*\S+)'
        elif email == 'yahoo':
            pattern = r'(\byahoo\.com\b)(\s*:\s*\S+)'
        else:
            print("Invalid provider. Please choose 'gmail', 'terpmail', or 'yahoo'.")
            return

        # Use regular expression substitution to redact passwords
        redacted_content = re.sub(pattern, redact_password, content)

        # Write the redacted content back to the file
        with open(filename, 'w') as file:
            file.write(redacted_content)

        print(f"Passwords redacted for {email} emails in {filename}.")
    # Catches all errors if the file cant be found
    except FileNotFoundError:
        print(f"File not found: {filename}")

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    # Went over this in class
    if len(sys.argv) != 3:
        print("Usage: python file_editor.py <filename> <provider>")
    else:
        # Extract the filename and provider from command-line arguments
        filename = sys.argv[1]
        provider = sys.argv[2].lower()
        # Call the redact_file function to perform redaction
        redact_file(filename, provider)