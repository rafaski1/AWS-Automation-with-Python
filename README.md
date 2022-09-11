# AWS-Automation-with-Python

## webotron
Webotron is a script that will deploy websites to S3, sync a local directory to s3 bucket. 
Using AWS CLI with 'boto3' and 'click' frameworks with python.

### features

- list s3 buckets
- list content of a s3 bucket
- create and setup bucket
- sync directory tree to bucket
- set AWS profile with --profile profileName

## notifon
Notifon is a script that will notify Slack users of changes to your AWS account using CloudWatch Events. Using AWS CLI with 'boto3' and 'serverless' framework with python.

### features

- Automating creation of EC2 instances
- Creating Auto Scaling group on EC2 instance
- Creating CloudWatch event whenever auto scaling takes place
- Using 'serverless' framework to mantain and deploy aws lambda funtions
- Sending notifications to Slack when CloudWatch events happen
