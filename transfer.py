from lib import argumentParser as parser
from lib import gitbucketApi

args = parser.parse()
gitbucket = gitbucketApi.GitbucketApi(
    args.gitbucket_endpoint,
    args.gitbucket_owner,
    args.gitbucket_repo,
    args.gitbucket_token
)
gitbucket.getAllIssues()
