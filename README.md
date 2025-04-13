# Email to Telegram
Forward incoming email to a specific topic within a Telegram group.  
Deployed as a Google Cloud Function triggered by a Gmail pub/sub push notification, reads newly received email messages and forwards each one to a sepcific topic within a Telegram group.

## Dependencies 
- Google Cloud Functions, Run, Scheduler, API
- Gmail pub/sub push notification
- Telegram Bot API

## Design and Implementation
Reading and forwarding of email is done by a Python script running on Google Cloud Function.  This Google Cloud function is triggered by a watch configured on a Gmail pub/sub topic for a particular Gmail inbox.  Since a Google watch has a finite lifetime, it must be periodically renewed, and this renewal is handled by another Python script deployed on Google Run and triggered by Google Scheduler.

## Gmail Authentication
Access to the Gmail inbox of interest is provided via a token generated using the Gmail OAuth flow.  This token is then stored within the Google Cloud Secret Manager for the project.

## Telegram Authentication
Access to the Telegram group to which the email is forwarded is provided by a custom Telegram bot, which does nothing aside from existing as a member of the Telegram group of interest.

## Deployment
Use ```make deploy``` to rebuild and deploy each of the two pieces of the tool after making changes.

## Missing Pieces
A few bits are not stored in this public repository.

### .env.yaml
Defines environment variables:
- TELEGRAM_BOT_TOKEN
- TELEGRAM_CHAT_ID
- TELEGRAM_TOPIC_ID
- GCP_PROJECT

### token_<targetGmailUsername>.json
Gmail access token generated through OAuth flow by running utils/genOauthToken.py and authenticating with the <targetGmailUsername>@gmail.com, which is used only as an email account.  My personal Google Account has all the Google Cloud development gizmos associated with it.

### credentials.json
Google credentials for my personal Google Account so that these tools can access the Google API.

