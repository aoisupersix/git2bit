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

    def getIssues(self, pageNum, state='open'):
        """
        Issueを1ページ分取得します
        """
        payload = {
            'page': pageNum,
            'state': state
        }
        response = request.getRequestWithToken(f'{self.listIssuesUrl}', self.token, payload)
        issues = response.json()
        return issues

    def getAllIssues(self):
        pageNum = 1
        allIssues = []
        while True:
            issues = self.getIssues(pageNum)
            if not issues:
                break
            allIssues.extend(issues)
            pageNum += 1

        return allIssues
