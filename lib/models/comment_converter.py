from lib.models import GitbucketComment
from lib.models import IdConverter


def convert(gitbucketComment: GitbucketComment, idConverter: IdConverter) -> dict:
    """
    GitbucketのCommentをBitbucketのインポータに対応した形式に変換します
    """

    userId = idConverter.convertToBitbucketId(gitbucketComment.payload['user'].get('login'))
    return {
        'content': gitbucketComment.payload.get('body'),
        'created_on': gitbucketComment.payload.get('created_at'),
        'id': gitbucketComment.payload.get('id'),
        'issue': gitbucketComment.issueNo,
        'updated_on': gitbucketComment.payload.get('updated_at'),
        'user': {
            'display_name': userId,
            'account_id': userId,
        },
    }
