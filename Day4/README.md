# Day 4 — Git, GitHub CLI, and This Repository

## Lesson goal

This is a presenter-ready lesson that uses the entire `Python_intro`
repository as the live example. Students will move the repository from a local
folder to GitHub, then practice the complete collaboration workflow.

By the end, students should be able to:

- explain the difference between Git and GitHub;
- authenticate and work with GitHub through the `gh` command;
- initialize a repository and understand its three local areas;
- inspect, stage, and commit changes;
- create a GitHub repository from local code with `gh repo create`;
- download a GitHub repository with `gh repo clone`;
- create and switch branches;
- open, review, update, and merge a pull request;
- fetch and pull collaborators' work;
- resolve a merge conflict without losing either person's intent; and
- use a few safe recovery commands.

Estimated teaching time: 2.5–3 hours, including practice.

> **Instructor preparation:** Replace every placeholder such as `YOUR-USERNAME`
> with the real GitHub account or organization. Do not paste passwords or
> personal access tokens into commands, files, commits, or screenshots.

---

## Lesson plan

| Time | Topic | Result |
| ---: | --- | --- |
| 15 min | Git and GitHub concepts | Students understand the mental model |
| 25 min | Initialize and make the first commit | A local history exists |
| 20 min | Create the GitHub repository and push | Local and remote are connected |
| 25 min | Everyday commit workflow | Students make a focused commit |
| 35 min | Branch and pull request | A reviewed change reaches `main` |
| 35 min | Deliberate merge conflict | Students resolve and test it |
| 15 min | Clone, pull, recovery, recap | Students can continue safely |

## Before class

Each student needs:

- Git installed (`git --version`);
- GitHub CLI installed (`gh --version`);
- a GitHub account;
- a terminal and text editor; and
- this `Python_intro` folder.

Confirm the Day 4 program and tests work before Git is introduced:

```bash
python Day4/team_greeting.py
python -m unittest discover -s Day4 -p "test_*.py" -v
```

Confirm GitHub CLI is installed and authenticate before presenting:

```bash
gh --version
gh auth status
gh auth login
```

Run `gh auth login` only when `gh auth status` says no account is authenticated.
Follow the interactive prompts to choose the GitHub host, connection protocol,
and browser-based sign-in. Never paste a credential into lesson files, Git
commands, commits, or screenshots.

---

## 1. Git is not GitHub

**Git** is version-control software on the computer. It records snapshots,
compares changes, creates branches, and combines work. Git can work offline.

**GitHub** is an online service that hosts Git repositories and adds
collaboration tools such as pull requests, reviews, issues, and permissions.

**GitHub CLI (`gh`)** is a terminal interface to GitHub. In this lesson it
creates and clones repositories and manages pull requests. It complements Git;
it does not replace Git's `add`, `commit`, `pull`, or `push` commands.

A useful classroom analogy:

- the working tree is the work on the desk;
- the staging area is the selection placed into an envelope;
- a commit is a labeled, sealed envelope in local history; and
- a push sends local envelopes to the shared GitHub repository.

```text
working files --git add--> staging area --git commit--> local history
                                                        |
                                                     git push
                                                        v
                                                  GitHub remote
```

Presenter question: “Does saving a file create a commit?” The answer is no.
Saving changes the working file; Git records nothing until the change is staged
and committed.

### Essential vocabulary

| Term | Meaning |
| --- | --- |
| Repository | A project and its Git history |
| Commit | A named snapshot with an author and parent commit |
| Branch | A movable name pointing to a line of commits |
| `main` | The conventional default branch |
| Remote | A saved address for another copy of the repository |
| `origin` | The conventional name of the primary remote |
| Push | Send local commits to a remote |
| Fetch | Download remote information without merging it |
| Pull | Fetch, then integrate remote work into the current branch |
| Pull request | A proposal to review and merge one branch into another |
| Merge conflict | A place where Git needs a human to choose the final content |

