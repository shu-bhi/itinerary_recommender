def generate_itinerary(destination, days=3):
    """
    Generate a simple day-wise itinerary for the destination.
    """
    itinerary = {f"Day {i+1}": f"Explore {destination} - Suggested activities" for i in range(days)}
    return itinerary

if __name__ == "__main__":
    destination = "Bali"
    itinerary = generate_itinerary(destination)
    print(f"Itinerary for {destination}:")
    for day, activities in itinerary.items():
        print(f"{day}: {activities}")
