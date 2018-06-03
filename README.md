# aws-lambda-nat-gateway-test

Testing a NAT Gateway for AWS Lambda with public and VPC access

This is intended both act as a reference and to give some guided practice for setting up a lambda function with VPC and public access.

Demo: https://youtu.be/Il34sBQbfXE

## Setup

If you want to setup an environment for this test, follow the [setup guide](setup/README.md)

## VPC Configuration

*NOTE: a NAT Gateway has an [hourly charge](https://aws.amazon.com/vpc/pricing/) (cost will be ~$32+/month, if you don't need this for a production purpose, delete your NAT Gateway after completing this exercise)*

Assuming you already have a VPC with at least 1 subnet attached to an internet gateway (the default VPC is fine for this)

1. Services -> VPC -> NAT Gateway -> Create NAT Gateway
 * Select any (public) subnet that in the VPC that has resources you want your Lambda function to access that has an Internet Gateway in it's route table (0.0.0.0/0 -> igw-######). All of the default subnets in your account will be setup this way.
 * Create a new elastic IP by clicking Create New EIP (this will be the IP address your lambda function is seen as when accessing external resources)
 * Click Create a NAT Gateway
2. Select Route Tables -> Create Route Table
 * Name the route table (PrivateSubnetToNatGateway)
 * Select the same VPC as your public subnet from step 1
 * Create
 * Select the newly created route table
 * Remove any Internet Gateways in it's route table (if any in this there, this won't work!)
 * Add a route to the new NAT Gateway (0.0.0.0/0 -> nat-######)
3. Select Subnets -> Create Subnet
 * Name the new subnet (PrivateSubnetWithNatGateway)
 * Select ehe same VPC as your public subnet from step 1
 * IPV4 CIDR Block (depends on your VPC! Must be in your VPC's IP address block, must not overlap any other subnets in the VPC)
 * Create
 * Select your new subnet (PrivateSubnetWithNatGateway)
 * Route Table -> Edit -> Change to your new route table (PrivateSubnetToNatGateway)
 * Verify the route table has no Internet Gateways in it (0.0.0.0/0 -> igw-###)
 * Verify the route table has your new NAT Gateway in it (0.0.0.0/0 -> nat-###)
