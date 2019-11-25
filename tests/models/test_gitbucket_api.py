from lib.models.gitbucket_api import GitbucketApi


def test_getIssuesPerPage_RequestParameters(mocker):
    requests = mocker.MagicMock(**{
        'return_value.ok': True,
        'return_value.json.return_value': {}
    })

    mocker.patch('requests.get', requests)
    GitbucketApi('endpoint', 'owner', 'repo', 'token').getIssuesPerPage(1)
    issues_endpoint, optional_args = requests.call_args

    # Check Request Header
    assert 'headers' in optional_args
    header = optional_args['headers']
    assert header['Authorization'] == 'token token'
    assert header['content-type'] == 'application/json'

    assert 'params' in optional_args
    payload = optional_args['params']
    assert payload['page'] == 1
    assert payload['state'] == 'open'

    assert issues_endpoint[0] == 'endpoint/api/v3/repos/owner/repo/issues'
    assert header['Authorization'] == 'token token'
    assert header['content-type'] == 'application/json'
