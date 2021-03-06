from typing import List

from lib.models import comment_converter
from lib.models import GitbucketComment
from lib.models import issue_converter
from lib.models import IdConverter


def convert(issues: list, comments: List[GitbucketComment], idConverter: IdConverter) -> dict:
    """
    Bitbucketにインポートできる形式に変換します
    """
    return {
        'issues': [issue_converter.convert(issue, idConverter) for issue in issues],
        'comments': [comment_converter.convert(comment, idConverter) for comment in comments],
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
