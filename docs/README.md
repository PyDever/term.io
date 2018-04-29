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
