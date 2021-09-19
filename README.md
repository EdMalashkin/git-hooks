# Create git hooks to standardize commit and code
    
Three git hooks, namely **pre-commit**, **commit-msg**, **pre-push** are
created to standardize the commit and code in this repo.
    
**pre-commit**: This hook is run before every commit is created. It stops
developers from creating commits in the master/main branch directly. Besides,
it also checks if the Python code is formatted properly with black, which
formats Python code according to PEP8.
    
**commit-msg**: This hook checks the commit message entered by the author.
If the exit status is 0, the commit message will be aborted. In this
repo, the exit status of this hook is always 0, even if there are
errors or warnings. The purpose is to keep the commit message the author
has entered and not discard it due to style issues. The author can modify the
commit message according to the hints of this hook.
    
**pre-push**: This hook is run before commits are pushed to the remote
repository. It stops developers pushing to the master/main branch directly.
Besides, it also does unit tests. If the unit tests fail, the push will be
aborted.
