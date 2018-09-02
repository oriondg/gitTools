## Git Tools

This script is meant to be used by build machines, or during the process of building to incorporate the status of the containing git repository into the versioning. A good example of use would be CI builds being triggered by pushes to develop that need to be versioned in some meaningful way.

Usage:
```
gitVersion.py <command>
```

Commands:
```
branch
count
fullversion
hash
url
version
```

# branch

prints the name of the current branch

# count

prints a count of revision lists, useful for a "build" version. Can collide with other version if used as the sole specifier

# fullversion

prints the "full" version, which puts together the other data you can fetch with this tool into a single version name

# hash

prints the short hash of the HEAD

# url

prints the URL of the repo. This is useful for distinguishing between forks

# version

prints the version number. This should be implemented specifically for your needs. Some teams use a JSON file while others will use text files, tags, or other means of establishing version.
