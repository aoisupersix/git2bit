from lib.models import issue_converter


def convert(issues: list, comments: list) -> dict:
    """
    Bitbucketにインポートできる形式に変換します
    """
    return {
        'issues': [issue_converter.convert(issue) for issue in issues],
        'comments': comments,
        'attachments': [],
        'logs': [],  # これはGitbucketのAPIからは取得できないので空
        'meta': {
            'default_assignee': None,
            'default_component': None,
            'default_kind': 'task',  # これは引数で設定できるようにしたい
            'default_milestone': None,
            'default_version': None,
        },
        'components': [],
        'milestones': [],
        'versions': [],
    }
