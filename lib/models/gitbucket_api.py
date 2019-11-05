import requests


class GitbucketApi:
    def __init__(self, endpoint: str, owner: str, repo: str, token: str) -> None:
        self.__endpoint = endpoint
        self.__owner = owner
        self.__repo = repo
        self.__token = token

    @property
    def baseUrl(self) -> str:
        return f'{self.__endpoint}/api/v3/{self.__owner}/{self.__repo}'

    def __getRequestWithToken(self, subUrl: str, payload={}) -> requests.Response:
        """
        引数に与えられたURLに認証トークン付きでGetリクエストを送信し、結果を返します。
        """
        header = {
            'Authorization': f'token {self.__token}',
            'content-type': 'application/json'
        }
        return requests.get(
            f'{self.baseUrl}/{subUrl}', headers=header, params=payload)

    def getIssuesPerPage(self, pageNum: int, state='open') -> list:
        """
        Issueを1ページ分取得します
        """
        payload = {
            'page': pageNum,
            'state': state
        }
        response = self.__getRequestWithToken('issues', payload)
        issues = response.json()
        return issues

    def getIssues(self, state='open') -> list:
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

    def getAllIssues(self) -> list:
        """
        リポジトリの全Issueを取得します
        """
        allIssues = self.getIssues('open')
        allIssues.extend(self.getIssues('closed'))
        return allIssues
