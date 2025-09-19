"""
Auckland Transport Logistics System
Language Preference: English only - no Chinese characters anywhere
"""

from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime
from typing import Dict, List, Optional

# System Configuration Constants
DEFAULT_LANGUAGE = "English"
DEFAULT_CURRENCY = "NZD"
DEFAULT_DISTANCE_UNIT = "km"
DEFAULT_WEIGHT_UNIT = "tons"
DEFAULT_TIME_UNIT = "hours"

# Transport vehicle type enumeration
class TransportType(Enum):
    SHIP = "ship"
    TRUCK = "truck"
    TRAIN = "train"
    PLANE = "plane"

# Cargo status enumeration
class CargoStatus(Enum):
    PENDING = "pending"
    IN_TRANSIT = "in_transit"
    AT_PORT = "at_port"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

# Abstract base class for transport vehicles
class TransportVehicle(ABC):
    def __init__(self, vehicle_id: str, capacity: float, current_location: str):
        self.vehicle_id = vehicle_id
        self.capacity = capacity
        self.current_location = current_location
        self.is_available = True
        self.current_cargo = []
    
    @abstractmethod
    def get_vehicle_type(self) -> TransportType:
        pass
    
    @abstractmethod
    def calculate_cost(self, distance: float, weight: float) -> float:
        pass
    
    @abstractmethod
    def get_estimated_time(self, distance: float) -> int:  # Returns hours
        pass
    
    def load_cargo(self, cargo_id: str, weight: float) -> bool:
        if not self.is_available or sum(cargo['weight'] for cargo in self.current_cargo) + weight > self.capacity:
            return False
        self.current_cargo.append({'id': cargo_id, 'weight': weight})
        return True
    
    def unload_cargo(self, cargo_id: str) -> bool:
        for i, cargo in enumerate(self.current_cargo):
            if cargo['id'] == cargo_id:
                self.current_cargo.pop(i)
                return True
        return False

# Concrete transport vehicle implementations
class Ship(TransportVehicle):
    def __init__(self, vehicle_id: str, capacity: float, current_location: str):
        super().__init__(vehicle_id, capacity, current_location)
        self.max_capacity = 10000  # tons
    
    def get_vehicle_type(self) -> TransportType:
        return TransportType.SHIP
    
    def calculate_cost(self, distance: float, weight: float) -> float:
        # Ship transport cost: base cost + distance cost + weight cost
        base_cost = 500
        distance_cost = distance * 0.5
        weight_cost = weight * 0.1
        return round(base_cost + distance_cost + weight_cost, 2)
    
    def get_estimated_time(self, distance: float) -> int:
        # Ship average speed ~25 knots, 1 knot = 1.852 km/h
        speed_kmh = 25 * 1.852
        return int(distance / speed_kmh)

class Truck(TransportVehicle):
    def __init__(self, vehicle_id: str, capacity: float, current_location: str):
        super().__init__(vehicle_id, capacity, current_location)
        self.max_capacity = 50  # tons
    
    def get_vehicle_type(self) -> TransportType:
        return TransportType.TRUCK
    
    def calculate_cost(self, distance: float, weight: float) -> float:
        # Truck transport cost
        base_cost = 100
        distance_cost = distance * 2.0
        weight_cost = weight * 0.5
        return base_cost + distance_cost + weight_cost
    
    def get_estimated_time(self, distance: float) -> int:
        # Truck average speed ~80 km/h
        return int(distance / 80)

class Train(TransportVehicle):
    def __init__(self, vehicle_id: str, capacity: float, current_location: str):
        super().__init__(vehicle_id, capacity, current_location)
        self.max_capacity = 2000  # tons
    
    def get_vehicle_type(self) -> TransportType:
        return TransportType.TRAIN
    
    def calculate_cost(self, distance: float, weight: float) -> float:
        # Train transport cost
        base_cost = 200
        distance_cost = distance * 1.0
        weight_cost = weight * 0.2
        return base_cost + distance_cost + weight_cost
    
    def get_estimated_time(self, distance: float) -> int:
        # Train average speed ~60 km/h
        return int(distance / 60)

