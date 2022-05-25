import sys

sys.path.insert(0,'/var/www/hello-world-app')

activate_this = '/var/www/hello-world-app/.venv/bin/activate_this.py'

with open(activate_this) as file:
	
	exec(file.read(), dict(__file__=activate_this))

from app import app as application
