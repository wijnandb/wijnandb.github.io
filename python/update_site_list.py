import subprocess
import json
import requests

def get_repositories():
    all_repos = []
    page = 1
    while True:
        url = f'https://api.github.com/users/wijnandb/repos?page={page}&per_page=100'
        response = requests.get(url)
        if response.status_code != 200:
            print(f'Failed to retrieve repositories: {response.content}')
            break

        repos = response.json()
        if not repos:
            break  # Break if there are no more repositories

        all_repos.extend(repos)
        page += 1

    return all_repos

def check_site(repo_name):
    url = f'https://wijnandb.github.io/{repo_name}'
    response = requests.get(url)
    return response.status_code == 200


def update_site_list():
    repos = get_repositories()
    active_sites = []

    for repo in repos:
        if check_site(repo['name']):
            site_info = {
                'name': repo['name'],
                'html_url': repo['html_url'],
                'created_at': repo['created_at'],
                'updated_at': repo['updated_at'],
                'open_issues_count': repo['open_issues_count'],
                'default_branch': repo['default_branch'],
                'homepage': "https://wijnandb.github.io/"+ repo['name'],
                'description': repo['description'],
            }
            active_sites.append(site_info)

    # Update a file in your Jekyll site with the list of active sites
    with open('/data/allsites.json', 'w') as file:
        json.dump(active_sites, file, indent=4)

if __name__ == "__main__":
    update_site_list()