class Plane(TransportVehicle):
    def __init__(self, vehicle_id: str, capacity: float, current_location: str):
        super().__init__(vehicle_id, capacity, current_location)
        self.max_capacity = 100  # tons
    
    def get_vehicle_type(self) -> TransportType:
        return TransportType.PLANE
    
    def calculate_cost(self, distance: float, weight: float) -> float:
        # Plane transport cost (most expensive but fastest)
        base_cost = 1000
        distance_cost = distance * 3.0
        weight_cost = weight * 2.0
        return base_cost + distance_cost + weight_cost
    
    def get_estimated_time(self, distance: float) -> int:
        # Plane average speed ~800 km/h
        return int(distance / 800)

# Transport vehicle factory class
class TransportFactory:
    _vehicle_types = {
        TransportType.SHIP: Ship,
        TransportType.TRUCK: Truck,
        TransportType.TRAIN: Train,
        TransportType.PLANE: Plane
    }
    
    @staticmethod
    def create_vehicle(vehicle_type: TransportType, vehicle_id: str, 
                      capacity: float, current_location: str) -> TransportVehicle:
        vehicle_class = TransportFactory._vehicle_types.get(vehicle_type)
        if not vehicle_class:
            raise ValueError(f"Unsupported vehicle type: {vehicle_type}")
        return vehicle_class(vehicle_id, capacity, current_location)
    
    @staticmethod
    def get_available_vehicle_types() -> List[TransportType]:
        return list(TransportFactory._vehicle_types.keys())

# Cargo class
class Cargo:
    def __init__(self, cargo_id: str, description: str, weight: float, 
                 origin: str, destination: str, priority: str = "normal"):
        self.cargo_id = cargo_id
        self.description = description
        self.weight = weight
        self.origin = origin
        self.destination = destination
        self.priority = priority
        self.status = CargoStatus.PENDING
        self.created_at = datetime.now()
        self.assigned_vehicle = None
        self.estimated_delivery = None

# Port class
class Port:
    def __init__(self, port_id: str, name: str, location: str, capacity: int):
        self.port_id = port_id
        self.name = name
        self.location = location
        self.capacity = capacity
        self.current_cargo = []
        self.available_vehicles = []
    
    def add_vehicle(self, vehicle: TransportVehicle):
        if len(self.available_vehicles) < self.capacity:
            self.available_vehicles.append(vehicle)
            vehicle.current_location = self.location
            return True
        return False
    
    def remove_vehicle(self, vehicle_id: str) -> bool:
        for i, vehicle in enumerate(self.available_vehicles):
            if vehicle.vehicle_id == vehicle_id:
                self.available_vehicles.pop(i)
                return True
        return False
    
    def get_available_vehicles(self, vehicle_type: TransportType = None) -> List[TransportVehicle]:
        if vehicle_type:
            return [v for v in self.available_vehicles 
                   if v.get_vehicle_type() == vehicle_type and v.is_available]
        return [v for v in self.available_vehicles if v.is_available]

