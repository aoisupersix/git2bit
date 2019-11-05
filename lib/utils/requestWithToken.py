import requests


def getRequestWithToken(url: str, token: str, payload={}) -> requests.Response:
    """
    引数に与えられたURLに認証トークン付きでGetリクエストを送信し、結果を返します。
    """
    header = {
        'Authorization': f'token {token}',
        'content-type': 'application/json'
    }
    return requests.get(url, headers=header, params=payload)
