from functions.general import (
    save_json,
    load_json
)

class LocationBase:
    def __init__(self, name: str):
        self.name = name
        self.information = ""
        self.persons = []
        self.notes = []

    def set_information(self, info: str):
        self.information = info

    def reindex_notes(self):
        for i, note in enumerate(self.notes, start=1):
            note["id"] = i

    def delete_notes(self, note_id: int):
        self.notes = [n for n in self.notes if n["id"] != note_id]
        self.reindex_notes()

    def add_note(self, note: str):
        note_id = len(self.notes) + 1
        self.notes.append({"id": note_id, "note": note})

class City(LocationBase):
    def __init__(self, name: str):
        super().__init__(name)
        self.shops = []
        self.poi = []

    def add_poi(self, poi_name: str):
        self.poi.append(poi_name)

    def add_shop(self, shop_name: str):
        self.shops.append(shop_name)

    def to_dict(self):
        return {
            "City": self.name,
            "Information": self.information,
            "Places of Interest": self.poi,
            "Shops": self.shops,
            "Persons of Interest": [p.to_dict() for p in self.persons],
            "Notes": self.notes
        }

class PointOfInterest(LocationBase):
    def __init__(self, name: str):
        super().__init__(name)
        self.theme = ""
        self.effects = []

    def set_theme(self, theme: str):
        self.theme = theme

    def add_effect(self, effect: str):
        self.effects.append(effect)

    def to_dict(self):
        return {
            "Point of Interest": self.name,
            "Information": self.information,
            "Theme": self.theme,
            "Effects": self.effects,
            "Persons of Interest": [p.to_dict() for p in self.persons],
            "Notes": self.notes
        }

class Region:
    def __init__(self, name: str):
        self.name = name
        self.cities = []
        self.poi = []
        self.notes = []

    @staticmethod
    def delete(name: str):
        data = load_json("regions.json")
        del data[name]
        save_json("regions.json", data)

    @classmethod
    def load_from_file(cls, name: str):
        data = load_json("regions.json")

        if name not in data:
            return None

        region_data = data[name]
        region = cls(name)

        region.notes = region_data.get("Notes", [])
        for city_data in region_data.get("Cities", []):
            city = City(city_data["City"])
            city.information = city_data.get("Information", "")
            city.poi = city_data.get("Places of Interest", [])
            city.shops = city_data.get("Shops", [])
            city.notes = city_data.get("Notes", [])
            region.add_city(city)

        for poi_data in region_data.get("POI", []):
            poi = PointOfInterest(poi_data["Point of Interest"])
            poi.information = poi_data.get("Information", "")
            poi.theme = poi_data.get("Theme", "")
            poi.effects = poi_data.get("Effects", [])
            poi.notes = poi_data.get("Notes", [])
            region.add_poi(poi)
        return region

    def add_city(self, city: City):
        if not isinstance(city, City):
            raise TypeError("Expected City Instance")
        self.cities.append(city)

    def add_poi(self, poi: PointOfInterest):
        if not isinstance(poi, PointOfInterest):
            raise TypeError("Expected POI Instance")
        self.poi.append(poi)

    def delete_city(self, city_name: str):
        self.cities = [c for c in self.cities if c.name != city_name]
        self.save_to_file()

    def delete_poi(self, poi_name: str):
        self.poi = [p for p in self.poi if p.name != poi_name]
        self.save_to_file()

    def add_note(self, note: str):
        note_id = len(self.notes) + 1
        self.notes.append({"id": note_id, "note": note})
        self.save_to_file()

    def reindex_notes(self):
        for i, note in enumerate(self.notes, start=1):
            note["id"] = i

    def delete_note(self, note_to_delete: int):
        self.notes = [n for n in self.notes if int(n["id"]) != note_to_delete]
        self.reindex_notes()
        self.save_to_file()

    def to_dict(self):
        return {
            "Region": self.name,
            "Cities": [c.to_dict() for c in self.cities],
            "POI": [p.to_dict() for p in self.poi],
            "Notes": self.notes
        }

    def save_to_file(self):
        data = load_json("regions.json")
        data[self.name] = self.to_dict()
        save_json("regions.json", data)