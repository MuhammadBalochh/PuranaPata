class Plugin:
    def __init__(self, args):
        self.args = args

    def execute(self):
        """
        This method will be executed when the plugin is called.
        The logic of the plugin should be implemented here.
        """
        raise NotImplementedError("Each plugin must implement the execute method.")
