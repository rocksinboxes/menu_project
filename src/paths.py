import os
class paths:
    def __init__(self) -> None:
        self.login=os.getlogin()
        self.home_path=os.path.expanduser('~')
