from flask import Flask, render_template, request
from azure.storage.blob import BlobServiceClient
import os

app = Flask(__name__)

# Replace with your Azure Storage connection string and container name
AZURE_CONNECTION_STRING = os.getenv("CUSTOMCONNSTR_AZURE_CONNECTION_STRING")
CONTAINER_NAME = "data-files"

# Initialize the Blob Service Client
blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        field1 = request.form.get("field1")
        field2 = request.form.get("field2")
        field3 = request.form.get("field3")
        field4 = request.form.get("field4")
        
        # Format the data to save
        result = f"Field 1: {field1}, Field 2: {field2}, Field 3: {field3}, Field 4: {field4}\n"
        
        # Define blob name for storing the data
        blob_name = "data.txt"

        # Upload the data to the blob
        try:
            # Get a reference to the blob
            blob_client = container_client.get_blob_client(blob_name)
            
            # Check if blob already exists to append data
            if blob_client.exists():
                # Download the current content to append to it
                current_data = blob_client.download_blob().readall().decode()
                result = current_data + result
            
            # Upload the updated content back to the blob
            blob_client.upload_blob(result, overwrite=True)
            print(f"Data saved to blob: {blob_name}")
        except Exception as e:
            print(f"Error saving to blob: {e}")

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
