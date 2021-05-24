# Aws_Tag_Import
This tool allows you to extract a list of resources (ARN), keys and values (Tags) from your AWS account.
It uses Boto3, (AWS SDK) as well as the Resource Group tagging API (https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/overview.html).
The region name is 'us-east-1' but it can easily be changed. 

*How to use:*
-create and add your  aws_access_key_id and aws_secret_access_key in the credentials.yml file
-run main.py
