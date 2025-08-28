#! /usr/bin/env python3
# vim:fenc=utf-8
# Copyright © 2025 nylander <johan.nylander@nrm.se>
# Distributed under terms of the MIT license.
# Last modified: tor aug 28, 2025  04:38

"""
Search https://github.com/Naturhistoriska for public repositories.
Print the results as a markdown formatted list to stdout.
Documentation on the GitHub API: https://docs.github.com/en/rest
"""

import sys
import requests

PUBLIC_REPOS_URL = 'https://api.github.com/orgs/Naturhistoriska/repos?type=public'
response = requests.get(PUBLIC_REPOS_URL)
response_list = response.json()

# Debug printing of available keys (key => value)
#fk = response_list[0]
#[print(f"{k} => {fk[k]}", file=sys.stderr) for k in fk.keys()]

# Markdown output
print("## Public repositories\n", file=sys.stdout)
for x in sorted(response_list, key=lambda x: x['name'].lower()):
    if x['description'] is None:
        DESCR = '(No description)'
    else:
        DESCR = x['description']
    print(f"- [{x['name']}]({x['html_url']}): {DESCR}", file=sys.stdout)
