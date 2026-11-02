from typing import List, Callable
from fleet.vehicles import Vehicle

class FleetAnalytics:
    def __init__(self, vehicles: List[Vehicle] = None):
        self.vehicles = vehicles if vehicles is not None else []

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)

    def filter_vehicles(self, predicate_fn: Callable[[Vehicle], bool]) -> List[Vehicle]:
        """Filtert Fahrzeuge flexibel nach einem übergebenen Lambda-Ausdruck."""
        return list(filter(predicate_fn, self.vehicles))

    def sort_vehicles(self, key_fn: Callable[[Vehicle], any], reverse: bool = False) -> List[Vehicle]:
        """Sortiert die Flotte flexibel nach Lambda-Kriterien."""
        return sorted(self.vehicles, key=key_fn, reverse=reverse)
