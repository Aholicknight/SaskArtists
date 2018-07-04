import os
import subprocess

ROOT = "./www/artists"

for artist in filter(lambda x: os.path.isdir(os.path.join(ROOT, x)), os.listdir(ROOT)):
    for dir in os.walk(os.path.join(ROOT, artist)):
        for file in dir[2]:
            if not file.endswith(".html"): continue
            path = os.path.join(dir[0], file)
            errors = subprocess.getoutput("cat {} | aspell -a -H".format(path)).split("\n")[1:]
            for line in errors:
                if line.strip() in ["*", ""]: continue
                print(path, line.split(":")[0])
