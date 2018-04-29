
import socket, termio

terminal = termio.Terminal()

old_settings = terminal.get_attributes()
terminal.update_attributes(old_settings)

serverSocket = socket.socket(socket.AF_INET,
    socket.SOCK_STREAM)
    
terminal.flushio()
terminal.reset()
    
serverSocket.bind(('localhost', 3000))
terminal.echo(term.fg.bblue + "[server] bound the port." + term.fg.reset)

serverSocket.listen(5)

while (True):
    conn, addr = serverSocket.accept()
    try:
        data = conn.recv(1024)
        terminal.echo("[server] received %s" % data)
    except socket.error or terminal.error:
        terminal.echo(term.fg.red+"[server] error." + term.fg.reset)
        
