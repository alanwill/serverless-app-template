from aws_xray_sdk.core import patch_all
import logging
import boto3
import os
import sys
import json

# Path to modules needed to package local lambda function for upload
currentdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(currentdir, "./vendored"))

# Modules downloaded into the vendored directory
# from aws_xray_sdk.core import xray_recorder

# AWS X-Ray
patch_all()

# Logging
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# Initialize AWS services
dynamodb = boto3.resource('dynamodb')
ssm = boto3.client('ssm')

# Initialize variables
table_services = dynamodb.Table(os.environ['TABLE_SERVICES'])
key_pagerduty = ssm.get_parameter(Name='/' + os.environ['PARAMETER_PAGERDUTYKEY'])
session_pagerduty = APISession(key_pagerduty['Parameter']['Value'])


def handler(event, context):
    log.debug("Received event {}".format(json.dumps(event)))

    print("test")

    return