# Auckland Transport Logistics System Singleton Class
class AucklandTransportLogistics:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self.ports = {}
            self.vehicles = {}
            self.cargo_list = {}
            self.transport_routes = {}
            self._initialized = True
            self._initialize_auckland_ports()
    
    def _initialize_auckland_ports(self):
        """Initialize Auckland's main ports"""
        # Auckland Port
        auckland_port = Port("AKL001", "Auckland Port", "Auckland CBD", 50)
        self.ports["AKL001"] = auckland_port
        
        # West Port
        west_port = Port("WST001", "West Port", "Auckland West", 30)
        self.ports["WST001"] = west_port
        
        # East Port
        east_port = Port("EST001", "East Port", "Auckland East", 25)
        self.ports["EST001"] = east_port
    
    def add_vehicle(self, vehicle_type: TransportType, vehicle_id: str, 
                   capacity: float, port_id: str) -> bool:
        """Add transport vehicle to specified port"""
        if port_id not in self.ports:
            return False
        
        vehicle = TransportFactory.create_vehicle(vehicle_type, vehicle_id, capacity, "")
        success = self.ports[port_id].add_vehicle(vehicle)
        if success:
            self.vehicles[vehicle_id] = vehicle
        return success
    
    def create_cargo(self, cargo_id: str, description: str, weight: float,
                    origin: str, destination: str, priority: str = "normal") -> Cargo:
        """Create new cargo"""
        cargo = Cargo(cargo_id, description, weight, origin, destination, priority)
        self.cargo_list[cargo_id] = cargo
        return cargo
    
    def assign_cargo_to_vehicle(self, cargo_id: str, vehicle_id: str) -> bool:
        """Assign cargo to transport vehicle"""
        if cargo_id not in self.cargo_list or vehicle_id not in self.vehicles:
            return False
        
        cargo = self.cargo_list[cargo_id]
        vehicle = self.vehicles[vehicle_id]
        
        if not vehicle.is_available:
            return False
        
        # Calculate distance (simplified)
        distance = self._calculate_distance(cargo.origin, cargo.destination)
        
        # Check capacity
        if not vehicle.load_cargo(cargo_id, cargo.weight):
            return False
        
        # Update cargo status
        cargo.status = CargoStatus.IN_TRANSIT
        cargo.assigned_vehicle = vehicle_id
        # Fix time calculation
        estimated_hours = vehicle.get_estimated_time(distance)
        cargo.estimated_delivery = datetime.now().replace(hour=(datetime.now().hour + estimated_hours) % 24)
        
        # Mark vehicle as unavailable
        vehicle.is_available = False
        
        return True
    
    def _calculate_distance(self, origin: str, destination: str) -> float:
        """Calculate distance between two points (simplified implementation)"""
        # In real application, should use geographic coordinates for actual distance
        distance_map = {
            ("Auckland CBD", "Auckland West"): 25.0,
            ("Auckland CBD", "Auckland East"): 20.0,
            ("Auckland West", "Auckland East"): 35.0,
            ("Auckland CBD", "Auckland CBD"): 0.0,
            ("Auckland West", "Auckland West"): 0.0,
            ("Auckland East", "Auckland East"): 0.0,
        }
        return distance_map.get((origin, destination), 50.0)
    
    def get_available_vehicles(self, port_id: str, vehicle_type: TransportType = None) -> List[TransportVehicle]:
        """Get available transport vehicles at specified port"""
        if port_id not in self.ports:
            return []
        return self.ports[port_id].get_available_vehicles(vehicle_type)
    
    def get_cargo_status(self, cargo_id: str) -> Optional[CargoStatus]:
        """Get cargo status"""
        if cargo_id in self.cargo_list:
            return self.cargo_list[cargo_id].status
        return None
    
    def get_system_summary(self) -> Dict:
        """Get system summary information"""
        total_vehicles = len(self.vehicles)
        total_cargo = len(self.cargo_list)
        available_vehicles = sum(1 for v in self.vehicles.values() if v.is_available)
        
        return {
            "Total Ports": len(self.ports),
            "Total Vehicles": total_vehicles,
            "Available Vehicles": available_vehicles,
            "Total Cargo": total_cargo,
            "Port List": [port.name for port in self.ports.values()]
        }

