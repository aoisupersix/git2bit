import argparse


def parse() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='transfer your Gitbucket issues to Bitbucket.')
    parser.add_argument('-ge', '--gitbucket_endpoint', required=True,
                        help='Gitbucket API endpoint URL. (http(s)://yourgitbucket/api/v3)')
    parser.add_argument('-go', '--gitbucket_owner', required=True,
                        help='Gitbucket owner user or group name from which the issue was migrated.')
    parser.add_argument('-gr', '--gitbucket_repo', required=True,
                        help='Gitbucket repository name from which the issue was migrated.')
    parser.add_argument('-gt', '--gitbucket_token', required=True,
                        help='Personal access token to access the Gitbucket API.')
    parser.add_argument('-m', '--mapping', required=False,
                        help='Path from Gitbucket to Bitbucket user id mapping definition file. (*.yml)')

    args = parser.parse_args()
    args.gitbucket_endpoint = removeTrailingSlash(args.gitbucket_endpoint)

    return args


def removeTrailingSlash(str: str) -> str:
    """
    URL末尾にスラッシュがあった場合に削除します。
    """
    return str.rstrip('/')
