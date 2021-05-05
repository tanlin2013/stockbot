#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from '@aws-cdk/core';
import { MasterStack } from '../lib/master-stack';

const app = new cdk.App();
new MasterStack(app, 'StockbotStack');
