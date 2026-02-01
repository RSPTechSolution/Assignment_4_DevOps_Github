# SSH Key Setup

1. I generated an SSH key using the ssh-keygen command with an email comment.
2. I added the generated public key to my GitHub account under.

Settings → SSH and GPG keys.

3. To verify whether the SSH connection was working, I ran the following command:

```

ssh -T git@github.com

At this stage, the connection was not successful.

```

4. To resolve the issue, I added a host configuration for GitHub in the SSH config file:

```

~/.ssh/config

This configuration explicitly specifies which SSH key should be used for GitHub.

```

5. After updating the SSH configuration, I re-ran the verification command:

```

ssh -T git@github.com

```

6. This time, the connection was successful, confirming that the SSH key is correctly configured and GitHub authentication is working.

# Git Workflow

* Configured the SSH key on my system to enable secure authentication with GitHub.
* Cloned the project repository using the SSH URL.
* Created a new branch named Subodh using **git checkout -b Subodh** and switched to it immediately.
* Added my Flask project files to the newly created branch.
* Staged all project files using **git add .**
* Committed the changes with a proper commit message using **git commit -m**.
* Pushed the committed changes to the remote repository using **git push**.
* Created a .gitignore file to exclude unnecessary files from version control.
* Added the .venv directory to **.gitignore** to prevent the virtual environment from being tracked.
