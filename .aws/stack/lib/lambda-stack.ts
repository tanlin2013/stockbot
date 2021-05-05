import * as cdk from '@aws-cdk/core';
import * as lambda from '@aws-cdk/aws-lambda';
import * as ecr from '@aws-cdk/aws-ecr';
import * as apigateway from '@aws-cdk/aws-apigateway';
import * as events from '@aws-cdk/aws-events';
import * as targets from '@aws-cdk/aws-events-targets';
import * as path from 'path';


export class LambdaStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here

    const repo = new ecr.Repository(this, 'Repository');

    new lambda.DockerImageFunction(this, 'ECRFunction', {
      code: lambda.DockerImageCode.fromEcr(repo),
    });

    new lambda.Function(this, 'dynamo', {
      code: lambda.Code.fromAsset(path.join(__dirname, 'dynamo-handler')),
      handler: 'functions/dynamo/handler.handler',
      runtime: lambda.Runtime.PYTHON_3_7,
    });

    new lambda.Function(this, 'telegram', {
      code: lambda.Code.fromAsset(path.join(__dirname, 'telegram-handler')),
      handler: 'functions/telegram/handler.handler',
      runtime: lambda.Runtime.PYTHON_3_7,
    });

    const lambdaTrading = new lambda.Function(this, 'trading', {
      code: lambda.Code.fromAsset(path.join(__dirname, 'trading-handler')),
      handler: 'functions/trading/handler.handler',
      runtime: lambda.Runtime.PYTHON_3_7,
    });

    const rule = new events.Rule(this, 'Rule', {
        schedule: events.Schedule.expression('cron(0 18 * ? MON-FRI *)')
    });
    rule.addTarget(new targets.LambdaFunction(lambdaTrading));

    const api = new apigateway.RestApi(this, 'api', {
      description: 'example api gateway',
      deployOptions: {
        stageName: 'dev',
      },
      // 👇 enable CORS
      defaultCorsPreflightOptions: {
        allowHeaders: [
          'Content-Type',
          'X-Amz-Date',
          'Authorization',
          'X-Api-Key',
        ],
        allowMethods: ['OPTIONS', 'GET', 'POST', 'PUT', 'PATCH', 'DELETE'],
        allowCredentials: true,
        allowOrigins: ['http://localhost:3000'],
      },
    });

    // 👇 create an Output for the API URL
    new cdk.CfnOutput(this, 'apiUrl', {value: api.url});

  }
}