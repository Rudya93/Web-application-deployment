#!/usr/bin/env python
from collections import defaultdict
import boto3

ec2 = boto3.resource("ec2", region_name="eu-west-2")

vpc = ec2.Vpc("vpc-0f287cc8ae36b639d")

# Get information for all running instances
running_instances = ec2.instances.filter(Filters=[{
'Name': 'instance-state-name', 'Values': ['running','stopped']}])

ec2info = defaultdict()
for instance in running_instances:
    for tag in instance.tags:
        if 'Name'in tag['Key']:
            name = tag['Value']
    # Add instance info to a dictionary
    ec2info[instance.id] = {
        'Name': name,
        'Type': instance.instance_type,
        'State': instance.state['Name'],
        'Private IP': instance.private_ip_address,
        'Public IP': instance.public_ip_address,
        'Launch Time': instance.launch_time
        }

attributes = ['Name', 'Type', 'State', 'Private IP', 'Public IP', 'Launch Time']
for instance_id, instance in ec2info.items():
    for key in attributes:
        print("{0}: {1}".format(key, instance[key]))
    print("------")
