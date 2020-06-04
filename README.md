# cc-proc
An AWS SQS message handler written in Python that send payments to a remote service.

## Pre-requisites
* Install Python 3.7.x
* Create an AWS account
* Install the AWS CLI: https://docs.aws.amazon.com/cli/index.html?nc2=h_ql_doc_cli

## Testing and packaging
To execute all unit tests from the root folder, from the console run: `python -m unittest discover -v -s test`

In order to send latest code changes to AWS, follow these steps:
* Zip the root `*.py` files and everything in the `dg` folder into a zip file
* Run the following to upload the code: `aws lambda update-function-code --function-name <aws function name> --zip-file fileb://<filename>.zip`

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
* How to install with 3rd party dependencies in AWS Lambda Layers: 
  * https://docs.aws.amazon.com/lambda/latest/dg/python-package.html
  * https://medium.com/@adhorn/getting-started-with-aws-lambda-layers-for-python-6e10b1f9a5d
  * https://gist.github.com/gene1wood/4a052f39490fae00e0c3#file-all_aws_lambda_modules_python3-7-txt