# test-repo

This is a testing ground for building a Python project with all of the bells and whistles of a build pipeline using GitHub Actions.

![GitHub License](https://img.shields.io/github/license/paullockaby/test-repo)
![GitHub Release](https://img.shields.io/github/v/release/paullockaby/test-repo)
![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fpaullockaby%2Ftest-repo%2Fmain%2Fpyproject.toml)
[![Merge Pipelines](https://github.com/paullockaby/test-repo/actions/workflows/merge.yaml/badge.svg)](https://github.com/paullockaby/test-repo/actions/workflows/merge.yaml)

[![Mastodon Follow](https://img.shields.io/mastodon/follow/106882571030731815?domain=https%3A%2F%2Funcontrollablegas.com)](https://uncontrollablegas.com/@paul)

## Table of contents

* [Introduction](#introduction)
* [Installation](#installation)
* [Quick start](#quick-start)
* [Usage](#usage)
* [Known issues and limitations](#known-issues-and-limitations)
* [Getting help](#getting-help)
* [Contributing](#contributing)
* [License](#license)
* [Acknowledgments](#acknowledgments)

## Introduction

This is a test repository for seeing how GitHub Actions work.

To make this kinda work, first you'll want to generate a deploy key for the repository, like this:

```
ssh-keygen -t ed25519 -C commitizen -f deploy_key -P ""
```

This will create two files: `deploy_key` and `deploy_key.pub`. **DO NOT COMMIT THESE.** Save them off somewhere for future reference. Take the `deploy_key.pub` file and add it as a deploy key to the repo and make sure that it has write access. Take the private key, aka the non `.pub` file, and create a secret called `DEPLOY_KEY` in the repo. This will be used by commitizen to push commits with the changelog to the `main` branch.

Then set up some branch rules. These will only work on public repos. Or, if you have paid for a pro or team plan or enterprise plan, then it will work on private repos, too.

The rule that we're going to create is will look like this:

* Ruleset Name: default
* Enforcement status: Active
* Bypass list: deploy keys
* Target branches: Default
* Rules: uncheck everything except these:
  * Restrict deletions
  * Require a pull request before merging
    * Required approvals: your call but if you're a solo developer set it to zero
    * Dismiss stale pull request approvals when new commits are pushed
    * Require review from Code Owners
  * Require status checks to pass
    * Require branches to be up to date before merging
    * Status checks that are required:
      * `tests / pre-commit` - GitHub Actions
      * `tests / test` - GitHub Actions
  * Block force pushes

Create the above rule, the above deploy key, and tweak the jobs to your liking, to run the lints, and tests, and builds that you want and you're on your way. What's next?

Well, this should be what you do next:

1. Install pre-commit hooks: `make pre-commit`
2. Make changes in branches only and commit them using convential commit messages. Make sure that the SUBJECT LINE of the pull request describes what the pull request does because that's the only thing that will appear in the changelog.
3. When you're ready to make a release, go to GitHub Actions tab and choose "Create Releases" and then click "Run workflow" and run the workflow against the `main` branch. You'll see, based on your commit messages, an update to CHANGELOG.md, a new tag, a release, and whatever you put into the `release-build.yaml` action.

## Installation

TODO

## Quick start

TODO

## Usage

TODO

## Known issues and limitations

TODO

## Getting help

TODO

## Contributing

TODO

## License

TODO

## Acknowledgements

I took the format for this README file from [Michael Hucka's READMINE repository](https://github.com/mhucka/readmine).
