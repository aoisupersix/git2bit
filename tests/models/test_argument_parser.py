import pytest
from pytest_mock.plugin import MockFixture

from lib.models.argument_parser import parse, removeTrailingSlash


@pytest.fixture
def argv():
    argument = [
        'exec/commandline',
        '--api-endpoint=endpoint',
        '--owner=owner',
        '--repo=repo',
        '--token=token'
    ]

    return argument


def test_parse_RequiredArguments(mocker: MockFixture, argv: list):
    mocker.patch('sys.argv', argv)
    args = parse()

    assert len(vars(args)) == 7
    assert args.api_endpoint == 'endpoint'
    assert args.owner == 'owner'
    assert args.repo == 'repo'
    assert args.token == 'token'
    assert args.mapping is None
    assert args.output is None
    assert args.write_apiresponse is False


def test_parse_OptionalArguments(mocker: MockFixture, argv: list):
    argv.append('--mapping=mapping')
    argv.append('--output=output')
    argv.append('--write-apiresponse')
    mocker.patch('sys.argv', argv)
    args = parse()

    assert len(vars(args)) == 7
    assert args.api_endpoint == 'endpoint'
    assert args.owner == 'owner'
    assert args.repo == 'repo'
    assert args.token == 'token'
    assert args.mapping == 'mapping'
    assert args.output == 'output'
    assert args.write_apiresponse


def test_removeTrailingSlash_Removing():
    assert removeTrailingSlash('abc/def/') == 'abc/def'


def test_removeTrailingSlash_NotRemoving():
    assert removeTrailingSlash('abc/def') == 'abc/def'
