#!/usr/bin/env python

import os
import github3

# required
token = os.getenv('GITHUB_TOKEN')
user = os.getenv('GITHUB_USER')
repo_name = os.getenv('GITHUB_REPO')
branch = os.getenv('GITHUB_BRANCH')

environment = os.getenv('GITHUB_DEPLOYMENT_ENVIRONMENT')
action = os.getenv('GITHUB_DEPLOYMENT_ACTION', 'create')
deployment_id = os.getenv('GITHUB_DEPLOYMENT_ID', None)
url = os.getenv('GITHUB_DEPLOYMENT_URL', None)

def repo(token, user, repo_name):
    gh = github3.login(token=token)
    return gh.repository(user, repo_name)

def create_deployment(repo, branch, environment, url=False, auto_merge=True):
    deployment = repo.create_deployment(
        branch,
        auto_merge=auto_merge,
        environment=environment)
    if url:
        deployment.create_status('pending', target_url=url)
    return(deployment.id)


def update_deployment(repo, action, deploymet_id):
    deployment = repo.deployment(deployment_id)
    deployment.create_status(action)


if __name__ == '__main__':
    repo = repo(token, user, repo_name)
    if action == 'create':
        print(create_deployment(repo, branch, environment, url))
    if action == 'success' and deployment_id is not None:
        update_deployment(repo, action, deployment_id)
