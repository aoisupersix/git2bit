import json
import os

from lib.models import argumentParser as parser
from lib.models import gitbucketApi

args = parser.parse()
gitbucket = gitbucketApi.GitbucketApi(
    args.gitbucket_endpoint,
    args.gitbucket_owner,
    args.gitbucket_repo,
    args.gitbucket_token
)

issues = sorted(gitbucket.getAllIssues(), key=lambda x: x['number'])  # チケット番号でソート

# 特に使い道はないけど後で確認したいとき用に取得したデータを保存しておく
os.makedirs('./data', exist_ok=True)
f = open(f'./data/gitbucket_issues_{args.gitbucket_owner}-{args.gitbucket_repo}.json', 'w')
json.dump(issues, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
f.close()
