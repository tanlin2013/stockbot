#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from '@aws-cdk/core';
import { CdkstackStack } from '../lib/cdkstack-stack';

const app = new cdk.App();
new CdkstackStack(app, 'CdkstackStack');
