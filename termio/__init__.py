
import sys, termios
import tty, fcntl, os

from getch import getch

from asciix import bg, fg, dec 

class Terminal (object):


    def __init__ (self):

        """ 
        initialization function for the termincal
        class. this function hosts basic meta
        information for terminal io
        """

        self.fileno = sys.stdin.fileno()
        self.attribs = termios.tcgetattr(
            self.fileno)

        self.cursor_location = [0,0,1]

        """ implement ASCII and ANSI codes for color control """
        self.fg = fg 
        self.bg = bg
        self.dec = dec

    """ implement a simple termios private wrapper """
    def __get_attributes__ (self, file_descriptor):
        """
        usage:
            assuming public wrapper:
                self.__get_attributes__()

        """
        attributes_and_settings = termios.tcgetattr(file_descriptor)

        return attributes_and_settings

    def __set_attributes__ (self, file_descriptor, when):
        """
        usage:
            assuming public wrapper:
                self.__set_attributes__(file_descriptor,
                    termios.TCSANOW, self.__get_attributes__())
        """
        attributes_and_settings = self.__get_attributes__(file_descriptor)

        termios.tcsetattr(file_descriptor, when, attributes_and_settings)

    def __flush_input_stream__ (self, file_descriptor):
        """
        usage:
            assuming public wrapper:
                self.__flush_input_stream__()
        """
        termios.tcflush(file_descriptor, termios.TCIFLUSH)

    def __flush_output_stream__ (self, file_descriptor):
        """
        usage:
            assuming public wrapper:
                self.__flush_output_stream__()
        """
        termios.tcflush(file_descriptor, termios.TCOFLUSH)

    def __flush_io_stream__ (self, file_descriptor):
        """
        usage:
            assuming public wrapper:
                self.__flush_io_stream__()
        """
        termios.tcflush(file_descriptor, termios.TCIOFLUSH)

    def __get_input_stream__ (self):
        """
        usage:
            assuming public wrapper:
                self.__get_input_stream__()
        """
        sys.stdin.readlines()

    def __get_one_character__ (self):
        """
        usage:
            assuming public wrapper:
                self.__get_one_character__()
        """    
        character = getch()
        return character

    def __write_string_text__ (self, string, newline = None):
        """
        usage:
            assuming public wrapper:
                self.__echo_string_text__()
        """    
        if newline != None:

            sys.stdout.write("\n"*newline + string + "\n"*newline)

        elif newline is None:
            sys.stdout.write(string)

    def __change_cursor_location__ (self, location_array):
        """ no usage case here """
        """ free private unbound """

        self.cursor_location = location_array

    def __echo__ (self, string):

        sys.stdout.write("\n"*self.cursor_location[1])

        sys.stdout.write("    "*self.cursor_location[0]+string)
        sys.stdout.write("\n"*self.cursor_location[2])

    """ implement some public methods that wrap the private API """
    """ ....................................................... """
    """ ....................................................... """

    def flush_all (self): # this public method will wrap the private one for io
        self.__flush_io_stream__(self.fileno)

        sys.stdout.flush()

        sys.stdin.flush()

    def flush_out (self):
        self.__flush_output_stream__(self.fileno)

    def flush_inp (self):
        self.__get_input_stream__(self.fileno)

    """ there is really no reason for this method """
    def getattribs (self): # this public method will wrap the private one for tcgetattr
        return self.__get_attributes__(self.fileno)

    def setattribs (self, now=True):

        if now is not None:

            if now is True and not False:

                self.__set_attributes__(self.fileno, termios.TCSANOW)

            elif now is False and not True:

                self.__set_attributes__(self.fileno, termios.TCSADRAIN)

    def readlines (self):
        try:
            self.__get_input_stream__()
        except KeyboardInterrupt:

            sys.stdout.write("Input stream halted." + "\n")

    def getch (self):
        char = self.__get_one_character__()
        return char

    def writeln (self, string, newline=None):
        if newline is not None:
            self.__write_string_text__(string, newline=newline)

        elif newline is None or False:
            self.__write_string_text__(string, newline=None)

    def echo (self, string):
        self.__echo__(string)

    def move_cursor (self, location):
        self.__change_cursor_location__(location)

    def reset_settings (self):

        self.__change_cursor_location__([0,0,1])

        self.__flush_io_stream__(self.fileno)

        self.__flush_output_stream__(self.fileno)

        self.__flush_input_stream__(self.fileno)

        sys.stdout.write("\u001b[0m")

