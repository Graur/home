import os
import json
import subprocess

env_file = os.getenv('GITHUB_ENV')
env_data = json.loads(env_file)
eo_lib_version = env_data.get('eo_lib_version')
branch_name = "update-" + eo_lib_version

command = f'git rev-parse --verify {branch_name}'
result = subprocess.run(command, shell=True, capture_output=True)
is_exist = result.returncode == 0
with open(env_file, "a") as myfile:
    myfile.write(f'is_exist={is_exist}')
print(f'Added to env: {is_exist}')