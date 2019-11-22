from lib.models.gitbucket_api import GitbucketApi


def test_2():
    # TODO
    api = GitbucketApi('', '', '', '')
    assert api.baseUrl == ''
