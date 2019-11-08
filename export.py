from lib.models import argument_parser as parser
from lib.models import GitbucketApi
from lib.utils import write_data

args = parser.parse()
gitbucket = GitbucketApi(
    args.gitbucket_endpoint,
    args.gitbucket_owner,
    args.gitbucket_repo,
    args.gitbucket_token
)

issues = sorted(gitbucket.getAllIssues(), key=lambda x: x['number'])  # チケット番号でソート
write_data.writeData(f'gitbucket_issues_{args.gitbucket_owner}-{args.gitbucket_repo}.json', issues)

issueNos = [issue['number'] for issue in issues]
comments = gitbucket.getIssuesComments(issueNos)
write_data.writeData(f'gitbucket_comments_{args.gitbucket_owner}-{args.gitbucket_repo}.json', comments)

labels = gitbucket.getLabels()
write_data.writeData(f'gitbucket_labels_{args.gitbucket_owner}-{args.gitbucket_repo}.json', labels)
