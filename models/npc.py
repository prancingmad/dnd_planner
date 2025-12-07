from functions.general import (
    save_json,
    load_json
)

class PersonOfInterest:
    def __init__(self, name: str):
        self.name = name
        self.info = []
        self.notes = []

    def add_info(self, info: str):
        self.info.append(info)

    def add_notes(self, note: str):
        self.notes.append(note)

    def to_dict(self):
        return {
            "Person": self.name,
            "Info": self.info,
            "Notes": self.notes
        }