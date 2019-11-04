from lib import requestWithToken as request


class GitbucketApi:
    def __init__(self, endpoint, owner, repo, token):
        self.endpoint = endpoint
        self.owner = owner
        self.repo = repo
        self.token = token

    @property
    def listIssuesUrl(self):
        return f'{self.endpoint}/api/v3/repos/{self.owner}/{self.repo}/issues'

    def getIssues(self, pageNum):
        response = request.getRequestWithToken(f'{self.listIssuesUrl}?page={pageNum}', self.token)
        issues = response.json()
        return issues
