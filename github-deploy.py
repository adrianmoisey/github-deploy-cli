#!/usr/bin/env python

import os
import github3

# required
token = os.getenv('GITHUB_TOKEN')
user = os.getenv('GITHUB_USER')
repo = os.getenv('GITHUB_REPO')
branch = os.getenv('GITHUB_BRANCH')

environment = os.getenv('GITHUB_DEPLOYMENT_ENVIRONMENT')
action = os.getenv('GITHUB_DEPLOYMENT_ACTION', 'create')
deployment_id = os.getenv('GITHUB_DEPLOYMENT_ID', None)
url = os.getenv('GITHUB_DEPLOYMENT_URL', None)

gh = github3.login(token=token)
repo = gh.repository(user, repo)


def create_deployment(branch, environment, url=False, auto_merge=True):
    deployment = repo.create_deployment(
        branch,
        auto_merge=auto_merge,
        environment=environment)
    if url:
        deployment.create_status('pending', target_url=url)
    return(deployment.id)


def update_deployment(action, deploymet_id):
    deployment = repo.deployment(deployment_id)
    deployment.create_status(action)


if __name__ == '__main__':
    if action == 'create':
        print(create_deployment(branch, environment, url))
    if action == 'success' and deployment_id is not None:
        update_deployment(action, deployment_id)
