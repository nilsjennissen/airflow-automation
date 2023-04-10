# Airflow Automation Project for ML Clustering

This project is an end-to-end machine learning workflow using Apache Airflow. The goal of this project is to take a tracklist.csv file, cluster the data using a machine learning clustering algorithm, and create playlists based on the clustering results.

### 🧭 Project Overview

This project follows the following tasks:

1. Extract data from a Bronze layer in an S3 bucket (raw csv/json...)
2. Transform the data by joining it with other data and saving it in a Silver layer in an S3 bucket in Parquet format with the necessary splits for model training
3. Train a machine learning clustering algorithm on the transformed data
4. Track parameters and metrics, such as the accuracy of the clustering algorithm, using logs
5. Deploy the model to production as an endpoint/API container or execute a batch prediction on some data

### ⏱️ Estimated time needed: 2h 
Note: That the time estimation may vary due to your setup and previous experience. 

### 🚧 Prerequisites

Before running this project, you must have the following:

1. Access to an AWS account
2. An S3 bucket for storing data in both the Bronze and Silver layers
3. An EC2 instance for running Apache Airflow

### 🎛️ Project Setup

1. Clone the project repository to your local machine
2. Create a Python virtual environment and activate it
3. Install the necessary packages by running pip install -r requirements.txt
4. Configure your AWS credentials by running aws configure and entering your access and secret keys
5. Configure your Airflow environment by setting up the Airflow home directory, creating the dags folder, and updating the airflow.cfg file with your S3 bucket information.
6. Running the Project
7. Start the Airflow webserver by running airflow webserver -p 8080
8. Start the Airflow scheduler by running airflow scheduler
9. Navigate to http://localhost:8080 in your browser to access the Airflow web interface
10. Trigger the DAG by turning it on from the Airflow UI or using the airflow trigger_dag command
11. Monitor the DAG's progress and logs in the Airflow UI

### 🧩 Project Structure

```bash
├── dags
│   └── ml_clustering_workflow.py
├── logs
│   └── ...
├── src 
│   ├── extract_data.py
│   ├── transform_data.py
│   ├── train_model.py
│   └── deploy_model.py
├── utils
│   ├── config.py
│   └── s3.py
├── README.md
└── requirements.txt
```

* dags/: This folder contains the Airflow DAG file that defines the workflow.
* logs/: This folder contains the logs for the Airflow DAG.
* scripts/: This folder contains the Python scripts that perform the data extraction, transformation, model training, and model deployment tasks.
* utils/: This folder contains utility functions and configurations for the project.
* README.md: This file contains the project overview and setup instructions.
* requirements.txt: This file contains the Python package dependencies for the project.

### 🗄️ Data

### 📚 References


### 🏆 Conclusion

This project showcases an end-to-end machine learning workflow using Apache Airflow. It extracts data from a Bronze layer in an S3 bucket, transforms the data, trains a machine learning clustering algorithm, and deploys the model to production. This project can be used as a template for creating more complex machine learning pipelines with Airflow.
