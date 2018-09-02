import subprocess
import json
import argparse
import sys

def getCommitCount():
    result = subprocess.check_output(['git', 'rev-list', 'HEAD', '--count'])
    return result.decode('utf-8').replace('\n', '')

def getCommitShortHash():
    result = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'])
    return result.decode('utf-8').replace('\n', '')

def getVersionID():
    #implement your own code here, such as checking config files or directly the executable
    return '0.0.1'

def getFullVersionID():
    with open("PhantomConfig/phantomakeConfig_project.json", "r") as conf:
        data = json.loads(conf.read())
        return data['presets']['project']['version'] + '.' + getCommitCount()

def getBranchName():
    result = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])
    return result.decode('utf-8').replace('\n', '').replace('/', '.')

def getGitURL():
	result = subprocess.check_output(['git', 'config', '--get', 'remote.origin.url'])
	return result.decode('utf-8')

def parse_args():
    parser = argparse.ArgumentParser(description='gitVersion')
    subparsers = parser.add_subparsers(title='commands', metavar='COMMAND',
                                       description='Tool for getting git/project status')
    def show(request):
        print(request)

    bv = subparsers.add_parser('branch',
                            help='Show the current branch')
    bv.set_defaults(func=lambda a:
                    show(getBranchName()))

    url = subparsers.add_parser('url',
                            help='Show the current repo\'s URL')
    url.set_defaults(func=lambda a:
                    show(getGitURL()))

    hash = subparsers.add_parser('hash',
                            help='Show the hash of the HEAD')
    hash.set_defaults(func=lambda a:
                    show(getCommitShortHash()))

    version = subparsers.add_parser('version',
                            help='Show the version')
    version.set_defaults(func=lambda a:
                    show(getVersionID()))

    fullversion = subparsers.add_parser('fullversion',
                            help='Show the full version (phantom config version + git commit count as build version)')
    fullversion.set_defaults(func=lambda a:
                    show(getFullVersionID()))

    count = subparsers.add_parser('count',
                            help='Show the count of changelists')
    count.set_defaults(func=lambda a:
                    show(getCommitCount()))

    return parser, parser.parse_args()

def main():
    if len(sys.argv) == 1:
        version = getVersionID() + "." + getCommitCount() + "@" + getCommitShortHash()
        print(version)
        sys.exit(0)
    parser, args = parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
