import json
import zipfile

from lib.models import argument_parser as parser
from lib.models import GitbucketApi
from lib.models import IdConverter
from lib.models import bitbucket_converter
from lib.utils import writeTmpFile


def export():
    """Execute convert gitbucket -> bitbucket
    """
    args = parser.parse()
    gitbucket = GitbucketApi(
        args.api_endpoint,
        args.owner,
        args.repo,
        args.token
    )

    idConverter = IdConverter()
    if (args.mapping is not None):
        idConverter.loadMappingFromFilePath(args.mappingFilePath)

    issueResult = gitbucket.getIssueResult()
    writeTmpFile(f'gitbucket_issues_{args.owner}-{args.repo}.json', issueResult.issueSummaries)
    writeTmpFile(f'gitbucket_comments_{args.owner}-{args.repo}.json', issueResult.comments)
    writeTmpFile(f'gitbucket_labels_{args.owner}-{args.repo}.json', issueResult.labels)

    export = bitbucket_converter.convert(issueResult.issueSummaries, issueResult.comments, idConverter)

    with zipfile.ZipFile(f'{args.repo}-issues.zip', 'w', compression=zipfile.ZIP_DEFLATED) as zip:
        zip.writestr(
            'db-2.0.json',
            json.dumps(export, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': ')))


if __name__ == '__main__':
    export()
