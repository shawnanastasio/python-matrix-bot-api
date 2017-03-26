"""
Defines a Matrix bot message handler
"""


class MHandler(object):
    # test_callback - function that takes a room and event and returns a boolean
    # indicating whether we should pass the message on to handle_callback
    #
    # handle_callback - function that takes a room and event and handles them
    def __init__(self, test_callback, handle_callback):
        self.test_callback = test_callback
        self.handle_callback = handle_callback
