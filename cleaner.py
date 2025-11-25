# This script will take a folder of files as input and output a combined cleaned csv file.

import sys, os

def dict_to_str(value: dict) -> str:
    return ";".join([f'{k}:{v}' for k, v in value.items()])

def read_file(filename: str) -> str:
    with open(filename, "r") as file:
        return file.read()

def write_file(filename: str, text: str) -> None:
    with open(filename, "w+") as file:
        file.write(text)

class DataPoint:
    def __init__(self,
            participant_group: str = None,
            participant_name: str = None,
            session_id: str = None,
            block_name: str = None,
            trial_name: str = None,
            event_name: str = None,
            cumulative_time: str = None,
            participant_response: str = None,
            key: str = None,
            pressed_or_released: str = None,
            correct_response: str = None,
            reaction_time: str = None,
            error_code: str = None,
            p_or_b: str = None) -> None:
        self.participant_group: str = participant_group
        self.participant_name: str = participant_name
        self.session_id: str = session_id
        self.block_name: str = block_name
        self.trial_name: str = trial_name
        self.event_name: str = event_name
        self.cumulative_time: str = cumulative_time
        self.participant_response: str = participant_response
        self.key: str = key
        self.pressed_or_released: str = pressed_or_released
        self.correct_response: str = correct_response
        self.error_code: str = error_code
        self.reaction_time: str = reaction_time
        self.p_or_b: str = p_or_b

    def from_str(text: str) -> DataPoint:
        splits: list[str] = text.split("\t")

        if len(splits) < 14:
            return None

        return DataPoint(*splits)

    def __repr__(self) -> str:
        return dict_to_str(self.__dict__)

    def create_dataset(path: str) -> list[DataPoint]:
        dataset: list[DataPoint] = []

        if os.path.isdir(path):
            for member in os.listdir(path):
                dataset += DataPoint.create_dataset(f"{path}/{member}")

            return dataset

        text: str = read_file(path)
    
        for line in text.split("\n")[9:]:
            dataset.append(DataPoint.from_str(line))

        dataset = filter(lambda x: x is not None, dataset)

        return dataset

    def generate_csv(dataset: list[DataPoint]) -> str:
        lines: list[str] = [
            "Participant Group,Participant Name,Session ID,Block Name,Trial Name,Event Name,Cumulative Time,Participant Response,Key,Pressed Or Released,Correct Response,Error Code,Reaction Time,P or B"
        ]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        quit()

    dataset: list[DataPoint] = []

    for arg in sys.argv[1:]:
        dataset += DataPoint.create_dataset(arg)

    print(len(dataset))
    print(dataset[0])
