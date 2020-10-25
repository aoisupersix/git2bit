from typing import Union

from git2bit.lib.models import IdConverter


def convert(gitbucketIssue: dict, idConverter: IdConverter) -> dict:
    """
    GitbucketのIssueをBitbucketのインポータに対応した形式に変換します
    """

    reporterId = idConverter.convertToBitbucketId(gitbucketIssue['user'].get('login'))
    assigneeId = idConverter.convertToBitbucketId(gitbucketIssue.get('assignee', {}).get('login', ''))

    return {
        'assignee': assigneeId or None,
        'component': None,
        'content': gitbucketIssue.get('body'),
        'content_updated_on': gitbucketIssue.get('updated_at'),
        'created_on': gitbucketIssue.get('created_at'),
        'edited_on': gitbucketIssue.get('updated_at'),
        'id': gitbucketIssue.get('number'),
        'kind': getKind(gitbucketIssue),
        'milestone': None,  # これもGitbucketのAPIが未対応
        'priority': 'major',  # これも。ただnot nullなので何か指定する必要がある
        'reporter': {
            'display_name': reporterId,
            'account_id': reporterId,
        },
        'status': getStatus(gitbucketIssue),
        'title': gitbucketIssue.get('title'),
        'updated_on': gitbucketIssue.get('updated_at'),
        # 以下、Gitbucket対応する項目がないのでNone
        'version': None,
        'watchers': [],
        'voters': [],
    }


def getKind(gitbucketIssue: dict) -> Union[str, None]:
    """
    Gitbucketのラベルを無理やりBitbucketのkind(bug, enhancement, proposal, task)に変換します
    デフォルトは'task'
    """

    labels = gitbucketIssue['labels']
    if 'bug' in labels:
        return 'bug'
    elif 'enhancement' in labels:
        return 'enhancement'
    elif 'proposal' in labels:
        return 'proposal'

    return 'task'


def getStatus(gitbucketIssue: dict) -> str:
    """
    GitbucketのラベルとIssueの状態から無理やりBitBucketのstatus(new, open, resolved, on hold, invalid, duplicate, wontfix)に変換します
    """

    # ラベルから判断
    labels = gitbucketIssue['labels']
    if 'new' in labels:
        return 'new'
    elif 'open' in labels:
        return 'open'
    elif 'resolved' in labels:
        return 'resolved'
    elif 'on hold' in labels:
        return 'on hold'
    elif 'invalid' in labels:
        return 'invalid'
    elif 'duplicate' in labels:
        return 'duplicate'
    elif 'wontfix' in labels:
        return 'wontfix'

    # Issueの状態から判断
    if gitbucketIssue.get('state') == 'open':
        return 'open'
    else:
        return 'resolved'
