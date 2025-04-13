PROJECT_ID=email-to-telegram-455900
REGION=us-central1
FUNCTION_NAME=renew-gmail-watch
ENV_FILE=../.env.yaml

deploy:
	gcloud functions deploy $(FUNCTION_NAME) \
		--entry-point=app \
		--runtime=python310 \
		--trigger-http \
		--allow-unauthenticated \
		--source=. \
		--env-vars-file=$(ENV_FILE) \
		--region=$(REGION) \
		--project=$(PROJECT_ID)

logs:
	gcloud functions logs read $(FUNCTION_NAME) --region=$(REGION) --project=$(PROJECT_ID)