---

## 2. Initialize and inspect the repository

Open a terminal in the `Python_intro` folder, then initialize Git and name the
initial branch `main`:

```bash
pwd
ls
git init -b main
git status
```

If an older Git installation does not support `-b`, use:

```bash
git init
git branch -M main
```

Ask students to inspect the untracked files shown by `git status`. They should
notice that Git sees more than source code, including the local virtual
environment directories, Python cache files, and the `Day3/output/` directory.

Presenter question: “Should every file inside a project folder be committed?”
The answer is no. Program output, local environments, editor settings, and
secrets do not belong in the repository.

### Create `.gitignore` as a class exercise

Create a new file named `.gitignore` in the repository root using the editor.
Begin with one rule:

```gitignore
py_into/
```

Run `git status` again and ask students what disappeared. Add the remaining
rules gradually, checking the result after each section:

```gitignore
# Local Python virtual environments
py_into/
py_intro/
.venv/
venv/

# Python cache and compiled files
__pycache__/
*.py[cod]

# Files created by the Day 3 demonstration
Day3/output/

# Editor and operating-system files
.vscode/
.idea/
.DS_Store
Thumbs.db
```

Teaching points:

- A trailing `/` matches a directory.
- `*` is a wildcard; `*.py[cod]` matches `.pyc`, `.pyo`, and `.pyd` files.
- A line beginning with `#` is a comment.
- Rules are normally written relative to the repository root.
- `.gitignore` itself should be committed so every collaborator shares the
  same rules.
- Ignore rules affect untracked files. They do not automatically remove files
  that Git already tracks.

Confirm which rule ignores each path:

```bash
git status
git check-ignore -v py_into
git check-ignore -v Day3/output/transparency_demo.png
```

Optional safety check for large or sensitive files:

```bash
find . -type f -size +10M -not -path "./.git/*"
```

Explain before continuing: Git history is durable. Secrets and private data
should be excluded before the first commit, not “deleted later” and assumed
gone.

---

## 3. Create the first commit

Configure the author identity only if Git asks for it:

```bash
git config --global user.name "Your Name"
git config --global user.email "YOUR-EMAIL"
```

For an email address shown on GitHub commits, students may use the private
GitHub-provided `noreply` address from their GitHub email settings.

### Stage the first snapshot

```bash
git status
git add .
git status
git diff --staged
```

Teaching point: `git add .` is reasonable for this reviewed first snapshot. In
daily work, naming files explicitly makes accidental commits less likely:

```bash
git add Day4/team_greeting.py Day4/test_team_greeting.py
```

Create the commit:

```bash
git commit -m "chore: add Python course materials"
git log --oneline --decorate --graph
```

A good commit is focused, works, and has a message that completes the sentence
“If applied, this commit will …”. Examples:

- `docs: add Git branching lesson`
- `feat: greet students by name`
- `fix: handle an empty student name`
- `test: cover whitespace-only names`

---

## 4. Create the GitHub repository with `gh`

First confirm which account is authenticated:

```bash
gh auth status
```

From the repository root, create a public GitHub repository from the current
directory, name its Git remote `origin`, and push the local commits:

```bash
gh repo create Python_intro --source=. --public --remote=origin --push
```

Use `--private` instead of `--public` when the repository should not be public.
For an organization-owned repository, use `ORGANIZATION/Python_intro` as the
name.

Explain each argument before running it:

| Argument | Purpose |
| --- | --- |
| `Python_intro` | Name of the new GitHub repository |
| `--source=.` | Use the current local repository as the source |
| `--public` | Set repository visibility; `--private` is the alternative |
| `--remote=origin` | Save the created GitHub repository as remote `origin` |
| `--push` | Push the existing local commits after creation |

This one command performs the GitHub-side creation plus the remote setup and
initial push that would otherwise require several browser and Git steps.

For a prompt-driven classroom demonstration, use this instead:

```bash
gh repo create
```

