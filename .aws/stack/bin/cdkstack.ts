#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from '@aws-cdk/core';
import main from '../lib/index';

const app = new cdk.App();
main(app);
