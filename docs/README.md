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

## term.io API

### public variables
these are public so that you can access them if you must.

```Terminal.cursor_location``` 
* the current location of the cursor. 
<br>

```Terminal.fileno```
* the POSIX file descriptor. **DO NOT EDIT!**
<br>

```Terminal.attribs```
* the POSIX terminal attributes. 
<br>

### public methods

```Terminal.move_cursor([y1,x,y2])```
* this sets ```Terminal.cursor_location``` to the array given.
<br>

```Terminal.echo("string")```
* this is an improved and much more advanced version of ```print()``` 
<br>

```Terminal.readlines()```
* uses ```Terminal.fileno``` to read stdin.
<br>

```Terminal.getch()```
* uses ```Terminal.fileno``` to read ch*1.
<br>

```Terminal.flush_all()```
* uses ```Terminal.fileno``` to flush i/o streams
<br>

```Terminal.flush_inp()```
* uses ```Terminal.fileno``` to flush input streams
<br>

```Terminal.flush_out()```
* uses ```Terminal.fileno``` to flush output streams
<br>

```Terminal.reset_settings()```
* resets all POSIX settings to default.
<br>

```Terminal.getattribs()```
* uses ```Terminal.fileno``` to read POSIX attributes.
<br>

```Terminal.setattribs(now=True)```
* uses ```Terminal.fileno``` to set the POSIX attributes to the
  current file descriptor. ```now``` decides when it is done. 
<br>

### public ASCII codes
term.io supports 32 ASCII VT-220 color codes. these codes
can be accessed:
```python
term.fg.*foreground-color*
term.bg.*background-color*
term.dec.*decoration*
```