Choose **Push an existing local repository to GitHub**, select the current
directory, choose the owner/name and visibility, and confirm that `gh` should
add a remote and push the commits.

Inspect the result from the terminal:

```bash
git remote -v
gh repo view
```

Optionally open the new repository page:

```bash
gh repo view --web
```

Presenter note: authentication is separate from Git commit authorship.
`gh auth login` authorizes GitHub operations, while `git config user.name` and
`user.email` identify the author recorded in commits.

---

## 5. The everyday edit–commit–push loop

Make a small documentation change, then inspect it:

```bash
git status
git diff
```

Run the relevant check before recording the change:

```bash
python -m unittest discover -s Day4 -p "test_*.py" -v
```

Stage, review, commit, and push:

```bash
git add Day4/README.md
git diff --staged
git commit -m "docs: clarify the daily Git workflow"
git push
```

The two diff commands answer different questions:

- `git diff`: what changed but is not staged?
- `git diff --staged`: what exactly will the next commit contain?

Instructor habit to model repeatedly: run `git status` between steps. It is a
description of the current state and often tells the user what to do next.

---

## 6. Branches

Never use a shared `main` branch as a scratchpad. Start new work from an updated
`main`:

```bash
git switch main
git pull --ff-only
git switch -c feature/friendly-message
```

`git switch -c` creates a branch and switches to it. Confirm the result:

```bash
git branch
git status
```

Edit `WELCOME_MESSAGE` in `Day4/team_greeting.py`:

```python
WELCOME_MESSAGE = "Welcome to the Python course — we are glad you are here!"
```

Then test and commit:

```bash
python -m unittest discover -s Day4 -p "test_*.py" -v
git diff
git add Day4/team_greeting.py
git commit -m "feat: make the course welcome more friendly"
git push -u origin feature/friendly-message
```

The branch now exists both locally and on GitHub. `main` has not changed.

---

## 7. Create and review a pull request with `gh`

A pull request asks to merge a **compare/head branch** into a **base branch**.
For this lesson:

```text
feature/friendly-message  --->  main
        compare/head              base
```

Create the pull request interactively from the feature branch:

```bash
gh pr create --base main
```

GitHub CLI prompts for the title and body, then prints the new pull request's
URL. The current branch is the compare/head branch, and `--base main` states
where the change should be merged.

To supply the content without prompts:

```bash
gh pr create \
  --base main \
  --title "feat: make the course welcome more friendly" \
  --body "Makes the greeting warmer. Tested with the Day 4 unittest suite."
```

Suggested description:

```markdown
## What changed

- Made the course greeting warmer.

## How I tested it

- Ran the Day 4 unittest suite.
```

Inspect the pull request from the terminal:

```bash
gh pr view
gh pr diff
gh pr checks
```

Use `gh pr view --web` when you want to present GitHub's Conversation, Commits,
and Files changed tabs visually:

- **Conversation**: context, discussion, approvals, and checks;
- **Commits**: the snapshots proposed by the branch; and
- **Files changed**: the combined diff reviewers must inspect.

If review requests a change, edit the same local branch, test, commit, and
push. The existing pull request updates automatically:

```bash
git add Day4/team_greeting.py
git commit -m "docs: address greeting review feedback"
git push
```

After approval and passing checks, merge the current branch's pull request.
Leaving the merge strategy flag out lets `gh` prompt for a permitted strategy:

```bash
gh pr merge --delete-branch
```

The option deletes the feature branch after merging; its commits remain in
repository history.

Synchronize locally:

```bash
git switch main
git pull --ff-only
git branch -d feature/friendly-message
```

`-d` refuses to delete a branch Git believes is unmerged, making it safer than
the force form `-D`.

---

## 8. Deliberate merge-conflict exercise

This exercise deliberately makes two branches change the same line. Do it only
after the first repository push.

### A. Create two branches from the same starting commit

