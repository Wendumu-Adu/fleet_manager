class MaintenanceRequiredError(Exception):
    """Wird ausgelöst, wenn ein Fahrzeug mit überfälliger Wartung gebucht wird."""
    def __init__(self, license_plate, message="Wartung ist überfällig! Fahrt nicht erlaubt."):
        self.license_plate = license_plate
        self.message = f"[{license_plate}] {message}"
        super().__init__(self.message)


class InvalidMileageError(ValueError):
    """Wird geworfen, wenn ein Kilometerstand unzulässig ist."""
    pass
