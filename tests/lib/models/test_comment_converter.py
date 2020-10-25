import pytest

from src.git2bit.lib.models.comment_converter import convert
from src.git2bit.lib.models import GitbucketComment
from src.git2bit.lib.models import IdConverter


@pytest.fixture
def emptyIdConverter() -> IdConverter:
    return IdConverter({})


def gitbucketBaseUser() -> dict:
    """
    GitbucketのAPIが返すUserデータのダミーを生成して返します。
    """
    return {
        'login': 'user_name',
        'email': 'email@example.com',
        'type': 'User',
        'site_admin': False,
        'created_at': '2000-01-01T00:00:00Z',
        'id': 0,
        'url': 'user_url',
        'html_url': 'user_html_url',
        'avatar_url': 'user_avatar_url'
    }


def gitbucketBaseComment() -> GitbucketComment:
    """
    GitbucketCommentのベースとなるデータを生成して返します。
    """
    payload = {
        'body': 'issue_comment',
        'created_at': '3000-01-01T00:00:00Z',
        'html_url': 'issue_html_url',
        'id': 1,
        'updated_at': '4000-01-01T00:00:00Z',
        'user': gitbucketBaseUser(),
    }
    return GitbucketComment(issueNo=1, payload=payload)


def bitbucketBaseComment() -> dict:
    """
    BitbucketCommentのベースとなるデータを生成して返します。
    """
    return {
        'content': 'issue_comment',
        'created_on': '3000-01-01T00:00:00Z',
        'id': 1,
        'issue': 1,
        'updated_on': '4000-01-01T00:00:00Z',
        'user': {
            'display_name': 'user_name',
            'account_id': 'user_name'
        },
    }


@pytest.fixture
def gitbucketComment() -> GitbucketComment:
    return gitbucketBaseComment()


@pytest.fixture
def bitbucketComment() -> dict:
    return bitbucketBaseComment()


def test_convert_normalComment(emptyIdConverter, gitbucketComment, bitbucketComment):
    actual = convert(gitbucketComment, emptyIdConverter)
    assert actual == bitbucketComment
