import requests

API_TOKEN = 'your-api-token'
BASE_URL = 'http://your-gitea-instance/api/v1'
HEADERS = {'Authorization': f'token {API_TOKEN}'}

# Get all members of the organization
def get_org_members(org_name):
    url = f'{BASE_URL}/orgs/{org_name}/members'
    response = requests.get(url, headers=HEADERS)
    return response.json()

# Get all repositories for a specific user
def get_user_repos(username):
    url = f'{BASE_URL}/users/{username}/repos'
    response = requests.get(url, headers=HEADERS)
    return response.json()

# Get pull requests for a specific repo
def get_repo_pulls(owner, repo_name):
    url = f'{BASE_URL}/repos/{owner}/{repo_name}/pulls'
    response = requests.get(url, headers=HEADERS)
    return response.json()

# Example usage
org_name = 'your-org-name'
members = get_org_members(org_name)

for member in members:
    username = member['username']
    repos = get_user_repos(username)
    for repo in repos:
        pulls = get_repo_pulls(username, repo['name'])
        print(f"Pull requests for {username}/{repo['name']}: {pulls}")
    