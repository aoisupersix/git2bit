import argparse


def parse() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='transfer your gitbucket issues to bitbucket.')
    parser.add_argument('-ge', '--gitbucket_endpoint', required=True)
    parser.add_argument('-go', '--gitbucket_owner', required=True)
    parser.add_argument('-gr', '--gitbucket_repo', required=True)
    parser.add_argument('-gt', '--gitbucket_token', required=True)
    parser.add_argument('-m', '--mapping', required=False)

    args = parser.parse_args()
    args.gitbucket_endpoint = removeTrailingSlash(args.gitbucket_endpoint)

    return args


def removeTrailingSlash(str: str) -> str:
    """
    URL末尾にスラッシュがあった場合に削除します。
    """
    return str.rstrip('/')
