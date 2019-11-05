from lib.utils import requestWithToken as request


class GitbucketApi:
    def __init__(self, endpoint, owner, repo, token):
        self.endpoint = endpoint
        self.owner = owner
        self.repo = repo
        self.token = token

    @property
    def listIssuesUrl(self):
        return f'{self.endpoint}/api/v3/repos/{self.owner}/{self.repo}/issues'

    def getIssuesPerPage(self, pageNum, state='open'):
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

    def getIssues(self, state='open'):
        """
        全ページのIssueを取得します
        """
        pageNum = 1
        issues = []
        while True:
            issuesPerPage = self.getIssuesPerPage(pageNum, state)
            if not issuesPerPage:
                break
            issues.extend(issuesPerPage)
            pageNum += 1

        return issues

    def getAllIssues(self):
        """
        リポジトリの全Issueを取得します
        """
        allIssues = self.getIssues('open')
        allIssues.extend(self.getIssues('closed'))
        return allIssues
