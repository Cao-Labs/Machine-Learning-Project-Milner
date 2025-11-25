# This script will take a folder of files as input and output a combined cleaned csv file.

import sys, os

def dict_to_str(value: dict) -> str:
    return ";".join([f'{k}:{v}' for k, v in value.items()])

def read_file(filename: str) -> str:
    with open(filename) as file:
        return file.read()

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
        self.part_blocks: int = None
        self.all_blocks: int = None
        self.pattern: str = None
        self.trial_num: int = None
        self.pb: str = None
        self.final: str = None
        self.part: int = None
        self.correct: int = None
        self.invRT: float = None
        self.trial: int = None
        self.group: str = None

    def from_str(text: str) -> DataPoint:
        print(text)
        quit()

    def __repr__(self) -> str:
        return dict_to_str(self.__dict__)

    def create_dataset(path: str) -> list[DataPoint]:
        dataset: list[DataPoint] = []

        if os.path.isdir(path):
            for member in os.listdir(path):
                dataset.append(DataPoint.create_dataset(f"{path}/{member}"))

            return dataset

        text: str = read_file(path)

        for line in text.split("\n"):
            data_point: DataPoint = DataPoint.from_str(line)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        quit()

    dataset: list[DataPoint] = []

    for arg in sys.argv[1:]:
        dataset += DataPoint.create_dataset(arg)
