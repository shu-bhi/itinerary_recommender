from scripts.data_preprocessing import load_user_data, preprocess_data
from scripts.user_segmentation import segment_users
from scripts.recommendation_engine import recommend_destination
from scripts.itinerary_generation import generate_itinerary

# Step 1: Load and preprocess the data
data = load_user_data("data/users.csv")
data = preprocess_data(data)

# Step 2: Segment users
segmented_data, _ = segment_users(data)

# Step 3: Recommend destination for a sample user
user_profile = segmented_data.iloc[0]  # Select first user for demo
destination = recommend_destination(user_profile)

# Step 4: Generate itinerary
itinerary = generate_itinerary(destination)
print(f"Recommended destination for User {user_profile['user_id']}: {destination}")
print("Generated Itinerary:")
for day, activities in itinerary.items():
    print(f"{day}: {activities}")
