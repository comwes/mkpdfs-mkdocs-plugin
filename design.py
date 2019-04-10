import os
import sys

from npm.bindings import npm_install, npm_run

wd = os.getcwd()

dir = os.path.dirname(os.path.realpath(__file__))
npm_install('{}/mkpdfs_mkdocs/design'.format(dir))
os.chdir('{}/mkpdfs_mkdocs/design'.format(dir))
stderr, stdout = npm_run('run', 'build-css')
if stderr :
    sys.exit(stderr)
print(stdout)
os.chdir(wd)
