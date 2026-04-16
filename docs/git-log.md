# git log

`git log` displays the commit history of a repository.

## Syntax

```bash
git log [options]
```

## Common Usage

```bash
# Show full commit history
git log

# Compact one-line format
git log --oneline

# Show last N commits
git log -5

# Show history with a visual branch graph
git log --oneline --graph --all

# Show commits by a specific author
git log --author="John"

# Show commits between two dates
git log --after="2024-01-01" --before="2024-06-01"

# Show commits that changed a specific file
git log -- filename.txt

# Show full diff for each commit
git log -p
```

## Common Format Options

```bash
# Show condensed stats (files changed, insertions, deletions)
git log --stat

# Custom format
git log --pretty=format:"%h - %an - %s"
```
