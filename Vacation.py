def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
        
def rental_car_cost(days):
    price = 40 * days
    if days >= 7:
        price -= 50
    elif days >= 3:
        price -= 20
    return price
    
def trip_cost(city, days, spending_money):
    return (rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city)) + spending_money

print trip_cost("Los Angeles", 5, 600)
