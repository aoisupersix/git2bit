from lib.models import argument_parser as parser
from lib.models import gitbucket_api
from lib.utils import write_data

args = parser.parse()
gitbucket = gitbucket_api.GitbucketApi(
    args.gitbucket_endpoint,
    args.gitbucket_owner,
    args.gitbucket_repo,
    args.gitbucket_token
)

issues = sorted(gitbucket.getAllIssues(), key=lambda x: x['number'])  # チケット番号でソート
write_data.writeData(f'./data/gitbucket_issues_{args.gitbucket_owner}-{args.gitbucket_repo}.json', issues)
