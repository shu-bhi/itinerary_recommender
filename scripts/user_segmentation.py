from sklearn.cluster import KMeans
import pandas as pd

def segment_users(df, n_clusters=3):
    """
    Segment users based on expenses and vibe using K-Means clustering.
    """
    # Convert categorical vibe into numerical values for clustering
    vibe_mapping = {vibe: idx for idx, vibe in enumerate(df['vibe'].unique())}
    df['vibe_num'] = df['vibe'].map(vibe_mapping)

    # Select features for clustering
    features = df[['expenses', 'vibe_num']]

    # Fit K-Means model
    kmeans = KMeans(n_clusters=n_clusters)
    df['cluster'] = kmeans.fit_predict(features)

    return df, kmeans

if __name__ == "__main__":
    # Load preprocessed data
    user_data = pd.read_csv("../data/users.csv")
    # Segment users into clusters
    segmented_data, model = segment_users(user_data)
    print(segmented_data[['user_id', 'vibe', 'expenses', 'cluster']])
