# Zachary Milner
# 11/25/25
# This file cleans the given data for use in machine learning. The cleaned data is given in CSV form.

import random
import sys
import os
import re

def dict_to_str(value: dict) -> str:
    """Create a string from a dictionary where key value pairs are represented with key:value, and each pair is separated by a semicolon."""
    return ";".join([f'{k}:{v}' for k, v in value.items()])

def read_file(filename: str) -> str:
    """Create a string of a file's contents, given the filename."""
    with open(filename, "r") as file:
        return file.read()

def write_file(filename: str, text: str) -> None:
    """Write a string to a file. Create the file if it does not exist."""
    with open(filename, "w+") as file:
        file.write(text)

class DataPoint:
    IGNTYPES: list[str] = [
        "instructions",
        "practice",
        "debreifing",
        "practice_instructions",
        "inverse_practice_instructions",
        "inverse_instructions"
    ]

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
            error_code: str = None,
            reaction_time: int = None,
            p_or_b: str = None) -> None:
        """Create a new DataPoint from the given data. If any elements are unspecified, they default to None."""
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
        self.reaction_time: int = int(reaction_time)
        self.p_or_b: str = p_or_b

    def from_str(text: str):
        """Create a new DataPoint from a string with elements separated by tab characters."""
        splits: list[str] = text.split("\t")

        if len(splits) < 14 or splits[3].strip().lower() in DataPoint.IGNTYPES:
            return None

        return DataPoint(*splits)

    def __repr__(self) -> str:
        return dict_to_str(self.__dict__)

    def create_dataset(path: str) -> list:
        """Create a list of DataPoints a file or directory. If a file path is given, the DataPoints will be created from the file's content. If a directory is given, the DataPoints will be created from every file and directory within the directory. This function is recursive, and will follow all folders."""
        dataset: list = []

        if os.path.isdir(path):
            for member in os.listdir(path):
                dataset += DataPoint.create_dataset(f"{path}/{member}")

            return dataset

        text: str = read_file(path)
    
        for line in text.split("\n")[9:]:
            dataset.append(DataPoint.from_str(line))

        dataset = filter(lambda x: x is not None, dataset)

        return dataset

    def generate_point(self, trial_num: int) -> str:
        """Generate a CSV line for the DataPoint with a given trial number."""
        match: re.Match = re.search(r"([^\s]*)\.wav", self.event_name)

        cons: str = self.p_or_b.lower()
        stimuli: str = ""

        if match is not None:
            stimuli: str = match.group(1)
        
        return ",".join([
            str(trial_num),
            "",
            "DispreferenceFirst",
            {
                "disfirst_reg": "dispreferenceFirst",
                "disfirst_inverse": "dispreferenceFirst_inverse"
            }[self.participant_group.lower()],
            str(-1000/self.reaction_time),
            "", "", "", "",
            str(self.reaction_time),
            stimuli,
            "",
            self.cumulative_time,
            "", "",
            "Voicing" if cons == "b" else "Devoicing",
            str(trial_num + 23),
            cons,
            "Final" if stimuli.endswith(cons) else "NonFinal",
            "", ""
        ])

    HEADER: str = ",expt_id,Group,group_id,invRT,Trial,participant_id,response_correct,response_name,response_rt,stimuli_presented,trial_template,trial_duration,PartBlocks,AllBlocks,Pattern,trial_num,PB,Final,Part,Correct"

    def generate_csv(dataset: list, ptraining: float) -> tuple[str, str]:
        """Generate a CSV file from a list of DataPoints."""
        generated: list[str] = [dataset[i].generate_point(i+1) for i in range(len(dataset))]
        random.shuffle(generated)
        split_point: int = int(len(generated) * ptraining)
        return [
            "\n".join([DataPoint.HEADER] + generated[:split_point]),
            "\n".join([DataPoint.HEADER] + generated[split_point:])
        ]

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(f"Please input in the format: python3 {__file__} <random seed> <portion training, eg. 0.7> <folder/file...>")
        quit()

    dataset: list[DataPoint] = []

    random.seed(float(sys.argv[1]))

    for arg in sys.argv[3:]:
        dataset += DataPoint.create_dataset(arg)

    training_csv, testing_csv = DataPoint.generate_csv(dataset, float(sys.argv[2]))
    write_file("cleanTraining.csv", training_csv)
    write_file("cleanTesting.csv", testing_csv)
