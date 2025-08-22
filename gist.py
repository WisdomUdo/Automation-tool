import requests

# Replace with your GitHub Personal Access Token
GITHUB_TOKEN = "your_personal_access_token"

# API URL for creating a Gist
GITHUB_API_URL = "https://api.github.com/gists"

# Headers for authentication
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def create_gist(filename, content, description="", public=True):
    """Create a GitHub Gist using the API."""
    payload = {
        "description": description,
        "public": public,
        "files": {
            filename: {
                "content": content
            }
        }
    }
    
    response = requests.post(GITHUB_API_URL, headers=headers, json=payload)
    
    if response.status_code == 201:
        gist_url = response.json().get("html_url")
        print(f"Gist created successfully: {gist_url}")
        return gist_url
    else:
        print(f"Failed to create Gist: {response.status_code}")
        print(response.json())
        return None


if __name__ == "__main__":
    # Example usage
    filename = "example.py"
    content = """# Sample Python script
print("Hello, GitHub Gist!")"""
    description = "My first automated Gist"
    
    create_gist(filename, content, description, public=True)
