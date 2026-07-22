One interface, many forms — this design makes the system flexible, easy to extend, and avoids messy conditional statementsThis code is a neat demonstration of polymorphism in Python applied to a smart traffic management system.

A parent class TrafficDevice defines a common interface activate().

Multiple child classes (TrafficLight, SpeedCamera, PedestrianSignal) each override activate() to perform their own unique action.

A new class, EmergencySiren, is added later without changing the activation loop, showing how polymorphism supports extensibility.Finally, all devices are stored in a list and activated in a loop, proving that the same method call (device.activate()) produces different behaviors depending on the object
