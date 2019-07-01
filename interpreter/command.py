class Command:
    'A base class for use by all commands. Interpreted by the CommandInterpreter'

    def __init__(self, library):
        self.library = library 

    def execute(self, player, arguments):
        pass

# End Command

class CommandInterpreter:
    'A simple command interpreter that parses the players input.'

    def __init__(self, player, library):
        self.player = player
        self.library = library 

    def interpret(self, input):
        if not input:
            return

        tokens = input.split(' ', 1)

        command = tokens[0].lower()
        arguments = tokens[1]

        command_object = self.library.getCommand(command)
        if command_object:
            command_object.execute(self.player, arguments)
        else:
            player.write("I don't think you can do that...")

# End CommandInterpreter