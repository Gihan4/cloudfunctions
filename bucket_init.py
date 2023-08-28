import os
from google.cloud import storage

def cleanup_old_tarballs(data, context):
    # Initialize Google Cloud Storage client
    client = storage.Client()

    # Get the bucket and object name from the event data
    bucket_name = data['bucket']
    object_name = data['name']

    # Define the name of the object you want to exclude from deletion
    excluded_object = 'index.yaml'

    # Get the bucket
    bucket = client.bucket(bucket_name)

    # List objects in the bucket
    blobs = list(bucket.list_blobs())

    # Sort blobs by their updated time in ascending order
    sorted_blobs = sorted(blobs, key=lambda blob: blob.updated)

    # Keep the newest blobs and exclude the specified object
    for blob in sorted_blobs[:-3]:  # Keep the three most recent objects
        if blob.name != excluded_object:
            blob.delete()

    print("Old tarballs cleaned up successfully.")

