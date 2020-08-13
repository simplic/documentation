import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--git-token', help='Your GitHub access token')
parser.add_argument('--ftp-user', help='The ftp username')
parser.add_argument('--ftp-pass', help='The ftp password')
args = vars(parser.parse_args())
print(args)

print(args['--git-token'] == '***')
print(args['--git-token'] == 'heyhey'
