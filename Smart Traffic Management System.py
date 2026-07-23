# Parent Class
class TrafficDevice:
    def activate(self):
        raise NotImplementedError("Subclasses must override activate()")

# Child Classes
class TrafficLight(TrafficDevice):
    def activate(self):
        print("Traffic Light: Switching lights to control vehicle flow.")

class SpeedCamera(TrafficDevice):
    def activate(self):
        print("Speed Camera: Monitoring and capturing speeding vehicles.")

class PedestrianSignal(TrafficDevice):
    def activate(self):
        print("Pedestrian Signal: Allowing pedestrians to cross safely.")

# New Class added later
class EmergencySiren(TrafficDevice):
    def activate(self):
        print("Emergency Siren: Alerting citizens of an emergency situation.")


# Create one object of each class
devices = [
    TrafficLight(),
    SpeedCamera(),
    PedestrianSignal(),
    EmergencySiren()  s
]

# Activate all devices without checking their types
for device in devices:
    device.activate()

