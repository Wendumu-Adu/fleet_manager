
from fleet import FuelVehicle, EVehicle, FleetAnalytics, MaintenanceRequiredError

def main():
    # 1. Flotte erstellen (mindestens 2 Verbrenner, 2 E-Fahrzeuge)
    v1 = FuelVehicle("K-VW-100E", mileage=12000, last_service_km=0, fuel_consumption_per_100km=6.5, fuel_price_per_liter=1.75)
    v2 = FuelVehicle("K-BM-200X", mileage=65000, last_service_km=48000, fuel_consumption_per_100km=8.2, fuel_price_per_liter=1.80)
    v3 = EVehicle("K-TS-300E", mileage=55000, last_service_km=50000, kwh_per_100km=18.0, electricity_price_per_kwh=0.40)
    v4 = EVehicle("K-ID-400E", mileage=8000, last_service_km=0, kwh_per_100km=16.5, electricity_price_per_kwh=0.35)

    analytics = FleetAnalytics([v1, v2, v3, v4])
    print("="* 72)
    print("		1. Fahrzeuge, die zum Service müssen")
    print("="* 72)

    service_needed = analytics.filter_vehicles(lambda v: v.needs_service())
    for v in service_needed:
        print(f" {v.license_plate} (KM: {v.mileage}, Letzter Service bei: {v.last_service_km})")

    print("="* 72)
    print("\n		2. Fahrzeuge mit Kilometerstand über 50.000 km")
    print("="* 72)

    high_mileage = analytics.filter_vehicles(lambda v: v.mileage > 50000)
    for v in high_mileage:
        print(f" {v.license_plate} (KM: {v.mileage})")

    # 3. Fahrtkostenberechnung für 250 km & günstigstes Fahrzeug finden
    test_distance = 250

    print("="* 72)
    print(f"\n		3. Fahrtkosten für {test_distance} km")
    print("="* 72)

    for v in analytics.vehicles:
        cost = v.calculate_trip_cost(test_distance)
        print(f" {v.license_plate}: {cost:.2f} €")

    cheapest_vehicle = min(analytics.vehicles, key=lambda v: v.calculate_trip_cost(test_distance))

    print("=" * 72)
    print(f"\n Günstigstes Fahrzeug für die Strecke: {cheapest_vehicle.license_plate} "
          f"({cheapest_vehicle.calculate_trip_cost(test_distance):.2f} €)")
    #print("="* 60)
    # 4. Demonstration der Zusatzaufgabe (Fahrsimulation & Exception)
    print("="* 72)
    print("\n		4. Simulation der Zusatzaufgabe")
    print("="* 72)
    try:
        print(f"Fahre mit {v1.license_plate}...")
        v1.drive(4000)

        print(f"\nVersuche mit {v2.license_plate} zu fahren (Wartung bereits überfällig)...")
        v2.drive(50)
    except MaintenanceRequiredError as e:
        print(f"Abgefangen: {e}")
        print("=" * 72)


if __name__ == "__main__":
    main()
