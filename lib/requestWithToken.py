import requests


def getRequestWithToken(url, token):
    """
    引数に与えられたURLに認証トークン付きでGetリクエストを送信し、結果を返します。
    """
    header = {'Authorization': f'token {token}'}
    requests.get(url, headers=header)