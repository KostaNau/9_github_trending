import requests
from datetime import datetime, timedelta


API_URL = 'https://api.github.com/search/repositories'


def get_trending_repositories(depth_of_request, repo_amout, target_url):
    initial_date = (datetime.now() - timedelta(days=depth_of_request)).date()
    payload = {
                'q': 'created:>={}'.format(initial_date),
                'sort': 'stars',
                'per_page': '{}'.format(repo_amout)
            }
    api_response = requests.get(target_url, params=payload).json()
    return api_response['items']


def repository_console_output(repositories):
    for count, repo in enumerate(repositories, start=1):
        print('=' * 80)
        print(count, 'Name: {name}, Stars: {stargazers_count}, Open Issues:'
              '{open_issues_count}'.format(**repo))
        print('Description: {description}'.format(**repo))
        print('Repository url: {html_url}'.format(**repo))
        print('=' * 80, end='\n\n')


if __name__ == '__main__':
    week = 7
    repo_amount = 20
    """ Max repositories returns up to 100 results per page.
    See details at https://developer.github.com/v3/#pagination
    """
    repositories = get_trending_repositories(week, repo_amount, API_URL)
    repository_console_output(repositories)
