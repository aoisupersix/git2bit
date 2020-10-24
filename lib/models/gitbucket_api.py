import requests
from typing import NamedTuple, List


class GitbucketComment(NamedTuple):
    issueNo: int
    payload: dict


class GitbucketApi:
    def __init__(self, endpoint: str, owner: str, repo: str, token: str) -> None:
        self.__endpoint = endpoint
        self.__owner = owner
        self.__repo = repo
        self.__token = token

    @property
    def baseUrl(self) -> str:
        return f'{self.__endpoint}/api/v3/repos/{self.__owner}/{self.__repo}'

    def __getRequestWithToken(self, subUrl: str, payload={}) -> requests.Response:
        """
        引数に与えられたURLに認証トークン付きでGetリクエストを送信し、結果を返します。
        """
        header = {
            'Authorization': f'token {self.__token}',
            'content-type': 'application/json'
        }
        response = requests.get(
            f'{self.baseUrl}/{subUrl}', headers=header, params=payload)

        if not response.ok:
            raise RuntimeError('''
                Gitbucket API did not return a normal response.
                ------------------------------------------------
                requested_url: {url}
                status_code: {status_code}
                response_text: {response}
                '''.format(url=response.url, status_code=response.status_code, response=response.text))

        return response

# region Issues
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
# endregion

    def getLabels(self) -> list:
        """
        リポジトリの全ラベルを取得します
        """

        response = self.__getRequestWithToken('labels')
        return response.json()

    def getIssueComments(self, issueNo: int) -> List[GitbucketComment]:
        """
        引数に指定されたIssueの全コメントを取得します
        """

        response = self.__getRequestWithToken(f'issues/{issueNo}/comments')
        issues = response.json()
        issues = map(lambda i: GitbucketComment(issueNo=issueNo, payload=i), issues)
        return issues

    def getIssuesComments(self, issueNos: list) -> List[GitbucketComment]:
        """
        引数に指定されたIssueの全コメントを取得します
        """

        allComments: List[GitbucketComment] = []
        for issueNo in issueNos:
            allComments.extend(self.getIssueComments(issueNo))

        return allComments
