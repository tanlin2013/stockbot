import * as cdk from '@aws-cdk/core';
import * as lambda from '@aws-cdk/aws-lambda';
import { PythonFunction } from "@aws-cdk/aws-lambda-python";
import * as apigateway from '@aws-cdk/aws-apigateway';
import * as events from '@aws-cdk/aws-events';
import * as targets from '@aws-cdk/aws-events-targets';
import * as acm from "@aws-cdk/aws-certificatemanager";

export class LambdaStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // 👇 Create lambda function - telegram handler
    const telegramHandler = new PythonFunction(this, 'telegram', {
      entry: 'src/telegram',
      runtime: lambda.Runtime.PYTHON_3_7,
      environment: {
        region: cdk.Stack.of(this).region,
        TELEGRAM_API_ID: process.env.TELEGRAM_API_ID,
        TELEGRAM_API_HASH: process.env.TELEGRAM_API_HASH,
        TELEGRAM_BOT_TOKEN: process.env.TELEGRAM_BOT_TOKEN,
        TELEGRAM_DB_KEY: process.env.TELEGRAM_DB_KEY,
        TELEGRAM_CHAT_ID: process.env.TELEGRAM_CHAT_ID,
      },
    });

    // API Gateway
    const api = new apigateway.RestApi(this, 'Telegram-Endpoint', {
      handler: telegramHandler,
      deployOptions: {
        stageName: 'dev',
      },
      // enable CORS
    //   defaultCorsPreflightOptions: {
    //     allowHeaders: [
    //       'Content-Type',
    //       'X-Amz-Date',
    //       'Authorization',
    //       'X-Api-Key',
    //     ],
    //     allowMethods: ['OPTIONS', 'GET', 'POST', 'PUT', 'PATCH', 'DELETE'],
    //     allowCredentials: true,
    //     allowOrigins: ['https://api.telegram.org'],
    //   },
    });

    // 👇 Create lambda function - trading handler
    new PythonFunction(this, 'trading', {
      entry: 'src/trading',
      runtime: lambda.Runtime.PYTHON_3_7,
    });

    // 👇 Create lambda function - daily examiner
    // const dailyExaminer = new lambda.Function(this, 'daily_examiner', {
    //   code: lambda.Code.fromAsset('src/daily_examiner'),
    //   handler: 'app.handler',
    //   runtime: lambda.Runtime.PYTHON_3_7,
    // });

    // Schedule lambda with contab
    // const rule = new events.Rule(this, 'Rule', {
    //     schedule: events.Schedule.expression('cron(0 18 * ? MON-FRI *)')
    // });
    // rule.addTarget(new targets.LambdaFunction(dailyExaminer));

    // 👇 Create outputs
    new cdk.CfnOutput(this, 'apiUrl', {value: api.url});

  }
}