import * as cdk from '@aws-cdk/core';
import { LambdaStack } from "./lambda-stack";
import { DynamoStack } from "./dynamo-stack";

export default function main(app: cdk.Construct) {
    new LambdaStack(app, "LambdaHandlers");
    // new DynamoStack(app, "DynamodbTables");
}