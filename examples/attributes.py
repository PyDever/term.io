
from termio import Terminal
import sys

term = Terminal() # grab a terminal controller

# grab the current attribute settings
old_settings = term.get_attributes()

# refresh settings by creating a new file descriptor/fileno
term.fileno = sys.stdin.fileno() # this line must happen so that
# calling update_attributes() uses a new file descriptor/fileno
term.update_attributes(old_settings)

# clean up the i/o stream
term.flushio()
term.reset()

term.echo("hello, term.io!")

