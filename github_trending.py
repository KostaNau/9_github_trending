import requests
from datetime import datetime, timedelta


def get_trending_repositories(depth_of_request, repo_amout):
    target_url = 'https://api.github.com/search/repositories'
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
        print(count, 'Name: {name}, Stars: {stars}, Open Issues: {issues}'
              .format(name=repo['name'],
                      stars=repo['stargazers_count'],
                      issues=repo['open_issues_count'])
              )
        print('Description: {}'.format(repo['description']))
        print('Repository url: {}'.format(repo['html_url']))
        print('=' * 80, end='\n\n')


if __name__ == '__main__':
    week = 7
    repositories_amount = 20
    """ Max repositories returns up to 100 results per page.
    See details at https://developer.github.com/v3/#pagination
    """
    repositories = get_trending_repositories(week, repositories_amount)
    repository_console_output(repositories)
