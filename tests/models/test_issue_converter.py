import pytest

from lib.models.issue_converter import convert


@pytest.fixture
def gitbucketIssue():
    return {
        'number': 1,
        'title': 'issue_title',
        'user': {
            'login': 'user_name',
            'email': 'email@example.com',
            'type': 'User',
            'site_admin': False,
            'created_at': '2000-01-01T00:00:00Z',
            'id': 0,
            'url': 'user_url',
            'html_url': 'user_html_url',
            'avatar_url': 'user_avatar_url'
        },
        'labels': [],
        'state': 'open',
        'created_at': '3000-01-01T00:00:00Z',
        'updated_at': '4000-01-01T00:00:00Z',
        'body': 'issue_summary',
        'id': 0,  # Gitbucketは必ず0を返す。ダミー
        'comments_url': 'issue_comment_url',
        'html_url': 'issue_html_url'
    }


@pytest.fixture
def bitbucketIssue():
    return {
        'assignee': None,
        'component': None,
        'content': 'issue_summary',
        'content_updated_on': '4000-01-01T00:00:00Z',
        'created_on': '3000-01-01T00:00:00Z',
        'edited_on': '4000-01-01T00:00:00Z',
        'id': 1,
        'kind': 'task',
        'milestone': None,
        'priority': 'major',
        'reporter': {
            'display_name': 'user_name',
            'account_id': 'user_name'
        },
        'status': 'open',
        'title': 'issue_title',
        'updated_on': '4000-01-01T00:00:00Z',
        'version': None,
        'watchers': [],
        'voters': []
    }


def test_convert_normalIssue(gitbucketIssue, bitbucketIssue):
    actual = convert(gitbucketIssue)
    assert actual == bitbucketIssue
