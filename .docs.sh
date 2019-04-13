#!/bin/bash

# Exit on fail
if [ "$TRAVIS_BRANCH" == "master" -a "$TRAVIS_PULL_REQUEST" == "false" -a "$GEN_DOC" == "yes" ]; then
  REMOTE="https://${GH_TOKEN}@github.com/comwes/mkpdfs-mkdocs-plugin"

  # Set configuration for repository and deploy documentation
  git config --global user.name "${GH_NAME}"
  git config --global user.email "${GH_EMAIL}"
  git remote set-url origin ${REMOTE}
  sudo apt-get update
  sudo apt-get install -y build-essential libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info

  # Build documentation with overrides and publish to GitHub pages
  mkdocs gh-deploy --force
fi
