import * as cdk from '@aws-cdk/core';
import * as lambda from '@aws-cdk/aws-lambda';
import * as apigateway from '@aws-cdk/aws-apigateway';
import { PythonFunction } from '@aws-cdk/aws-lambda-python';
import axios from 'axios';

export class LambdaStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // 👇 Define layers for custom module dependencies
    // new lambda.LayerVersion(this, 'DynamoLayer', {
    //   compatibleRuntimes: [
    //     lambda.Runtime.PYTHON_3_7,
    //   ],
    //   code: lambda.Code.fromAsset('lib/dynamo'),
    // });

    // 👇 Create lambda function - telegram handler
    const telegramHandler = new PythonFunction(this, 'TelegramHandler', {
      entry: 'src/telegram',
      index: 'app.py',
      runtime: lambda.Runtime.PYTHON_3_7,
      environment: {
        'TELEGRAM_API_ID': process.env.TELEGRAM_API_ID!,
        'TELEGRAM_API_HASH': process.env.TELEGRAM_API_HASH!,
        'TELEGRAM_BOT_TOKEN': process.env.TELEGRAM_BOT_TOKEN!,
        'TELEGRAM_DB_KEY': process.env.TELEGRAM_DB_KEY!,
      },
    });

    // API Gateway
    const api = new apigateway.LambdaRestApi(this, 'TelegramEndpoint', {
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
    // const tradingHandler = new lambda.Function(this, 'TradingHandler', {
    //   code: lambda.Code.fromAsset('src/trading'),
    //   handler: 'app.handler',
    //   runtime: lambda.Runtime.PYTHON_3_7,
    // });

    // 👇 Create lambda function - daily examiner
    // const dailyExaminer = new lambda.Function(this, 'DailyExaminer', {
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
    new cdk.CfnOutput(this, 'API url', {value: api.url});
    new cdk.CfnOutput(this, 'Lambda Function Name', {
      value: telegramHandler.functionName
    })
    // new cdk.CfnOutput(this, 'Trading Function Name', {
    //   value: tradingHandler.functionName
    // })

    // 👇 Register webhook
    const url: string = `https://api.telegram.org/bot${process.env.TELEGRAM_BOT_TOKEN}/setWebhook?url=${api.url}`;
    
    const getRequest = async () => {
      try {
        const response = await axios.get(url);
        console.log(response.data);
      } catch (exception) {
        process.stderr.write(`ERROR received from ${url}: ${exception}\n`);
      }
    };
    getRequest()
  }
}