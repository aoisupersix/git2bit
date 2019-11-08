from typing import Union


def convert(gitbucketIssue: dict) -> dict:
    """
    GitbucketのIssueをBitbucketのインポータに対応した形式に変換します
    """

    return {
        # GitbucketのAPIだとアサインが取得できないという、、、
        # https://github.com/gitbucket/gitbucket/issues/1743 で2017年ごろに起票されているのにまだ未修正。残念
        'assignee': None,
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
            'display_name': gitbucketIssue['user'].get('login'),
            'account_id': gitbucketIssue['user'].get('login'),
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
    Gitbucketのラベルから無理やりBitBucketのstatus(new, open, resolved, on hold, invalid, duplicate, wontfix)に変換します
    デフォルトは'open'
    """

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

    return 'open'