from subprocess import Popen, PIPE
from sys import executable
p = Popen([executable, "/repositories/PassportQueue/manage.py makemigrations --merge"],stdin=PIPE)

p.stdin.write('y'.encode())
