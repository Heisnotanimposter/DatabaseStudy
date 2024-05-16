//FirebaseCloudFunctiontoTriggerAWSLambda

const functions = require('firebase-functions');
const AWS = require('aws-sdk');

AWS.config.update({region: 'us-east-1'}); // Set your region
const lambda = new AWS.Lambda();

exports.triggerLambda = functions.firestore
    .document('path/to/document')
    .onCreate((snap, context) => {
        const data = snap.data();
        const params = {
            FunctionName: 'your_lambda_function_name',
            InvocationType: 'RequestResponse',
            Payload: JSON.stringify(data),
        };

        return lambda.invoke(params, (error, data) => {
            if (error) {
                console.error(JSON.stringify(error));
                return false;
            } else if (data) {
                console.log('Lambda function executed successfully:', data);
                return true;
            }
        });
    });