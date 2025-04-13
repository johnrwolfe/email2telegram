import os
import json
from flask import Request, jsonify
from google.cloud import secretmanager
from google.auth.transport.requests import Request as GoogleRequest
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def app(request: Request):
    project_id = os.environ['GCP_PROJECT']
    secret_name = "gmail_token_azffrescue"

    try:
        # Load token from Secret Manager
        client = secretmanager.SecretManagerServiceClient()
        secret_path = f"projects/{project_id}/secrets/{secret_name}/versions/latest"
        response = client.access_secret_version(request={"name": secret_path})
        token_data = json.loads(response.payload.data.decode("UTF-8"))

        # Setup credentials
        creds = Credentials.from_authorized_user_info(token_data)
        if not creds.valid and creds.expired and creds.refresh_token:
            creds.refresh(GoogleRequest())

        # Register Gmail watch
        service = build('gmail', 'v1', credentials=creds)
        res = service.users().watch(userId='me', body={
            'labelIds': ['INBOX'],
            'topicName': f'projects/{project_id}/topics/gmail-notifications'
        }).execute()

        return jsonify({'success': True, 'watch_response': res})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
