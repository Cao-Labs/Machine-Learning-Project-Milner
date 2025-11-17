# This script will take a folder of files as input and output a combined cleaned csv file.

class DataPoint:
    def __init__(self) -> None:
        self.group_id: str = None
        self.participant_id: str = None
        self.response_correct: bool = None
        self.response_name: str = None
        self.response_rt: int = None
        self.stimuli_presented: str = None
        self.trial_template: str = None
        self.trial_duration: int = None
        self.next = None

def readFile(filename: str) -> str:
    pass

def getData(text: str) -> DataPoint:
    pass


