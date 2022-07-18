from subprocess import Popen, PIPE
from sys import executable
p = Popen([executable, "merger.py"],stdin=PIPE)

p.stdin.write('y')
