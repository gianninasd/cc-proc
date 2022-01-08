# cc-proc
An AWS SQS message handler written in Python that send payments to a remote service.

## Pre-requisites
* Install Python 3.7.x
* Install Python 3rd Party packages:
  * `pip3 install boto3` 
  * `pip3 install requests` 
* Create an AWS account
* Install the AWS CLI: https://docs.aws.amazon.com/cli/index.html?nc2=h_ql_doc_cli

## Testing and packaging
* To execute all unit tests, run: `python3 -m unittest discover -v -s test`
* To generate the build archive, run: `gradle createArchive`
* To upload the archive to AWS, run: `gradle awsUpload`

Use the following sample event data for testing via AWS Lambda:
````
{
  "Records": [
    {
      "body": "aws-test-633151,7,6277411477100000,10,2025,Steve,Rogers,rick@sdf3.com,M5H 2N2"
    },
    {
      "body": "aws-test-306478,2300,4500030000000004,10,2029,Peggy,Carter,rick@sdf3.com,M5H 2N2"
    }
  ]
}
````

## References
* https://docs.aws.amazon.com/lambda/latest/dg/python-package.html

In order to install 3rd party dependencies in an AWS Lambda Layer, the important part is to
put all the contents in a `python` directory and then create your ZIP file
* https://medium.com/@adhorn/getting-started-with-aws-lambda-layers-for-python-6e10b1f9a5d
* https://gist.github.com/gene1wood/4a052f39490fae00e0c3#file-all_aws_lambda_modules_python3-7-txt
* https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html