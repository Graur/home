
import os

env_file = os.getenv('GITHUB_ENV')

with open(env_file, "a") as myfile:
    myfile.write("MESSAGE=eo-strings:0.0.1")