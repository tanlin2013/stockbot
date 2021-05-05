import * as cdk from '@aws-cdk/core';
import * as dynamodb from '@aws-cdk/aws-dynamodb';
import * as lambda from '@aws-cdk/aws-lambda';
import * as sqs from '@aws-cdk/aws-sqs';
import { DynamoEventSource, SqsDlq } from '@aws-cdk/aws-lambda-event-sources';


export class LambdaStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here

    const table = new dynamodb.Table(..., {
      partitionKey: ...,
      stream: dynamodb.StreamViewType.NEW_IMAGE // make sure stream is configured
    });

    const deadLetterQueue = new sqs.Queue(this, 'deadLetterQueue');

    const function = new lambda.Function(...);
    function.addEventSource(new DynamoEventSource(table, {
      startingPosition: lambda.StartingPosition.TRIM_HORIZON,
      batchSize: 5,
      bisectBatchOnError: true,
      onFailure: new SqsDlq(deadLetterQueue),
      retryAttempts: 10
    }));

  }
}