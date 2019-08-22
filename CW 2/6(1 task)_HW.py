def couneter_fuel(distance_to_pump, distance, fuel_left):
    if distance*fuel_left<distance_to_pump:
        return False
    else:
        return True