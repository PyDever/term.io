# term.io documentation
term.io has a very contained and robust API. 

## hello, term.io!
lets scratch the surface of term.io!
```python
import termio

term = termio.Terminal()

# move the cursor to the middle
term.move([2,2,2])

# push text to the screen in yellow
term.echo(term.fg.yellow + 
    "hello, term.io!" + term.fg.reset)
```
pretty nifty, right? lets underline it!
```python

# push text to the screen in underlined yellow
term.echo(term.fg.yellow + term.dec.underline + 
    "hello, term.io!" + term.fg.reset)
```
cool beans! lets try to get some user input. how about
just one character for now.
```python
# move the cursor to the middle
term.move([2,2,2])

# get one character
char = term.getch()

# push text to the screen in yellow
term.echo(term.fg.yellow + 
    str(char) + term.fg.reset)
```
nice! lets try normal input.
```python
# move the cursor to the middle
term.move([2,2,2])

# get some text
name = term.read()

# push text to the screen
term.echo("hello, %s" % name)
```
neat! lets refresh terminal settings!
```python
old_settings = term.get_attributes()

term.fileno = sys.stdin.fileno()
term.update_attributes(old_settings)
```

## basic API
```Terminal.clear()```
* clear the screen
<br>

```Terminal.reset()```
* reset colors and cursor position
<br>

```Terminal.move([y1,x,y2])```
* move the cursor to the given array
<br>

```Terminal.echo(string_and_colors)```
* print the string along with any color settings
<br>

```Terminal.read()```
* read in some bytes from the user
<br>

## low-level API
```Terminal.get_attributes()```
* retrieve the attributes currently in place
<br>

```Terminal.update_attributes()```
* update the attributes to the most recent ***fd*** call
<br>

```Terminal.flushio()```
* flush the standard i/o stream
<br>

```Terminal.read_raw()```
* bare bones bytes grabber
<br>

```Terminal.fileno```
* POSIX-style file descriptor
<br>

```Terminal.cursor_position```
* stores the current position of the cursor
<br>

```Terminal.ansi_codes```
* stores the ansi codes relating to cursor movement and i/o
<br>

## term.io server
now that you are familiar with the term.io low-level API, go ahead
and build a TCP server that only uses term.io control operations!

there is a completed one in the `examples` folder.



