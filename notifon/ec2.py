# ipython session output for ec2 instance creation

# coding: utf-8
import boto3

# creating ec2 session
session = boto3.Session(profile_name='pythonAutomation')
ec2 = session.resource('ec2')

# creating ssh key
key_name = 'python_automation_key'
key_path = key_name + '.pem'
key = ec2.create_key_pair(KeyName=key_name)
key.key_material
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')

# securing ssh key
import os, stat
# changing file mode, allowing user to change and write file
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')

# getting amazon ec2 AMI
img = ec2.Image('ami-922914f7')
img.name
ami_name = 'amzn-ami-hvm-2018.03.0.20180508-x86_64-gp2'
filters = [{'Name': 'name', 'Values': [ami_name]}]
list(ec2.images.filter(Owners=['amazon'], Filters=filters))

# creating ec2 instance
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
inst = instances[0]
inst.wait_until_running()
inst.public_dns_name
inst.security_groups

# Look up the security group
# Authorize incoming connections from our public IP address, on port 22 (the port SSH uses)
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])

myIP = 'your public IP goes here'
sg.authorize_ingress(
    IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': myIP}]}])
sg.authorize_ingress(
    IpPermissions=[{'FromPort': 80, 'ToPort': 80, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}])
inst.public_dns_name
