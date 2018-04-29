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

## basic API
```Terminal.clear()```
<br>
* clear the screen