```bash
git switch main
git pull --ff-only
git switch -c feature/formal-message
git switch main
git switch -c feature/friendly-message
```

Both feature branches now point to the same starting commit.

### B. Finish and merge the friendly branch

On `feature/friendly-message`, set the line to:

```python
WELCOME_MESSAGE = "Welcome! We are glad you joined the Python course."
```

Then:

```bash
python -m unittest discover -s Day4 -p "test_*.py" -v
git add Day4/team_greeting.py
git commit -m "feat: add a friendly welcome message"
git push -u origin feature/friendly-message
```

Create and merge its pull request with GitHub CLI:

```bash
gh pr create --base main --fill
gh pr view --web
gh pr merge --delete-branch
```

### C. Make a competing change on the older formal branch

Switch to the branch that still points to the earlier version:

```bash
git switch feature/formal-message
```

Set the same line to a different value:

```python
WELCOME_MESSAGE = "Welcome to the official Python training program."
```

Then:

```bash
python -m unittest discover -s Day4 -p "test_*.py" -v
git add Day4/team_greeting.py
git commit -m "feat: use a formal welcome message"
git push -u origin feature/formal-message
```

Open a second pull request into `main`:

```bash
gh pr create --base main --fill
gh pr view
```

GitHub should report that the branches cannot be merged automatically because
both changed `WELCOME_MESSAGE` from the same original line.

### D. Resolve the conflict locally

Download remote information and merge the current remote `main` into the
formal branch:

```bash
git fetch origin
git merge origin/main
git status
```

The file will contain markers similar to these:

```python
<<<<<<< HEAD
WELCOME_MESSAGE = "Welcome to the official Python training program."
=======
WELCOME_MESSAGE = "Welcome! We are glad you joined the Python course."
>>>>>>> origin/main
```

The markers mean:

- `<<<<<<< HEAD` begins the current branch's version;
- `=======` separates the two versions; and
- `>>>>>>> origin/main` ends the incoming version.

Git is not asking which person is right. It is asking what the final file
should say. Discuss the intent, edit the file into one valid result, and delete
all three marker lines. For example, combine the ideas:

```python
WELCOME_MESSAGE = "Welcome to the official Python course — we are glad you joined!"
```

Verify, mark the conflict resolved, commit, and update the PR branch:

```bash
python -m unittest discover -s Day4 -p "test_*.py" -v
git add Day4/team_greeting.py
git status
git commit -m "merge: resolve welcome message conflict"
git push
```

Refresh the pull request. The conflict should be gone and the combined result
should be visible in **Files changed**. Review it before merging.

If the class needs to abandon the in-progress merge before committing it:

```bash
git merge --abort
```

That returns the working tree to its pre-merge state. It is an exit route, not
a way to resolve and keep the merge.

---

## 9. Clone and update repositories

A new collaborator downloads the repository and its history with GitHub CLI:

```bash
gh repo clone KhalylDammas/Python_intro
cd Python_intro
git remote -v
git log --oneline --all --graph --decorate
```

`gh repo clone` accepts the concise `OWNER/REPOSITORY` form and uses the
authenticated account's configured Git protocol. A GitHub URL also works.

### “Clone” and “pull” are different

- `gh repo clone OWNER/REPOSITORY` downloads a repository for the first time.
- `git pull --ff-only` updates a repository that is already on the computer.

There is no `gh repo pull` command for updating the working copy. That remains
a Git operation because it changes local Git history and working files.

Before starting each new task:

```bash
git switch main
git pull --ff-only
git switch -c feature/short-description
```

`git fetch` updates remote-tracking names such as `origin/main` without changing
working files. `git pull --ff-only` fetches and updates the current branch only
when no merge commit is required, which makes unexpected divergence visible.

When a contributor cannot push branches to the original repository, they can
fork it, push the branch to their fork, and open a PR from that fork into the
original repository.

---

## 10. Safe recovery commands

Use these after explaining exactly which area each command changes:

