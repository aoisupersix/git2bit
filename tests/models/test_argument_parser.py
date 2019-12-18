import pytest
from pytest_mock.plugin import MockFixture

from lib.models.argument_parser import parse, removeTrailingSlash


@pytest.fixture
def argv():
    argument = [
        'exec/commandline',
        '--gitbucket_endpoint=endpoint',
        '--gitbucket_owner=owner',
        '--gitbucket_repo=repo',
        '--gitbucket_token=token'
    ]

    return argument


def test_parse_RequiredArguments(mocker: MockFixture, argv: list):
    mocker.patch('sys.argv', argv)
    args = parse()

    assert len(vars(args)) == 5
    assert args.gitbucket_endpoint == 'endpoint'
    assert args.gitbucket_owner == 'owner'
    assert args.gitbucket_repo == 'repo'
    assert args.gitbucket_token == 'token'
    assert args.mapping is None


def test_parse_OptionalArguments(mocker: MockFixture, argv: list):
    argv.append('--mapping=mapping')
    mocker.patch('sys.argv', argv)
    args = parse()

    assert len(vars(args)) == 5
    assert args.gitbucket_endpoint == 'endpoint'
    assert args.gitbucket_owner == 'owner'
    assert args.gitbucket_repo == 'repo'
    assert args.gitbucket_token == 'token'
    assert args.mapping == 'mapping'


def test_removeTrailingSlash_Removing():
    assert removeTrailingSlash('abc/def/') == 'abc/def'


def test_removeTrailingSlash_NotRemoving():
    assert removeTrailingSlash('abc/def') == 'abc/def'
