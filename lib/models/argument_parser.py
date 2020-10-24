import argparse


def parse() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='transfer your Gitbucket issues to Bitbucket.')
    parser.add_argument('-e', '--api-endpoint', required=True,
                        help='Gitbucket API endpoint URL. (http(s)://yourgitbucket/api/v3)')
    parser.add_argument('-o', '--owner', required=True,
                        help='Gitbucket owner user or group name from which the issue was migrated.')
    parser.add_argument('-r', '--repo', required=True,
                        help='Gitbucket repository name from which the issue was migrated.')
    parser.add_argument('-t', '--token', required=True,
                        help='Personal access token to access the Gitbucket API.')
    parser.add_argument('-m', '--mapping',
                        help='Path from Gitbucket to Bitbucket user id mapping definition file. (*.yml)')
    parser.add_argument('--output',
                        help='Output file path of Bitbucket Issue export data.')
    parser.add_argument('--write-apiresponse', action='store_true',
                        help='Write the Gitbucket API response in the ./tmp directory.')

    args = parser.parse_args()
    args.api_endpoint = removeTrailingSlash(args.api_endpoint)

    return args


def removeTrailingSlash(str: str) -> str:
    """
    URL末尾にスラッシュがあった場合に削除します。
    """
    return str.rstrip('/')
