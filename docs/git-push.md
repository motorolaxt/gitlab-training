# git push

`git push` uploads local commits from your current branch to a remote repository.

## Syntax

```bash
git push <remote> <branch>
```

## Common Usage

```bash
# Push to the default remote (origin) on the main branch
git push origin main

# Push and set upstream tracking (first push of a new branch)
git push -u origin feature-branch

# Push all local branches
git push --all origin

# Push tags
git push --tags

# Force push (overwrites remote history — use with caution)
git push --force origin main
```

## Key Concepts

- **remote** — the destination repository, typically called `origin`
- **upstream** — the remote branch your local branch tracks, set with `-u` on first push
- **force push** — rewrites remote history, dangerous on shared branches

## Notes

- `git push` only transfers committed changes — uncommitted work stays local
- On shared branches, prefer `--force-with-lease` over `--force` as it won't overwrite changes others have pushed
- If the remote branch has commits your local doesn't, push will be rejected — run `git pull` first

## See Also

`git pull`, `git fetch`, `git remote`
