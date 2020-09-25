from typing import List, Optional
from enum import Enum

class ParkingLot:
    def __init__(self, num_levels, num_spots_per_lvl) -> None:
        self.levels : List[Level] = [ Level(num_spots_per_lvl) for num in range(num_levels)]
        
    # with Optional typehint, you can return None or ParkingSpot type
    def find_parking_spot(self, incoming_vehicle:Vehicle) -> Optional[ParkingSpot]:
        # Find list of free/available spots
        # filter available list by size
        # return first available spot
        # else : None
        for lvl in self.levels:
            free_spot_lis_lvl = lvl.find_free_spots()
            for spot in free_spot_lis_lvl:
                if spot.size_ == incoming_vehicle.size_:
                    return spot
        return None

    def release_parking_spot(self, outgoing_vehicle:Vehicle) -> None:
        for lvl in self.levels:
            for spot in lvl:
                if spot.curr_vehicle.lic == outgoing_vehicle.lic:
                    spot.is_free = True

class Level:
    def __init__(self, num_spots) -> None:
        self._spots : List[ParkingSpot] = [ParkingSpot() for spot in range(num_spots)] # spots in this level

    def find_free_spots(self) -> List[ParkingSpot]:
        # find and return all free spots in a level
        free_spots_lis : List[ParkingSpot] = []
        for spot in self._spot:
            if spot._is_free:
                free_spots_lis.append(spot)
        return free_spots_lis

class ParkingSpot:
    def __init__(self) -> None:
        self._spotid:int = 0
        # restrict the values that a variable can take -> think enum
        self.size_:Size = Size.COMPACT
        self.is_free = True
        self.curr_vehicle : Optional[Vehicle] = None

    def park_vehicle(self, vehicle:Vehicle) -> None:
        # sanity check
        assert self.is_free
        self.is_free = False
        self.curr_vehicle = vehicle

class Size(Enum):
    COMPACT = 0
    NORMAL = 1
    LARGE = 2

class Vehicle:
    # leave it as abstract class. AG TODO - make it abstract
    # cannot create obbjects of Vehicle type, can only create sub-classes (Abstract class definition)
    def __init__(self) -> None:
        self.size_ = Size.LARGE
        self.lic = ""

class Bus(Vehicle):
    def __init__(self, license:str) -> None:
        self.lic = license
        self.size_ = Size.LARGE

class Car(Vehicle):
    def __init__(self, license:str) -> None:
        self.lic = license
        self.size_ = Size.NORMAL

class Bike(Vehicle):
    def __init__(self, license:str) -> None:
        self.lic = license
        self.size_ = Size.COMPACT

def main():
    lot = ParkingLot(5, 100)
    car1 = Car("KA1234")
    spot:ParkingSpot = lot.find_parking_spot(car1)
    
    if spot:
        spot.park_vehicle(car1)
        print("Parked succesfully!")
    else:
        print("Sorry, no spot available.")

    #bus1 is leaving
    bus1 = Bus("KA123")
    lot.release_parking_spot(bus1)
    print("spot released!")


if __name__ == "__main__":
    main()