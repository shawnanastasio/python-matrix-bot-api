"""
Defines a matrix bot handler for commands
"""
import re

from matrix_bot_api.mhandler import MHandler


class MCommandHandler(MHandler):

    # command  - String of command to handle
    # handle_callback - Function to call if message contains command
    # cmd_char - Character that denotes a command. '!' by default
    def __init__(self, command, handle_callback, cmd_char='!'):
        MHandler.__init__(self, self.test_command, handle_callback)
        self.command = command
        self.cmd_char = cmd_char

    # Function called by Matrix bot api to determine whether or not to handle this message
    def test_command(self, room, event):
        # Test the message to see if it has our command
        if event['type'] == "m.room.message":
            if re.match(self.cmd_char + self.command, event['content']['body']):
                return True
        return False
