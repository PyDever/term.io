# Hello, term.io!
term.io has an API that is more simple than curses or termios. check 
out this simple program that takes your input and makes
it in the middle of the screen and in yellow!

```python
from termio import Terminal

# create a new controller
term = Terminal()

# flush the output stream
term.flush_out()

term.move_cursor([4,4,4])
term.echo(
    term.fg.yellow + "hello, world!" 
    + term.fg.reset
)

```
