from abc import ABC, abstractmethod
from enum import Enum

class TransportType(Enum):
    SHIP = "ship"
    TRUCK = "truck"
    TRAIN = "train"


class TransportVehicle(ABC):
    def __init__(self, vehicle_id: str):
        self.vehicle_id = vehicle_id

    
    @abstractmethod
    def get_vehicle_type(self) -> TransportType:
        pass

class Ship(TransportVehicle):
        def __init__(self, vehicle_id: str):
            super().__init__(vehicle_id)
            self.max_capacity = 10000  # tons
        
        def get_vehicle_type(self) -> TransportType:
            return TransportType.SHIP
        

class Truck(TransportVehicle):
    def __init__(self, vehicle_id: str):
        super().__init__(vehicle_id)
        self.max_capacity = 50  # tons
    
    def get_vehicle_type(self) -> TransportType:
        return TransportType.TRUCK