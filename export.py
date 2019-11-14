import json
import zipfile

from lib.models import argument_parser as parser
from lib.models import GitbucketApi
from lib.models import issue_converter
from lib.utils import writeData

args = parser.parse()
gitbucket = GitbucketApi(
    args.gitbucket_endpoint,
    args.gitbucket_owner,
    args.gitbucket_repo,
    args.gitbucket_token
)

issues = sorted(gitbucket.getAllIssues(), key=lambda x: x['number'])  # チケット番号でソート
writeData(f'gitbucket_issues_{args.gitbucket_owner}-{args.gitbucket_repo}.json', issues)

issueNos = [issue['number'] for issue in issues]
comments = gitbucket.getIssuesComments(issueNos)
writeData(f'gitbucket_comments_{args.gitbucket_owner}-{args.gitbucket_repo}.json', comments)

labels = gitbucket.getLabels()
writeData(f'gitbucket_labels_{args.gitbucket_owner}-{args.gitbucket_repo}.json', labels)

# 一旦ここで変換を試してみる
result = {
    'issues': [issue_converter.convert(issue) for issue in issues],
    'comments': [],
    'attachments': [],
    'logs': [],  # これはGitbucketのAPIからは取得できないので空
    'meta': {
        'default_assignee': None,
        'default_component': None,
        'default_kind': 'task',  # これは引数で設定できるようにしたい
        'default_milestone': None,
        'default_version': None,
    },
    'components': [],
    'milestones': [],
    'versions': [],
}

with zipfile.ZipFile(f'{args.gitbucket_repo}-issues.zip', 'w', compression=zipfile.ZIP_DEFLATED) as zip:
    zip.writestr(
        'db-2.0.json',
        json.dumps(result, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': ')))
