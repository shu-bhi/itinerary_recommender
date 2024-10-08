# Personalized Itinerary Generator

## Project Overview

This project is a basic implementation of a personalized travel itinerary generator using Python. The system segments users into different travel personas based on their preferences, recommends a destination, and generates a simple itinerary for a specified number of days.

The project includes scripts for:

- Data loading and preprocessing
- User segmentation using K-Means clustering
- Destination recommendation based on user profiles
- Itinerary generation for the recommended destination

## Getting Started

### Prerequisites

To run this project, you need to have Python installed on your system. You will also need the following Python libraries:

- `pandas`
- `numpy`
- `scikit-learn`

Install the libraries using the following command:

```bash
pip install pandas numpy scikit-learn
```

## Dataset

```
user_id	expenses	vibe	reviews	instagram_photos	previous_destinations	favorite_activities
1	150	Adventure	Loved hiking in the mountains!	beach.jpg,hike.jpg	France,Spain	Hiking,Swimming
2	100	Relaxation	Enjoyed the calm beaches and sunset.	sunset.jpg,beach_dine.jpg	Thailand,Maldives	Beach walking,Fine dining
3	200	Socializing	Partied all night and made new friends!	party.jpg,club.jpg	New York,Las Vegas	Clubbing,Networking
```

## Setup

1. Clone the Repository Clone the repository to your local machine:

    ```bash
    git clone <repository_url>
    cd itinerary_recommender
    ```

2. Set Up the Data Ensure that the data/users.csv file is present with sample user data. You can modify this file or add more rows for additional users.

3. Run the Project Execute the main script to run the complete pipeline:

    ```bash
    python main.py
    ```
