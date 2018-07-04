import os
import subprocess

ROOT = "./www/artists"

<<<<<<< HEAD
total = 0

with open("./build/spelling_allowed.txt") as fobj:
    allowed = fobj.read().split("\n")

most = {}

=======
>>>>>>> 91d448720177b76273187e922dc63ed32e71f840
for artist in filter(lambda x: os.path.isdir(os.path.join(ROOT, x)), os.listdir(ROOT)):
    for dir in os.walk(os.path.join(ROOT, artist)):
        for file in dir[2]:
            if not file.endswith(".html"): continue
            path = os.path.join(dir[0], file)
            errors = subprocess.getoutput("cat {} | aspell -a -H".format(path)).split("\n")[1:]
            for line in errors:
                if line.strip() in ["*", ""]: continue
<<<<<<< HEAD
                word = line.strip().split(" ")[1]
                if word in allowed: continue
                print(path, line.split(":")[0])
                total += 1
                if word in most:
                    most[word] += 1
                else:
                    most[word] = 1

for spelling in sorted(most.items(), key=lambda x: x[1]):
    print(spelling)

print(total, "total errors")
=======
                print(path, line.split(":")[0])
>>>>>>> 91d448720177b76273187e922dc63ed32e71f840
