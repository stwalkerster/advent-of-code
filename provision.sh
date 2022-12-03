#!/bin/bash
# Quick script called from cron to create the new day's puzzle directory and download the data automatically

cp -a template $(date +day%d)

# run `pip3 install advent-of-code-data` to install aocd binary
~/.local/bin/aocd > $(date +day%d)/input.txt


