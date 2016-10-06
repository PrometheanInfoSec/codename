#!/usr/bin/env python
import linecache
import random
import subprocess
import sys

dicti = "/usr/share/dict/words"

len = subprocess.check_output("wc -l %s" % dicti, shell=True).split()[0]

lines = []
lines.append(random.randint(0, int(len)))
lines.append(random.randint(0, int(len)))

for line in lines:
	sys.stdout.write( linecache.getline(dicti, line).strip("\n") + " ")

print


