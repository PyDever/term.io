# Hello, term.io!
term.io has an API that is more simple than curses or termios. check 
out this simple program that makes you type one char and makes
it in the middle of the screen and in yellow!

```python
from termio import Terminal

# create a new controller
term = Terminal()

# flush the i/o stream
term.flush_all()

# store your char
char = term.getch()

term.move_cursor([4,4,4])
term.echo(
    term.fg.yellow + char 
    + term.fg.reset
)

```
