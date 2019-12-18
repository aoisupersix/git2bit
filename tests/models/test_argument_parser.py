from pytest_mock.plugin import MockFixture

from lib.models.argument_parser import parse


def test_parse_RequiredArguments(mocker: MockFixture):
    argv = [
        'exec/commandline',
        '--gitbucket_endpoint=endpoint',
        '--gitbucket_owner=owner',
        '--gitbucket_repo=repo',
        '--gitbucket_token=token'
    ]
    mocker.patch('sys.argv', argv)
    args = parse()

    assert len(vars(args)) == 5
    assert args.gitbucket_endpoint == 'endpoint'
    assert args.gitbucket_owner == 'owner'
    assert args.gitbucket_repo == 'repo'
    assert args.gitbucket_token == 'token'
    assert args.mapping is None
