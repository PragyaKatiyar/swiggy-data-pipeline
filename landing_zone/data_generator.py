import os
import sys
import uuid
import random
import math
from datetime import datetime , timedelta
# pyrefly: ignore [missing-import]
from faker import Faker
import json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config
from landing_zone.indian_locations import pick_indian_location

fake = Faker("en_IN")
random.seed(42)
Faker.seed(42)


def generate_restaurants(num_restaurants=500):
    restaurants = []
    for _ in range(num_restaurants):
        city, state, zone = pick_indian_location()
        restaurant = {
            "restaurant_id": str(uuid.uuid4()),
            "restaurant_name": fake.company(),
            "cuisine_type": random.choices(
                [
                    "North Indian",
                    "South Indian",
                    "Chinese",
                    "Pizza",
                    "Biryani",
                    "Burgers",
                    "Desserts",
                ],
                weights=[30, 20, 15, 15, 10, 5, 5],
            )[0],
            "avg_rating": round(random.uniform(1.0, 5.0), 1),
            "avg_preparation_time": random.randint(10, 60),
            "is_active": random.choices([True, False], weights=[80, 20])[0],
            "commission_pct": random.randint(5, 20),
            "zone": zone,
            "restaurant_city": city,
            "restaurant_state": state, 
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")       }
        restaurants.append(restaurant)
    os.makedirs(config.LANDING_RESTAURANTS, exist_ok=True)
    with open(f"{config.LANDING_RESTAURANTS}/restaurants.json", 'w') as f:
        for row in restaurants:
            f.write(json.dumps(row) + "\n")
    print(f"Restaurants data generated and saved to {config.LANDING_RESTAURANTS}/restaurants.json")
    return restaurants



def random_past_date(days_back = 3 * 365 ):
    days_ago = random.randint(0 , days_back)
    return datetime.now() - timedelta(days=days_ago)


def generate_customers(num_customers = 2000):
    customers = []
    for _ in range(num_customers):
        city , state , zone = pick_indian_location()
        signup_date = random_past_date(1095)
        days_since_signup = (datetime.now() - signup_date).days
        last_order_date = random_past_date(days_since_signup)
        customer = {
            "customer_id" : str(uuid.uuid4()) ,
            "customer_name" : fake.name() ,
            "customer_email" : fake.email(),
            "customer_phone" : fake.phone_number(),
            "zone" : zone,
            "customer_city" : city,
            "customer_state" : state,
            "signup_date" : signup_date.strftime("%Y-%m-%d %H:%M:%S"),
            "subscription_tier" : random.choices(["Free", "Basic", "Premium", "Pro"] , weights=[40, 30, 20, 10])[0],
            "total_orders" : random.randint(0 , 500),
            "preferred_cuisine" : random.choices(
                [
                    "North Indian",
                    "South Indian",
                    "Chinese",
                    "Pizza",
                    "Biryani",
                    "Burgers",
                    "Desserts",
                ],
                weights=[30, 20, 15, 15, 10, 5, 5],
            )[0],
            "last_order_date" : last_order_date.strftime("%Y-%m-%d %H:%M:%S"),
            "rfm_segment" : random.choices(["Champions","Loyal","At Risk","Lost"] , weights=[15 , 25, 30 , 30])[0],
            "created_at" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        customers.append(customer)
    os.makedirs(config.LANDING_CUSTOMERS, exist_ok=True)
    with open(f"{config.LANDING_CUSTOMERS}/customers.json", 'w') as f:
        for row in customers:
            f.write(json.dumps(row) + "\n")
    print(f"Customers data generated and saved to {config.LANDING_CUSTOMERS}/customers.json")
    return customers

    




def generate_orders(customers, restaurants, num_orders=10000):
    # Group restaurants by city to make city-based restaurant selection realistic
    restaurants_by_city = {}
    for r in restaurants:
        restaurants_by_city.setdefault(r["restaurant_city"], []).append(r)
        
    orders = []
    for _ in range(num_orders):
        customer = random.choice(customers)
        city = customer["customer_city"]
        
        # Pick a restaurant in the same city if available, otherwise any restaurant
        city_restaurants = restaurants_by_city.get(city, restaurants)
        restaurant = random.choice(city_restaurants)
        
        # Parse customer signup date to ensure order placed_at is after signup_date
        signup_date = datetime.strptime(customer["signup_date"], "%Y-%m-%d %H:%M:%S")
        delta = datetime.now() - signup_date
        random_seconds = random.randint(0, max(0, int(delta.total_seconds())))
        placed_at = signup_date + timedelta(seconds=random_seconds)
        discount_applied = random.choices([True, False], weights=[35, 65])[0]

        order = {
            "order_id": str(uuid.uuid4()),
            "customer_id": customer["customer_id"],
            "restaurant_id": restaurant["restaurant_id"],
            "order_value": round(random.uniform(150.0, 2000.0), 2),
            "item_count": random.randint(1, 8),
            "status": random.choices(["delivered", "cancelled", "in_progress"], weights=[85, 10, 5])[0],
            "city": city,
            "placed_at": placed_at.strftime("%Y-%m-%d %H:%M:%S"),
            "payment_mode": random.choices(["UPI", "Credit Card", "Debit Card", "Net Banking", "Cash on Delivery"], weights=[55, 20, 10, 5, 10])[0],
            "discount_applied": discount_applied,
            "discount_amount": round(random.uniform(20.0, 200.0), 2) if discount_applied else 0.0
        }
        orders.append(order)
        
    os.makedirs(config.LANDING_ORDERS, exist_ok=True)
    with open(f"{config.LANDING_ORDERS}/orders.json", 'w') as f:
        for row in orders:
            f.write(json.dumps(row) + "\n")
    print(f"Orders data generated and saved to {config.LANDING_ORDERS}/orders.json")
    return orders


def calculate_haversine(lat1, lon1, lat2, lon2):
    R = 6371.0 # Radius of Earth in km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    return round(R * c, 2)


def generate_deliveries(orders):
    deliveries = []
    for order in orders:
        if order["status"] == "cancelled":
            continue
            
        delivery_id = str(uuid.uuid4())
        agent_id = f"AGNT-{random.randint(10000, 99999)}"
        
        # Generate coordinates within India
        pickup_lat = round(random.uniform(8.0, 34.0), 6)
        pickup_lon = round(random.uniform(68.0, 96.0), 6)
        
        # Drop coordinates within 0.01 to 0.08 degrees (approx 1 - 9 km)
        d_lat = random.uniform(-0.08, 0.08)
        d_lon = random.uniform(-0.08, 0.08)
        if abs(d_lat) < 0.005: d_lat += 0.01 * random.choice([-1, 1])
        if abs(d_lon) < 0.005: d_lon += 0.01 * random.choice([-1, 1])
        
        drop_lat = round(pickup_lat + d_lat, 6)
        drop_lon = round(pickup_lon + d_lon, 6)
        
        # Calculate distance
        distance_km = calculate_haversine(pickup_lat, pickup_lon, drop_lat, drop_lon)
        
        # Promised time based on distance
        promised_time_min = 20 + int(distance_km * 4) + random.randint(0, 10)
        # Round to nearest 5 minutes for realism
        promised_time_min = max(20, (promised_time_min // 5) * 5)
        
        if order["status"] == "delivered":
            status = "delivered"
            # Actual time: around promised time, sometimes late
            actual_time_min = max(10, promised_time_min + random.randint(-10, 20))
            is_late = actual_time_min > promised_time_min
        else: # in_progress
            status = "in_transit"
            actual_time_min = None
            is_late = None
            
        delivery = {
            "delivery_id": delivery_id,
            "order_id": order["order_id"],
            "agent_id": agent_id,
            "restaurant_id": order["restaurant_id"],
            "pickup_lat": pickup_lat,
            "pickup_lon": pickup_lon,
            "drop_lat": drop_lat,
            "drop_lon": drop_lon,
            "promised_time_min": promised_time_min,
            "actual_time_min": actual_time_min,
            "distance_km": distance_km,
            "is_late": is_late,
            "status": status,
            "city": order["city"],
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        }
        deliveries.append(delivery)
        
    os.makedirs(config.LANDING_DELIVERY, exist_ok=True)
    with open(f"{config.LANDING_DELIVERY}/delivery.json", 'w') as f:
        for row in deliveries:
            f.write(json.dumps(row) + "\n")
    print(f"Delivery data generated and saved to {config.LANDING_DELIVERY}/delivery.json")
    return deliveries


if __name__ == "__main__":
    restaurants = generate_restaurants()
    customers = generate_customers()
    orders = generate_orders(customers, restaurants)
    generate_deliveries(orders)