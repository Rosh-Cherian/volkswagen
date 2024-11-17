def suggest_gear_and_speed(distance, speed, rpm, gear):
    # Vehicle-specific parameters (assumed for general case)
    safe_distance = speed / 30  # meters, minimum safe distance to the vehicle in front
    gear_speed_map = {
        1: (0, 20),    # Gear 1 is optimal for speeds between 0-20 km/h
        2: (15, 40),   # Gear 2 is optimal for speeds between 15-40 km/h
        3: (35, 60),   # Gear 3 is optimal for speeds between 35-60 km/h
        4: (55, 90),   # Gear 4 is optimal for speeds between 55-90 km/h
        5: (85, 120),  # Gear 5 is optimal for speeds between 85-120 km/h
    }
    optimal_rpm_range = (1500, 3000)  # Optimal RPM range for fuel efficiency
    
    # Safety check
    if distance < safe_distance:
        return "Reduce speed to maintain a safe distance."
      
    # Suggest optimal gear based on speed
    for g, (min_speed, max_speed) in gear_speed_map.items():
        if min_speed <= speed <= max_speed:
            optimal_gear = g
            break
    else:
        optimal_gear = gear  # No change if out of defined range

    # Determine current gear efficiency
    if rpm <= optimal_rpm_range[0]:
        suggestion = "Downshift to the next gear for better efficiency."
    elif rpm >= optimal_rpm_range[1]:
        suggestion = "Upshift to reduce RPM."
    elif gear == optimal_gear:
        suggestion = "Current gear is within the optimal range."
    else:
        suggestion = "None."
        
    # Return suggestions
    return {
        "suggested_gear": optimal_gear,
        "suggested_speed_range": gear_speed_map[optimal_gear],
        "additional_suggestion": suggestion
    }

# Example usage
print("Enter parameters")
input_data = {
    "distance": float(input("Distance: ")),  # in meters
    "speed": int(input("Speed: ")),     # in km/h
    "rpm": int(input("Rpm: ")),     # current RPM
    "gear": int(input("Gear: "))        # current gear
}

result = suggest_gear_and_speed(**input_data)
print("Suggestions:")
print(result)
