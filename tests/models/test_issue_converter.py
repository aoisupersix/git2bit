import pytest

from lib.models.issue_converter import convert
from lib.models import IdConverter


@pytest.fixture
def emptyIdConverter():
    return IdConverter({})


def gitbucketBaseIssue():
    """
    GitbucketIssueのベースとなるデータを生成して返します。
    """
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


def bitbucketBaseIssue():
    """
    BitbucketIssueのベースとなるデータを生成して返します。
    """
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


@pytest.fixture
def gitbucketIssue():
    return gitbucketBaseIssue()


@pytest.fixture
def bitbucketIssue():
    return bitbucketBaseIssue()


@pytest.fixture
def gitbucketBugIssue():
    issue = gitbucketBaseIssue()
    issue['labels'] = ['bug']
    return issue


@pytest.fixture
def bitbucketBugIssue():
    issue = bitbucketBaseIssue()
    issue['kind'] = 'bug'
    return issue


@pytest.fixture
def gitbucketEnhancementIssue():
    issue = gitbucketBaseIssue()
    issue['labels'] = ['enhancement']
    return issue


@pytest.fixture
def bitbucketEnhancementIssue():
    issue = bitbucketBaseIssue()
    issue['kind'] = 'enhancement'
    return issue


@pytest.fixture
def gitbucketProposalIssue():
    issue = gitbucketBaseIssue()
    issue['labels'] = ['proposal']
    return issue


@pytest.fixture
def bitbucketProposalIssue():
    issue = bitbucketBaseIssue()
    issue['kind'] = 'proposal'
    return issue


@pytest.fixture
def gitbucketNewIssue():
    issue = gitbucketBaseIssue()
    issue['labels'] = 'new'
    return issue


@pytest.fixture
def bitbucketNewIssue():
    issue = bitbucketBaseIssue()
    issue['status'] = 'new'
    return issue


@pytest.fixture
def gitbucketOpenedIssue():
    issue = gitbucketBaseIssue()
    issue['labels'] = 'open'
    return issue


@pytest.fixture
def bitbucketOpenedIssue():
    issue = bitbucketBaseIssue()
    issue['status'] = 'open'
    return issue


@pytest.fixture
def gitbucketResolvedIssue():
    issue = gitbucketBaseIssue()
    issue['labels'] = 'resolved'
    return issue


@pytest.fixture
def bitbucketResolvedIssue():
    issue = bitbucketBaseIssue()
    issue['status'] = 'resolved'
    return issue


@pytest.fixture
def gitbucketOnHoldIssue():
    issue = gitbucketBaseIssue()
    issue['labels'] = 'on hold'
    return issue


@pytest.fixture
def bitbucketOnHoldIssue():
    issue = bitbucketBaseIssue()
    issue['status'] = 'on hold'
    return issue


@pytest.fixture
def gitbucketInvalidIssue():
    issue = gitbucketBaseIssue()
    issue['labels'] = 'invalid'
    return issue


@pytest.fixture
def bitbucketInvalidIssue():
    issue = bitbucketBaseIssue()
    issue['status'] = 'invalid'
    return issue


@pytest.fixture
def gitbucketDuplicatedIssue():
    issue = gitbucketBaseIssue()
    issue['labels'] = 'duplicate'
    return issue


@pytest.fixture
def bitbucketDuplicatedIssue():
    issue = bitbucketBaseIssue()
    issue['status'] = 'duplicate'
    return issue


@pytest.fixture
def gitbucketWontfixIssue():
    issue = gitbucketBaseIssue()
    issue['labels'] = 'wontfix'
    return issue


@pytest.fixture
def bitbucketWontfixIssue():
    issue = bitbucketBaseIssue()
    issue['status'] = 'wontfix'
    return issue


@pytest.fixture
def gitbucketClosedIssue():
    issue = gitbucketBaseIssue()
    issue['state'] = 'closed'
    return issue


@pytest.fixture
def bitbucketClosedIssue():
    issue = bitbucketBaseIssue()
    issue['status'] = 'resolved'
    return issue


def test_convert_normalIssue(emptyIdConverter, gitbucketIssue, bitbucketIssue):
    actual = convert(gitbucketIssue, emptyIdConverter)
    assert actual == bitbucketIssue


def test_convert_bugIssue(emptyIdConverter, gitbucketBugIssue, bitbucketBugIssue):
    actual = convert(gitbucketBugIssue, emptyIdConverter)
    assert actual == bitbucketBugIssue


def test_convert_enhancementIssue(emptyIdConverter, gitbucketEnhancementIssue, bitbucketEnhancementIssue):
    actual = convert(gitbucketEnhancementIssue, emptyIdConverter)
    assert actual == bitbucketEnhancementIssue


def test_convert_proposalIssue(emptyIdConverter, gitbucketProposalIssue, bitbucketProposalIssue):
    actual = convert(gitbucketProposalIssue, emptyIdConverter)
    assert actual == bitbucketProposalIssue


def test_convert_NewIssue(emptyIdConverter, gitbucketNewIssue, bitbucketNewIssue):
    actual = convert(gitbucketNewIssue, emptyIdConverter)
    assert actual == bitbucketNewIssue


def test_convert_OpenedIssue(emptyIdConverter, gitbucketOpenedIssue, bitbucketOpenedIssue):
    actual = convert(gitbucketOpenedIssue, emptyIdConverter)
    assert actual == bitbucketOpenedIssue


def test_convert_ResolvedIssue(emptyIdConverter, gitbucketResolvedIssue, bitbucketResolvedIssue):
    actual = convert(gitbucketResolvedIssue, emptyIdConverter)
    assert actual == bitbucketResolvedIssue


def test_convert_OnHoldIssue(emptyIdConverter, gitbucketOnHoldIssue, bitbucketOnHoldIssue):
    actual = convert(gitbucketOnHoldIssue, emptyIdConverter)
    assert actual == bitbucketOnHoldIssue


def test_convert_InvalidIssue(emptyIdConverter, gitbucketInvalidIssue, bitbucketInvalidIssue):
    actual = convert(gitbucketInvalidIssue, emptyIdConverter)
    assert actual == bitbucketInvalidIssue


def test_convert_DuplicatedIssue(emptyIdConverter, gitbucketDuplicatedIssue, bitbucketDuplicatedIssue):
    actual = convert(gitbucketDuplicatedIssue, emptyIdConverter)
    assert actual == bitbucketDuplicatedIssue


def test_convert_WontfixIssue(emptyIdConverter, gitbucketWontfixIssue, bitbucketWontfixIssue):
    actual = convert(gitbucketWontfixIssue, emptyIdConverter)
    assert actual == bitbucketWontfixIssue


def test_convert_ClosedIssue(emptyIdConverter, gitbucketClosedIssue, bitbucketClosedIssue):
    actual = convert(gitbucketClosedIssue, emptyIdConverter)
    assert actual == bitbucketClosedIssue
