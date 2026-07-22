import re
import os
import subprocess

def run_git(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True)
    except Exception as e:
        pass

os.chdir(r"C:\Users\ishan\Documents\Projects\Awesome-Blockchain-Based-Prediction-Markets")

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

# Task 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 are essentially the same as in update.py, so let's just use update.py content but strip run_cmd and run our own run_git without push.
with open('update.py', 'r', encoding='utf-8') as f:
    update_code = f.read()

update_code = update_code.replace("def run_cmd(cmd):", "def run_cmd(cmd):\n    cmd = cmd.split('&& git push')[0]\n    cmd = cmd.split('; git push')[0]\n    try:\n        subprocess.run(cmd, shell=True, check=True)\n    except:\n        pass\n    return")
update_code = update_code.replace("run_cmd('git add . && git commit", "run_cmd('git add . ; git commit")

with open('update2.py', 'w', encoding='utf-8') as f:
    f.write(update_code)
