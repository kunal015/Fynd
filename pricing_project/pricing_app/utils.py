def calculate_pricing(distance_base_price, distance_additional_price, time_multiplier_factor, waiting_charges, total_distance, time_duration, waiting_time, is_peak_time=False):
    if(total_distance<=3):
        distance_cost= distance_base_price
    else:
        distance_cost= distance_base_price + (distance_additional_price * (total_distance - 3))
        print("Distnace_cost=", distance_cost)
    time_cost = time_multiplier_factor * time_duration
    if(waiting_time < 3):
        total_cost= (distance_cost + time_cost)
        print("Total Cost =", total_cost)
    else :
        total_cost = (distance_cost + time_cost) + (waiting_charges * (waiting_time-3))
        print("Total Cost =", total_cost)
    return total_cost