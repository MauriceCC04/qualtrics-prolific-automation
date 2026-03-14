import requests
import json

# Your API configuration
API_TOKEN = ""  # Replace with your actual token
BASE_URL = "https://api.prolific.com/api/v1"

# Headers for authorization
headers = {
    "Authorization": f"Token {API_TOKEN}",
    "Content-Type": "application/json"
}


# Function to create a study draft
def create_study_draft():
    url = f"{BASE_URL}/studies/"

    # Basic study details
    study_data = {
        "name": "Test Study",
        "description": "This study was created as a test",
        "external_study_url": "https://mysurvey.com?participant={{%PROLIFIC_PID%}}",
        "prolific_id_option": "url_parameters",
        "completion_codes": [
            {
                "code": "ABC123",
                "code_type": "COMPLETED",
                "actions": [
                    {"action": "AUTOMATICALLY_APPROVE"}
                ]
            }
        ],
        "total_available_places": 5,
        "estimated_completion_time": 5,
        "reward": 50,  # This is in cents (100 = $1.00 or £1.00)
        "device_compatibility": ["desktop"],
        "peripheral_requirements": [],
        "filters": []  # No filters means available to all participants
    }

    # Make the API request
    response = requests.post(url, headers=headers, data=json.dumps(study_data))

    # Check if successful
    if response.status_code == 201:
        print("Study draft created successfully!")
        return response.json()
    else:
        print(f"Error creating study: {response.status_code}")
        print(response.text)
        return None


# Function to publish the study
def publish_study(study_id):
    url = f"{BASE_URL}/studies/{study_id}/transition/"

    publish_data = {
        "action": "PUBLISH"
    }

    response = requests.post(url, headers=headers, data=json.dumps(publish_data))

    if response.status_code == 200:
        print("Study published successfully!")
        return response.json()
    else:
        print(f"Error publishing study: {response.status_code}")
        print(response.text)
        return None


# Run the functions
if __name__ == "__main__":
    # First create a draft
    study = create_study_draft()

    if study:
        # If draft created successfully, get the ID and publish
        study_id = study["id"]
        print(f"Created draft study with ID: {study_id}")

        # Uncomment the next line when you're ready to publish
        # published_study = publish_study(study_id)
