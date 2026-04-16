# Git Notes

## What is Git?
- Git is a version control system
- It tracks changes in your code
- It helps you collaborate with others
- It lets you go back to previous versions

## Basic Workflow
1. Make changes to files
2. git add → stage changes
3. git commit → save changes
4. git push → upload to GitHub

## Important Commands
```bash
git init → create new repo
git clone URL → copy repo
git status → check changes
git add . → stage all files
git commit -m "message" → save changes
git push → upload to GitHub
git pull → download from GitHub
git log → see commit history
git diff → see what changed
git reset → undo changes
```

## Branching
```bash
git branch → list branches
git branch name → create branch
git checkout name → switch branch
git checkout -b name → create and switch
git merge name → merge branch
git branch -d name → delete branch
```

## Common Mistakes and Fixes
- Forgot to add files → git add .
- Wrong commit message → git commit --amend
- Need to undo last commit → git reset HEAD~1
- Pushed wrong code → git revert