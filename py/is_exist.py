import os
import subprocess

myfile = os.getenv('GITHUB_ENV')
with open(env_file, "r") as myfile:
    eo_lib_version = myfile.getenv('eo_lib_version')
branch_name = "update-" + eo_lib_version

command = f'git rev-parse --verify {branch_name}'
result = subprocess.run(command, shell=True, capture_output=True)
is_exist = result.returncode == 0
with open(env_file, "a") as myfile:
    myfile.write(f'is_exist={is_exist}')
print(f'Added to env: {is_exist}')