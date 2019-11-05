from lib.models import argumentParser as parser
from lib.models import gitbucketApi
from lib.utils import writeData

args = parser.parse()
gitbucket = gitbucketApi.GitbucketApi(
    args.gitbucket_endpoint,
    args.gitbucket_owner,
    args.gitbucket_repo,
    args.gitbucket_token
)

issues = sorted(gitbucket.getAllIssues(), key=lambda x: x['number'])  # チケット番号でソート
writeData.writeData(f'./data/gitbucket_issues_{args.gitbucket_owner}-{args.gitbucket_repo}.json', issues)
