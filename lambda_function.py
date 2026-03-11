import json
import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    """
    Lambda function to automatically reboot EC2 instance when CloudWatch alarm triggers
    """
    
    # Extract instance ID from alarm event
    alarm_name = event['detail']['alarmName']
    instance_id = event['detail']['configuration']['metrics'][0]['metricStat']['metric']['dimensions']['InstanceId']
    
    print(f"Alarm triggered: {alarm_name}")
    print(f"Rebooting instance: {instance_id}")
    
    try:
        # Reboot the EC2 instance
        response = ec2.reboot_instances(InstanceIds=[instance_id])
        
        print(f"Successfully initiated reboot for instance {instance_id}")
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Instance reboot initiated successfully',
                'instanceId': instance_id
            })
        }
        
    except Exception as e:
        print(f"Error rebooting instance: {str(e)}")
        
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Failed to reboot instance',
                'error': str(e)
            })
        }
