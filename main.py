import csv_write
from package.dependencies import *
import yaml

credentials = yaml.safe_load(open('credentials.yml'))


# I use the AWS SDK, "boto3", to query my ARNs(resources), keys(tags) and values. Then, append in the csv file
# 'tags.csv'
def main():
    csv_write.delete_csv_if_exists()
    csv_write.write_csv('resource', 'key', 'value')
    client = boto3.client('resourcegroupstaggingapi',
                          aws_access_key_id=credentials['aws_access_key_id'],
                          aws_secret_access_key=credentials['aws_secret_access_key'],
                          region_name='us-east-1'
                          )

    result = client.get_tag_keys()
    keys = result['TagKeys']
    for key in keys:
        result_values = client.get_tag_values(Key=key)
        values = result_values['TagValues']
        for value in values:
            result_resource = client.get_resources(
                TagFilters=[
                    {
                        'Key': key,
                        'Values': [
                            value
                        ]
                    }
                ]
            )
            resource = result_resource['ResourceTagMappingList'][0]['ResourceARN']
            csv_write.write_csv(resource, key, value)


main()
