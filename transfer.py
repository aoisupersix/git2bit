import argparse

parser = argparse.ArgumentParser(description='transfer your gitbucket issues to bitbucket.')
parser.add_argument('-ge', '--gitbucket_endpoint', required=True)
parser.add_argument('-go', '--gitbucket_owner', required=True)
parser.add_argument('-gr', '--gitbucket_repo', required=True)
parser.add_argument('-gt', '--gitbucket_token', required=True)
parser.add_argument('-be', '--bitbucket_endpoint', default='https://api.bitbucket.org/2.0')
parser.add_argument('-bo', '--bitbucket_owner', required=True)
parser.add_argument('-br', '--bitbucket_repo', required=True)
parser.add_argument('-bt', '--bitbucket_token', required=True)

args = parser.parse_args()
print(args)
