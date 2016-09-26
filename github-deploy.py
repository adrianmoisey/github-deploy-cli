#!/usr/bin/env python

import os
import github3

# required
token = os.getenv('GITHUB_TOKEN')
user = os.getenv('GITHUB_USER')
repo = os.getenv('GITHUB_REPO')
branch = os.getenv('GITHUB_BRANCH')

environment = os.getenv('GITHUB_ENVIRONMENT')
action = os.getenv('GITHUB_ACTION', 'create_deployment')
deployment = os.getenv('GITHUB_DEPLOYMENT_ID', None)
url = os.getenv('GITHUB_DEPLOYMENT_URL', None)

gh = github3.login(token=token)
repo = gh.repository(user, repo)

if action == 'create_deployment':
    deployment = repo.create_deployment(
        branch,
        auto_merge=True,
        environment=environment)
    if url:
        deployment.create_status('pending', target_url=url)
    print(deployment.id)

if action == 'successful_deployment' and deployment is not None:
    deployment = repo.deployment(deployment)
    deployment.create_status('success')