# Demonstration and test functions
def demonstrate_auckland_logistics():
    """Demonstrate Auckland Transport Logistics System"""
    print("=== Auckland Transport Logistics System Demo ===\n")
    
    # Get system instance (singleton)
    logistics = AucklandTransportLogistics()
    
    # Add transport vehicles to different ports
    print("1. Adding transport vehicles to ports...")
    logistics.add_vehicle(TransportType.SHIP, "SHIP001", 5000, "AKL001")
    logistics.add_vehicle(TransportType.TRUCK, "TRUCK001", 30, "AKL001")
    logistics.add_vehicle(TransportType.TRAIN, "TRAIN001", 1000, "WST001")
    logistics.add_vehicle(TransportType.PLANE, "PLANE001", 50, "EST001")
    
    print("✓ Transport vehicles added successfully\n")
    
    # Create cargo
    print("2. Creating cargo...")
    cargo1 = logistics.create_cargo("CARGO001", "Electronics", 25, "Auckland CBD", "Auckland West", "high")
    cargo2 = logistics.create_cargo("CARGO002", "Food", 200, "Auckland West", "Auckland East", "normal")
    cargo3 = logistics.create_cargo("CARGO003", "Emergency Medical Supplies", 30, "Auckland CBD", "Auckland East", "urgent")
    
    print("✓ Cargo created successfully\n")
    
    # Assign cargo to transport vehicles
    print("3. Assigning cargo to transport vehicles...")
    result1 = logistics.assign_cargo_to_vehicle("CARGO001", "TRUCK001")
    result2 = logistics.assign_cargo_to_vehicle("CARGO002", "TRAIN001")
    result3 = logistics.assign_cargo_to_vehicle("CARGO003", "PLANE001")
    
    print(f"✓ Cargo assignment completed - CARGO001: {'Success' if result1 else 'Failed'}, CARGO002: {'Success' if result2 else 'Failed'}, CARGO003: {'Success' if result3 else 'Failed'}\n")
    
    # Display system status
    print("4. System Status Summary:")
    summary = logistics.get_system_summary()
    for key, value in summary.items():
        print(f"   {key}: {value}")
    
    print("\n5. Cargo Status:")
    for cargo_id in ["CARGO001", "CARGO002", "CARGO003"]:
        status = logistics.get_cargo_status(cargo_id)
        print(f"   {cargo_id}: {status.value if status else 'Not Found'}")
    
    print("\n6. Available Transport Vehicles:")
    for port_id, port in logistics.ports.items():
        available = logistics.get_available_vehicles(port_id)
        print(f"   {port.name}: {len(available)} available vehicles")
        for vehicle in available:
            print(f"     - {vehicle.vehicle_id} ({vehicle.get_vehicle_type().value})")

def demonstrate_singleton_pattern():
    """Demonstrate Singleton Pattern"""
    print("\n=== Singleton Pattern Demo ===")
    
    # Create two instances, should return the same object
    logistics1 = AucklandTransportLogistics()
    logistics2 = AucklandTransportLogistics()
    
    print(f"logistics1 ID: {id(logistics1)}")
    print(f"logistics2 ID: {id(logistics2)}")
    print(f"Are they the same instance: {logistics1 is logistics2}")
    
    # Verify they share the same data
    logistics1.add_vehicle(TransportType.SHIP, "SINGLETON_TEST", 1000, "AKL001")
    print(f"Does logistics2 contain test ship: {'SINGLETON_TEST' in logistics2.vehicles}")

def demonstrate_factory_pattern():
    """Demonstrate Factory Pattern"""
    print("\n=== Factory Pattern Demo ===")
    
    # Use factory to create different types of transport vehicles
    vehicle_types = [
        (TransportType.SHIP, "FACTORY_SHIP", 5000),
        (TransportType.TRUCK, "FACTORY_TRUCK", 40),
        (TransportType.TRAIN, "FACTORY_TRAIN", 1500),
        (TransportType.PLANE, "FACTORY_PLANE", 60)
    ]
    
    for vehicle_type, vehicle_id, capacity in vehicle_types:
        vehicle = TransportFactory.create_vehicle(vehicle_type, vehicle_id, capacity, "Test Location")
        print(f"Created {vehicle.get_vehicle_type().value}: {vehicle.vehicle_id}")
        print(f"  Capacity: {vehicle.capacity} tons")
        print(f"  Cost calculation (100km, 10 tons): ${vehicle.calculate_cost(100, 10):.2f}")
        print(f"  Estimated time (100km): {vehicle.get_estimated_time(100)} hours")

if __name__ == "__main__":
    demonstrate_auckland_logistics()
    demonstrate_singleton_pattern()
    demonstrate_factory_pattern()
