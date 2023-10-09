import os
import requests
import json

# Use the token stored in the environment variable
token = os.environ['GITHUB_TOKEN']

# Replace with your actual values
owner = 'wijnandb'
repo = 'bredeschool'

# URL to fetch issues from the repository
url = f"https://api.github.com/repos/{owner}/{repo}/issues"

# Headers for authentication
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json',  # Use GitHub API version 3
}

# Make a GET request to the GitHub API
response = requests.get(url, headers=headers)

# Handle potential errors
response.raise_for_status()

# Get JSON data
issues_data = response.json()

# Save data to a JSON file, using the repo name
filename = f"{repo}_issues.json"
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(issues_data, f, ensure_ascii=False, indent=4)
