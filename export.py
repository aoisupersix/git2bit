import json
import zipfile

from lib.models import argument_parser as parser
from lib.models import GitbucketApi
from lib.models import IdConverter
from lib.models import bitbucket_converter
from lib.utils import writeData


def export():
    """Execute convert gitbucket -> bitbucket
    """
    args = parser.parse()
    gitbucket = GitbucketApi(
        args.gitbucket_endpoint,
        args.gitbucket_owner,
        args.gitbucket_repo,
        args.gitbucket_token
    )

    idConverter = IdConverter()
    if (args.mapping is not None):
        idConverter.loadMappingFromFilePath(args.mappingFilePath)

    issues = sorted(gitbucket.getAllIssues(), key=lambda x: x['number'])  # チケット番号でソート
    writeData(f'gitbucket_issues_{args.gitbucket_owner}-{args.gitbucket_repo}.json', issues)

    issueNos = [issue['number'] for issue in issues]
    comments = gitbucket.getIssuesComments(issueNos)
    writeData(f'gitbucket_comments_{args.gitbucket_owner}-{args.gitbucket_repo}.json', comments)

    labels = gitbucket.getLabels()
    writeData(f'gitbucket_labels_{args.gitbucket_owner}-{args.gitbucket_repo}.json', labels)

    export = bitbucket_converter.convert(issues, comments, idConverter)

    with zipfile.ZipFile(f'{args.gitbucket_repo}-issues.zip', 'w', compression=zipfile.ZIP_DEFLATED) as zip:
        zip.writestr(
            'db-2.0.json',
            json.dumps(export, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': ')))


if __name__ == '__main__':
    export()