| Situation | Command | Effect |
| --- | --- | --- |
| See the current state | `git status` | Changes nothing |
| Inspect unstaged edits | `git diff` | Changes nothing |
| Inspect staged edits | `git diff --staged` | Changes nothing |
| Unstage a file | `git restore --staged FILE` | Keeps the working edit |
| Discard an uncommitted file edit | `git restore FILE` | Destructive to that edit |
| Stop an unfinished merge | `git merge --abort` | Restores the pre-merge state |
| Undo a shared commit | `git revert COMMIT` | Adds a new inverse commit |
| Inspect all branches | `git log --oneline --all --graph --decorate` | Changes nothing |

Never demonstrate `git reset --hard`, forced push, or deleting `.git` as a
casual fix. Those commands can remove work or rewrite shared history.

---

## Student practice tasks

1. Create `feature/course-duration` from an updated `main`.
2. Add a `COURSE_DAYS = 4` constant to `team_greeting.py` and include it in the
   displayed message.
3. Add or update a unit test for the behavior.
4. Run the tests, inspect both diffs, and create a focused commit.
5. Push the branch and open a pull request with `gh pr create --base main`.
6. Exchange PR reviews with another student. Request one concrete improvement.
7. Address the comment with a second commit, push, and merge after approval.
8. Update local `main` and safely delete the merged local branch.

## Pull-request review checklist

- Does the title explain the outcome?
- Does the description explain why the change exists?
- Is the PR limited to one purpose?
- Is any private data, credential, output file, or virtual environment added?
- Does the code behave correctly, including edge cases?
- Are tests present and passing?
- Are names and comments understandable to another developer?
- Has the author handled review feedback?

## Final review questions

- What does `git add` do, and what does it not do?
- Why inspect `git diff --staged` before committing?
- What is the relationship among `main`, a feature branch, and a PR?
- How are `fetch`, `pull`, and `push` different?
- Why can Git merge most changes automatically?
- What do the three conflict markers mean?
- Why should secrets never be committed, even briefly?

## Command cheat sheet

```bash
gh auth status                          # Show authenticated GitHub account
gh repo create NAME --source=. --public --remote=origin --push
gh repo clone OWNER/REPOSITORY          # Download a repository for first use
gh repo view                            # Show current GitHub repository
gh pr create --base main                # Open a pull request interactively
gh pr view                              # Show the current branch's PR
gh pr diff                              # Show the PR's combined changes
gh pr checks                            # Show automated check results
gh pr merge --delete-branch             # Merge and clean up the feature branch
git status                              # Explain the current state
git diff                                # Show unstaged changes
git diff --staged                       # Show the next commit's content
git add FILE                            # Stage a file
git commit -m "type: useful message"    # Record a local snapshot
git log --oneline --graph --decorate    # Show compact history
git switch main                         # Change branches
git switch -c feature/name              # Create and switch branch
git fetch origin                        # Download remote information
git pull --ff-only                      # Safely update current branch
git push -u origin BRANCH               # First push and set upstream
git push                                # Later push to the upstream
git merge origin/main                   # Merge current remote main locally
git merge --abort                       # Abandon an unfinished merge
```

## Official references

- [GitHub CLI manual](https://cli.github.com/manual/)
- [`gh repo create`](https://cli.github.com/manual/gh_repo_create)
- [`gh repo clone`](https://cli.github.com/manual/gh_repo_clone)
- [`gh pr create`](https://cli.github.com/manual/gh_pr_create)
- [`gh pr merge`](https://cli.github.com/manual/gh_pr_merge)
- [Creating a new repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)
- [Adding locally hosted code to GitHub](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)
- [Pull request quickstart](https://docs.github.com/en/pull-requests/get-started/pull-request-quickstart)
- [Creating a pull request](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request)
- [Resolving a merge conflict on the command line](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/resolving-a-merge-conflict-using-the-command-line)
- [Git command reference](https://git-scm.com/docs)
