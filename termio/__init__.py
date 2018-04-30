
import sys
import os
import termios
import tty
import fcntl

class foreground_colors:
      black = "\u001b[30m"
      red = "\u001b[31m"
      green = "\u001b[32m"
      yellow = "\u001b[33m"
      blue = "\u001b[34m"
      magenta = "\u001b[35m"
      cyan = "\u001b[36m"
      white = "\u001b[37m"
      bblack = "\u001b[30;1m"
      bred = "\u001b[31;1m"
      bgreen = "\u001b[32;1m"
      byellow = "\u001b[33;1m"
      bblue = "\u001b[34;1m"
      bmagenta = "\u001b[35;1m"
      bcyan = "\u001b[36;1m"
      bwhite = "\u001b[37;1m"
      reset = "\u001b[0m"

class background_colors:
      black = "\u001b[40m"
      red = "\u001b[41m"
      green = "\u001b[42m"
      yellow = "\u001b[43m"
      blue = "\u001b[44m"
      magenta = "\u001b[45m"
      cyan = "\u001b[46m"
      white = "\u001b[47m"
      bblack = "\u001b[40;1m"
      bred = "\u001b[41;1m"
      bgreen = "\u001b[42;1m"
      byellow = "\u001b[43;1m"
      bblue = "\u001b[44;1m"
      bmagenta = "\u001b[45;1m"
      bcyan = "\u001b[46;1m"
      bwhite = "\u001b[47;1m"
      reset = "\u001b[0m"

class decorations:
      bold = "\u001b[1m"
      underline = "\u001b[4m"
      reverse = "\u001b[7m"
      reset = "\u001b[0m"


class Terminal (object):

    def __init__ (self):

        # get the UNIX/POSIX file descriptor
        self.fileno = sys.stdin.fileno()

        # store the where the cursor is supposed to be
        self.cursor_location = [0,0,1]

        # store the ansi color codes
        self.fg = foreground_colors
        self.bg = background_colors
        self.dec = decorations

        # store the ansi sequences
        self.ansi_codes = {}

        self.ansi_codes['clear-screen'] = "\x1b[2J\x1b[H"
        self.ansi_codes['move-cursor'] = "\x1b[#;#H\x1b[H"


    """ implement the private API """

    def __get_attributes (self):
        attributes = termios.tcgetattr(self.fileno)
        return attributes

    def __set_attributes_now (self, settings_):
        termios.tcsetattr(self.fileno, termios.TCSANOW,
            settings_)

    def __flush_input_stream (self):
        termios.tcflush(self.fileno(), termios.TCIFLUSH)

    def __flush_output_stream (self):
        termios.tcflush(self.fileno, termios.TCOFLUSH)

    def __flush_io_stream (self):
        termios.tcflush(self.fileno, termios.TCIOFLUSH)

    def __flush_sys_io_stream (self):
        sys.stdout.flush(); sys.stdin.flush()

    def __reset (self):
        # reset colors 
        sys.stdout.write("\u001b[0m")
        # flush all streams
        self.__flush_io_stream()
        self.__flush_sys_io_stream()
        self.__change_cursor_location([0,0,1])

    def __destroy_fileno (self):
        self.fileno = None 

    def __set_fileno (self, fd):
        self.fileno = fd

    def __clear_terminal_screen (self):
        sys.stderr.write(self.ansi_codes['clear-screen'])

    def __enable_system_output (self, enable):
        new_rules = self.__get_attributes()
        if enable:
             new_rules[3] |= termios.ECHO
        else:
            new_rules[3] &= ~termios.ECHO
        self.__set_attributes()

    def __read_input_stream (self):
        try:
            sys.stdin.readlines()
        except KeyboardInterrupt:
            self.__echo("KeyboardInterrupt detected.")

    def __read_one_character (self):
        fd = self.fileno
        old_settings = self.__get_attributes()
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def __change_cursor_location (self, location_x_y):
        self.cursor_location = location_x_y

    def __echo (self, string):

        sys.stdout.write("\n"*self.cursor_location[1])

        sys.stdout.write("    "*self.cursor_location[0]+str(string))
        sys.stdout.write("\n"*self.cursor_location[2])

    """ implement the private API wrapper, or public methods """
    def get_attributes(self):
        return self.__get_attributes()

    def update_attributes(self, settings_):
        self.__set_attributes_now(settings_)

    def flushio (self):
        self.__flush_sys_io_stream()
        self.__flush_io_stream()

    def flushin (self):
        self.__flush_input_stream()

    def reset (self):
        self.__reset()

    def flushout (self):
        self.__flush_output_stream()

    def clear (self):
        self.__clear_terminal_screen()

    def read_raw (self):
        return self.__read_input_stream()

    def read (self, prompt):
        bytes_x = 0
        try:
            bytes_x = input(
                "\n"*self.cursor_location[1] + "    "*self.cursor_location[0]
                + str(prompt) + "\n"*self.cursor_location[2]
            )
        except KeyboardInterrupt:
            self.__echo("KeyboardInterrupt detected.")
        return bytes_x

    def getch (self):
        return self.__read_one_character()

    def move (self, loc):
        self.__change_cursor_location(loc)

    def echo (self, string):
        self.__echo(string)







