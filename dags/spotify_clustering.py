#%%
# import libraries
import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

#%%
def spotify_clustering():
    # Import csv
    df = pd.read_csv('/Users/nilsjennissen/PycharmProjects/airflow-automation/data/tracklist.csv')

    # Preprocessing for k-means
    df_cl = df[['tempo', 'loudness', 'danceability', 'energy', 'speechiness', 'acousticness', 'instrumentalness',
                'valence']]
    df_cl = df_cl.replace(0, 0.1)
    df_cl = df_cl.fillna(df_cl.mean())

    # Standardize data for k-means
    std_scaler = StandardScaler()
    df_scaled = std_scaler.fit_transform(df_cl)

    # Apply k-means
    model = KMeans(n_clusters=10, random_state=42)
    model.fit(df_scaled)
    df = df.assign(KMeans=model.labels_)

    # Transform cluster result
    df = df.rename(columns={'ClusterLabel': 'KMeans'})
    df['KMeans'] = df['KMeans'].astype('category')

    # Save the dataframe
    save_path = os.path.join('/Users/nilsjennissen/PycharmProjects/airflow-automation/data/', 'kmeans_spotify.csv')
    df.to_csv(save_path, index=False)

    return print(df.head(20))


# Call the function
# spotify_clustering()


#%%

# Define the default_args for the DAG
default_args = {
    'owner': 'your_name',  # Replace with your name
    'start_date': datetime(2023, 4, 11),  # Replace with the start date of your DAG
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


# Instantiate the DAG with the default_args
dag = DAG(
    'spotify_clustering_dag',  # Replace with the name of your DAG
    default_args=default_args,
    schedule_interval='@daily',  # Replace with the desired schedule interval for your DAG
)


# Define the PythonOperator to run the kmeans_clustering() function
spotify_task = PythonOperator(
    task_id='spotify_task',  # Replace with the name of the task
    python_callable=spotify_clustering,  # Replace with the actual name of your function
    dag=dag,
)

