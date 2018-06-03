# Setup

* Login to AWS -> Services -> Lambda -> Create function
* Select Author from Scratch

    Name: testSesAndSnsWithMySQL
    Runtime: Python 3.6
    Role: Create new role from Template(s)
    RoleName: ServiceRoleForLambda-TestSesAndSnsWithMySQL
    Policy Templates: Simple Microservice Template

See [testSesAndSnsWithMySQL.yaml](./testSesAndSnsWithMySQL.yaml) for reference

## Create Function

Add SNS, SES and VPC policies to new service role

* Services -> IAM -> Roles -> ServiceRoleForLambda-TestSesAndSnsWithMySQL
* Permissions -> Attach policy

## Additional Service Role Policies

Find and attach the following policies:

* AmazonSESFullAccess
* AWSLambdaVPCAccessExecutionRole
* AmazonSNSFullAccess

## Validate Email address for SES

Services -> Simple Email Service -> Email Addresses -> Verify a New Email Address

Enter email and click verification link in your inbox from amazon

## Security Group

Services -> EC2 -> Security Groups -> Create Security Group

    Name: MySQL
    Description: MySQL access

Save, then copy the security group ID, select the group, edit incoming rules

Add new rule

    Service: MySQL
    Source: sg-##### (paste security group id of the security group you are editing)
    Note: self

We will add this to the RDS instance as well as lambda, this will allow these services to talk to each other on port 80 without worrying about IP addresses (could do 2 groups, this works and doesn't really increase any security concerns as lambda can't be talked to directly).

## RDS

Services -> RDS -> Instances -> Launch Instance

Maria/MySQL/Aurora (or specify port for others)

Don't allow public access, add security group created above (MySQL)

## Lambda

Services -> Lambda -> Functions -> TestSesAndSnsWithMySQL

### Tests

Next to the Test button at the top, select Configure test events

Create a test for SNS, Email, http, and MySQL using the `.json` files in [/setup](./)

### Files

Make sure the Lambda function is selected in the designer view

Under Function Code, in the editor:

* Replace `lambda_function.py` with [src/lambda_function.py](../src/lambda_function.py)
* Create a new file `simple_tests.py` and paste the contets of [src/simple_tests.py](../src/simple_tests.py) there

### Environment variables

Add key: `FROM_ADDRESS`, value should be email address that you verified in SES

### VPC Configuration

See [README.md](../README.md)
