"""
Defines a matrix bot handler for commands
"""
import re

from matrix_bot_api.mhandler import MHandler

class MCommandHandler(MHandler):
    # The first word after a bot mention will be interpreted as a command
    # For example, if the bot is named testbot, a user would call the command
    # echo by saying the following:
    #  testbot: echo hello
    #
    # username - Bot's username
    # command  - String of command to handle
    # handle_callback - Function to call if message contains command
    def __init__(self, username, command, handle_callback):
        MHandler.__init__(self, self.test_command, handle_callback)
        self.username = username
        self.command = command

    # Function called by Matrix bot api to determine whether or not to handle this message
    def test_command(self, room, event):
        # Test the message and see if we were mentioned
        if event['type'] == "m.room.message":
            if re.match(self.username, event['content']['body']):
                # The message matches the regex, see if it contains the command
                args = event['content']['body'].split()
                if args[1] == self.command:
                    return True
        return False
