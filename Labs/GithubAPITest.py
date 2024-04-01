import json
import time
import unittest

import requests

# To run use ```python -m unittest .\GithubAPITest.py```

class GithubAPITest(unittest.TestCase):

    def test_get_repo_info(self):
        repo_url = "https://api.github.com/repos/facebook/react"

        response = requests.get(repo_url)

        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)

        self.assertEqual(data['name'], 'react')
        self.assertEqual(
            data['description'],
            'A declarative, efficient, and flexible JavaScript library for building user interfaces.'
        )

    def test_get_repo_info_200(self):
        repo_url = "https://api.github.com/repos/facebook/react"

        response = requests.get(repo_url)

        self.assertEqual(response.status_code, 200)

    def test_get_commits(self):
        repo_url = "https://api.github.com/repos/facebook/react"
        response = requests.get(repo_url)
        data = json.loads(response.content)
        commits_url = data['commits_url']
        commits_response = requests.get(commits_url)

        self.assertEqual(commits_response.status_code, 200)

        commits = json.loads(commits_response.content)

        self.assertGreaterEqual(len(commits), 1)

    def test_get_commits_since(self):
        repo_url = "https://api.github.com/repos/facebook/react/commits"

        params = {
            'since': '2023-01-01'
        }

        response = requests.get(repo_url, params=params)

        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)

        for commit in data:
            self.assertIsNotNone(commit['commit']['author']['date'], "Commit should have a valid author date")
            self.assertGreaterEqual(commit['commit']['author']['date'], '2023-01-01T00:00:00Z',
                                    "Commit date should be after the specified since date")

    def test_get_repo_info_speed(self):
        repo_url = "https://api.github.com/repos/facebook/react"

        start_time = time.time()

        response = requests.get(repo_url)

        end_time = time.time()
        self.assertEqual(response.status_code, 200)
        self.assertLess(end_time - start_time, 1)


if __name__ == '__main__':
    unittest.main() 
