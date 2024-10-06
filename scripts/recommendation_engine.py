import pandas as pd

# Define a mock destination dataset
DESTINATIONS = {
    "Adventure": ["Rocky Mountains", "Grand Canyon", "Mt. Everest"],
    "Relaxation": ["Bali", "Maldives", "Hawaii"],
    "Socializing": ["Las Vegas", "New York", "Ibiza"]
}

def recommend_destination(user_profile, destinations=DESTINATIONS):
    """
    Recommend a destination based on user profile (vibe).
    """
    vibe = user_profile['vibe']
    if vibe in destinations:
        return destinations[vibe][0]  # Return the first destination for ease
    return "Unknown Destination"

if __name__ == "__main__":
    # Load a single user profile for testing
    user_data = pd.read_csv("../data/users.csv")
    user_profile = user_data.iloc[0]  # Select the first user
    destination = recommend_destination(user_profile)
    print(f"Recommended destination for user {user_profile['user_id']} ({user_profile['vibe']}): {destination}")
