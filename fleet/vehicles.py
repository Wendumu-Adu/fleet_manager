from abc import ABC, abstractmethod
from fleet.exceptions import InvalidMileageError, MaintenanceRequiredError

class Vehicle(ABC):
    def __init__(self, license_plate: str, mileage: float, last_service_km: float):
        if mileage < 0 or last_service_km < 0 or last_service_km > mileage:
            raise InvalidMileageError("Ungültige Kilometerstände bei der Erstellung.")

        self.license_plate = license_plate
        self._mileage = mileage
        self.last_service_km = last_service_km

    @property
    def mileage(self):
        return self._mileage

    def needs_service(self) -> bool:
        """Gibt True zurück, wenn seit dem letzten Service mehr als 15.000 km gefahren wurden."""
        return (self._mileage - self.last_service_km) >= 15000

    @abstractmethod
    def calculate_trip_cost(self, distance: float) -> float:
        """Abstrakter Platzhalter für die Berechnung der Fahrtkosten."""
        pass

    def drive(self, distance: float):
        """Erhöht den Kilometerstand und prüft die Wartungsfälligkeit (Zusatzaufgabe)."""
        if distance < 0:
            raise InvalidMileageError("Fahrtstrecke darf nicht negativ sein.")

        # Wenn bereits vor Fahrtantritt Wartung fällig war
        if self.needs_service():
            raise MaintenanceRequiredError(self.license_plate)

        self._mileage += distance

        # Warnung nach der Fahrt, falls das Intervall jetzt überschritten wurde
        if self.needs_service():
            print(f"WARNUNG: [{self.license_plate}] Nach dieser Fahrt von {distance} km ist ein Service fällig!")


class FuelVehicle(Vehicle):
    def __init__(self, license_plate: str, mileage: float, last_service_km: float,
                 fuel_consumption_per_100km: float, fuel_price_per_liter: float):
        super().__init__(license_plate, mileage, last_service_km)
        self.fuel_consumption_per_100km = fuel_consumption_per_100km
        self.fuel_price_per_liter = fuel_price_per_liter

    def calculate_trip_cost(self, distance: float) -> float:
        """Berechnet die Kraftstoffkosten für die Strecke."""
        return (distance / 100) * self.fuel_consumption_per_100km * self.fuel_price_per_liter


class EVehicle(Vehicle):
    def __init__(self, license_plate: str, mileage: float, last_service_km: float,
                 kwh_per_100km: float, electricity_price_per_kwh: float):
        super().__init__(license_plate, mileage, last_service_km)
        self.kwh_per_100km = kwh_per_100km
        self.electricity_price_per_kwh = electricity_price_per_kwh

    def calculate_trip_cost(self, distance: float) -> float:
        """Berechnet die Stromkosten für die Strecke."""
        return (distance / 100) * self.kwh_per_100km * self.electricity_price_per_kwh
