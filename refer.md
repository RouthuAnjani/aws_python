# S3 Buckets

1. Search for `S3` and open s3 console
1. Click on `Create Bucket` button
1. Provide options for new bucket
    - Choose region of your choice
    - Choose Bucket type : General (Available in few regions)
    - Choose Globally Unique name (lowercase without space)
    - Object Ownership : Disable ACL [ Access Control Lists ]
    - Block Public Access
    - Tags : User=mahendra
1. Click `Create Bucket`
1. Click `Upload` button then `Add file` to upload any local file to S3 bucket
1. Click on newly uploaded file name and then scroll down for "Storage Class" segement
1. Click on `Edit` button to edit storage class
1. Explore all the class types
1. Save the changes if any












# SQS

Sending a Message to SQS:

import boto3
# Create an SQS client
sqs = boto3.client('sqs', region_name='your-region')
# Specify the URL of your SQS queue
queue_url = 'your-queue-url'
# Send a message to the queue
response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody='Hello, SQS!'
)
print("Message sent. Message ID:", response['MessageId'])


Receiving Messages from SQS:

import boto3
# Create an SQS client
sqs = boto3.client('sqs', region_name='your-region')
# Specify the URL of your SQS queue
queue_url = 'your-queue-url'
# Receive messages from the queue
response = sqs.receive_message(
    QueueUrl=queue_url,
    MaxNumberOfMessages=5,  # Adjust as needed
    VisibilityTimeout=60,   # Adjust as needed
    WaitTimeSeconds=20      # Adjust as needed
)
messages = response.get('Messages', [])
# Process received messages
for message in messages:
    receipt_handle = message['ReceiptHandle']
    body = message['Body']
    print("Received message:", body)
    # Add your processing logic here
    # Delete the message from the queue after processing
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle
    )








# SNS

Write Python Code to Publish a Message to SNS

import boto3
# Create an SNS client
sns = boto3.client('sns', region_name='your-region')
# Specify the ARN of your SNS topic
topic_arn = 'your-topic-arn'
# Publish a message to the topic
response = sns.publish(
    TopicArn=topic_arn,
    Message='Hello, SNS!'
)
# Print the message ID
print("Message published. Message ID:", response['MessageId'])










# BeanStalk

1.  Convert entire folder `flask-app` to a ZIP file, make sure ZIP file contains all the files.

    > The ready to deploy ZIP is available [here](./flask-app.zip)

1.  Create a new BeanStalk with Python 3.11 environment

1.  Go to "Beanstalk Console" and click "Create Application" button

1.  Enter name of application (I have used `demo1`) and click `Create` button.

1.  Once application is created, use `Create new Environment` button.

1.  Choose type `Web Server Environment` and scroll down

1.  Enter the domain name and use button `Check Availability`, scroll down if domain is available, try with different name if not available.

1.  Platform selection: Python, Python 3.11 and scroll down

1.  Choose Application code : `Upload your code` and enter version label `version-1` and choose `Local file`, you need to select the ZIP file of application. Scroll down

1.  Choose `Preset` => Single Instance  and click `Next`

1.  On next screen, choose service role (if exists) otherwise choose "Create New" option. Also select any existing EC2 Key Pair.  And choose EC2 Profile created earlier 

    > Refer to [EC2 Profile for ELB](../../Learning/13-IAM-Role-for-ELB-EC2.md) for creating this EC profile.

    Click `Next` to continue.

1.  Choose any existing VPC (with Public Subnets) and scroll down.

1.  Choose all the subnets and scroll down

1.  Scroll down to `Next` button and click on `Next`.

1.  Ignore all the options, scroll down and click `Next`

1.  Choose `Basic` health monitoring and scroll down.

1.  Disable the `Managed Updates` and scroll down for `Next` button.

1.  Click the `Next` button.

1.  Scroll down and click `Submit` button.






# RDS

Create a New DB Instance
Click on the "Create database" button.

Choose the "Standard create" option.

Select the "Engine options" as "MySQL."

Choose the appropriate version of MySQL for your application (I Prefer latest version).

In the "Templates" section, you can choose a predefined template or create a custom one.

In the "Settings" section:

Set a DB instance identifier (a name for your RDS instance).
Set a Master username and password (these credentials will be used to access the MySQL database).
Choose a DB instance size (the computing and memory capacity).
Optionally, configure the storage settings and enable Multi-AZ for high availability.
In the "DB instance size" section, select the appropriate instance size.

Configure the storage settings, including allocated storage and whether to enable automatic storage scaling.

In the "Connectivity" section:

Choose the VPC (Virtual Private Cloud) where you want to launch the RDS instance.
Configure the subnet group and choose the security group settings.
Configure public accessibility if needed.
In the "Database authentication" section, choose the authentication method (password authentication is common).

In the "Additional configuration" section, configure additional settings if necessary.

Click "Create database" to start the RDS instance creation.

Step 4: Wait for the RDS Instance to be Ready
The RDS instance creation may take some time. You can monitor the progress on the RDS dashboard. Once the status is "available," your RDS instance is ready to use.

Step 5: Connect to the MySQL Database
Retrieve the endpoint of your RDS instance from the RDS dashboard.

Use a MySQL client (e.g., MySQL Workbench, MySQL command-line client) to connect to the RDS instance using the provided endpoint, master username, and password.

You may use SQLTools MySQL/MariaDB extension of VSCode to connect

My Sample Database connection string

MySQL-Endpoint = sampledb.cimr0kdyqj64.us-east-1.rds.amazonaws.com
Username = admin
Password = Password!123
Default-Database = sys
Step 6: Manage Your MySQL Database
Once connected, you can manage your MySQL database as you would with any other MySQL instance. Create databases, tables, and users, and execute queries based on your application requirements.

Database creation (Schema)

create schema sampledb;
Sample Table creation

use sampledb;

CREATE TABLE employees
( empid int primary key auto_increment,
firstname varchar(20),
lastname varchar(30) );

INSERT into employees (firstname, lastname)
VALUES ('Donald','Duck');

INSERT into employees (firstname, lastname)
VALUES ('Micky','Mouse');




# ElasticBeanStalk

Creating a new Elastic Beanstalk application using the AWS Management Console involves several steps. Here's a step-by-step guide:

Step 1: Log in to AWS Console
Open your web browser and go to the AWS Management Console.
Log in with your AWS account credentials.
Step 2: Navigate to Elastic Beanstalk
In the AWS Management Console, search for "Elastic Beanstalk" in the services search bar or navigate to the "Compute" section and select "Elastic Beanstalk."
Step 3: Create a New Elastic Beanstalk Application
Click on the "Create Application" button.

Application Information:

Application name: Enter a name for your application.
Description: Optionally, provide a description.
Click "Create."

Step 4: Create an Environment
After creating the application, click on the "Create a new environment" button.

Select a Platform:

Choose a platform that matches your application. For example, if you have a Python application, select the appropriate Python version.
Environment Information:

Environment name: Enter a name for your environment.
Domain: Choose between a web server environment for HTTP applications or a worker environment for background processing.
Application Code:

Choose the source of your application code. You can either upload your code, use a sample application, or connect to a code repository.
Click "Create Environment."

Step 5: Wait for Environment Creation
AWS Elastic Beanstalk will create the necessary resources for your environment. This may take a few minutes.

Once the environment is created, you'll see the environment dashboard with information about your application, environment URL, and more.

Step 6: Access Your Application
In the Elastic Beanstalk environment dashboard, find the URL under the "Environment URL" section.

Open the provided URL in a web browser to access your deployed application.






# DynamoDB Demo

Sign in to the AWS Management Console:

Go to the AWS Management Console (https://aws.amazon.com/), and sign in with your AWS account credentials.
Navigate to DynamoDB:

Once signed in, navigate to the DynamoDB service. You can find it under the "Database" section in the AWS Management Console.
Click "Create Table":

In the DynamoDB dashboard, click on the "Create table" button to begin the table creation process.
Enter Table Details:

Provide a name for your table in the "Table name" field.
Specify the primary key for your table. You can choose between a simple primary key (partition key) or a composite primary key (partition key and sort key).
Set the data types for your primary key attributes.
Configure Provisioned Throughput or Use On-Demand:

DynamoDB allows you to choose between Provisioned and On-Demand capacity modes.
For Provisioned Throughput, specify the desired read and write capacity units.
For On-Demand, you don't need to specify capacity; DynamoDB automatically scales based on actual consumption.
Configure Additional Settings:

Expand the "Additional settings" section to configure optional settings, such as encryption, auto-scaling, and DynamoDB Streams.
You can also enable a Time to Live (TTL) attribute if you want to automatically delete items after a certain period.
Create Table:

Once you've configured all the settings, click the "Create" button to create your DynamoDB table.
Table Creation Confirmation:

DynamoDB will take a few moments to create the table. Once the table is created, you will see a confirmation message.






# VPC-EC2

Create EC2 instances inside a VPC

VPC and Subnet
Create a new VPC "app1" with additional tag user=mahendra

IP Address Range : 10.0.0.0/16
Create THREE new Public Subnets

Subnet-A-AVzone-a : 10.0.1.0/24
Subnet-B-AVzone-b : 10.0.2.0/24
Subnet-C-AVzone-c : 10.0.3.0/24
Create the FIRST ec2 instance in First Subnet
Search for EC2 and click to open EC2 Console

Click on Launch Instance

Use Display name web1, use Additional tags user=mahendra

Choose AMI (Template/Image) : Ubuntu

Choose the EC2 Instance Size : t2.micro or t3.micro

For Key pair, use option Create new key pair

Your browser should auto-download the .pem file.

In Network Settings, use EDIT button to modify settings

Choose the network created in previous steps
Choose First Subnet (Should be in AZ a)
Enable Auto assign Public IP
For Security Group choose option to Create new security group

Enter name of security group mahendra-sg
Add new rule (Use Add security group rule button) . Use protocol HTTP and Source Anywhere . Click Save
Click Create Instance and wait for EC2 instance to be ready.




# Demo 2 : Setup `Website` inside EC2 instance

1. Login into AWS Console and find your EC2 instance. 
   
    > Filter using tag `user=mahendra`

1. Copy the `Public IP` of EC2 instance. Also find the location of PEM file downloaded in `demo-1`

    > Default location of PEM would be `~\Downloads\key101.pem`

    > the filename depends on name of key

1.  Launch `Windows Powershell` from Start menu and use following commands

    ```pwsh
    cd Downloads
    dir *.pem
    ```

1.  Use following command, to ENTER inside Linux Server USING SSH protocol

    ```pwsh
    # ssh  -i PEM_FILE ubuntu@PUBLIC_IP_EC2
    ssh -i key101.pem ubuntu@3.93.172.183
    TRUST THIS SERVER ? > yes
    ## The prompt has been changed from Powershell to BASH shell (Linux Shell)
    ## Install NGINX
    sudo apt update -y
    sudo apt install nginx -y
    ```
 
1.  Verify the location of default `index.html` file in linux server.

    ```bash
    cd /var/www/html
    cat index.html
    # If the file exists, its contents should be displayed
    ```

1.  Try accessing this website from Browser `http://PUBLIC_IP_EC2`

1.  Go back to SSH prompt and use following commands to EXIT from linux server.

    ```pwsh
    exit
    # The prompt should be changed from Linux to Windows
    ```

1.  To copy files from Local (Windows) filesystem to linux filesystem we use following command:

    ```bash
    # SYNTAX
    scp -i PEM_FILE  SOURCE_FILE_PATH   USER@PUBLIC_IP:LINUX_DESTINATION_PATH
    ```

    ```pwsh
    scp -i key101.pem  D:\git\aws-kpit\demos\src\index.html  ubuntu@3.93.172.183:/home/ubuntu
    scp -i key101.pem  D:\git\aws-kpit\demos\src\main.css  ubuntu@3.93.172.183:/home/ubuntu
    ```

1.  Login with SSH and Move the files to correct location.

    ```pwsh
    ssh -i key101.pem ubuntu@3.93.172.183 
    ls 
    sudo mv * /var/www/html/
    exit
    ```

1.  Revisit the URL `http://PUBLIC_IP_EC2`



# Demo 3 : Load Balancer Demo

> Setup a load-balancer (Elastic Load Balancer) to distribute the incoming traffic (HTTP) to three EC2 instances in target group

## Resources that can be `shared` by multiple EC2 instance

    - VPC and Subnet
    - Security Group
    - Key Pair
    - Load Balancer

## Create the FIRST ec2 instance


1. Search for `EC2` and click to open `EC2` Console
1. Click on `Launch Instance`
1. Use Display name `web-1`, use Additional tags `user=mahendra`
1. Choose AMI (Template/Image) : `Ubuntu`
1. Choose the EC2 Instance Size : `t2.micro` or `t3.micro`
1. For Key pair, use option 'Select Existing' and then choose `key101`

1. In Network Settings, use `EDIT` button to modify settings

    - Choose the network created in previous steps
    - Choose First Subnet (Should be in AZ `a`)
    - Enable `Auto assign Public IP`

1. For `Security Group` choose option to `Select Existing` and choose `mahendra-sg`

1.  Click `Create Instance` and wait for EC2 instance to be ready.

## Create the SECOND ec2 instance

1. Search for `EC2` and click to open `EC2` Console
1. Click on `Launch Instance`
1. Use Display name `web-2`, use Additional tags `user=mahendra`
1. Choose AMI (Template/Image) : `Ubuntu`
1. Choose the EC2 Instance Size : `t2.micro` or `t3.micro`
1. For Key pair, use option 'Select Existing' and then choose `key101`

1. In Network Settings, use `EDIT` button to modify settings

    - Choose the network created in previous steps
    - Choose Second Subnet (Should be in AZ `b`)
    - Enable `Auto assign Public IP`

1. For `Security Group` choose option to `Select Existing` and choose `mahendra-sg`

1.  Click `Create Instance` and wait for EC2 instance to be ready.

## Create the THIRD ec2 instance

1. Search for `EC2` and click to open `EC2` Console
1. Click on `Launch Instance`
1. Use Display name `web-3`, use Additional tags `user=mahendra`
1. Choose AMI (Template/Image) : `Ubuntu`
1. Choose the EC2 Instance Size : `t2.micro` or `t3.micro`
1. For Key pair, use option 'Select Existing' and then choose `key101`

1. In Network Settings, use `EDIT` button to modify settings

    - Choose the network created in previous steps
    - Choose Third Subnet (Should be in AZ `c`)
    - Enable `Auto assign Public IP`

1. For `Security Group` choose option to `Select Existing` and choose `mahendra-sg`

1.  Click `Create Instance` and wait for EC2 instance to be ready.

## Install the necessory packages (nginx) inside all three instances

1. Using either Command prompt or Powershell connect the instance 'web-1'

    ```
    ssh -i key101.pem ubuntu@WEB-1-PUBLIC_IP
    sudo apt update -y
    sudo apt install nginx -y
    ```

1. Using either Command prompt or Powershell connect the instance 'web-2'

    ```pwsh
    ssh -i key101.pem ubuntu@WEB-2-PUBLIC_IP
    sudo apt update -y
    sudo apt install nginx -y
    ```

1. Using either Command prompt or Powershell connect the instance 'web-3'

    ```pwsh
    ssh -i key101.pem ubuntu@WEB-3-PUBLIC_IP
    sudo apt update -y
    sudo apt install nginx -y
    ```

1.  Copy the original HTML and CSS file inside 'web-1'

    ```pwsh
    scp -i key101.pem  D:\git\aws-kpit\demos\src\index.html  ubuntu@WEB-1-PUBLIC_IP:/home/ubuntu
    scp -i key101.pem  D:\git\aws-kpit\demos\src\main.css  ubuntu@WEB-1-PUBLIC_IP:/home/ubuntu
    ssh -i key101.pem ubuntu@WEB-1-PUBLIC_IP
    ls
    sudo mv * /var/www/html
    ```

1.  Modify index.html, add web-2 somewhere in H1 or page title

1.  Copy the original HTML and CSS file inside 'web-2'

    ```pwsh
    scp -i key101.pem  D:\git\aws-kpit\demos\src\index.html  ubuntu@WEB-2-PUBLIC_IP:/home/ubuntu
    scp -i key101.pem  D:\git\aws-kpit\demos\src\main.css  ubuntu@WEB-2-PUBLIC_IP:/home/ubuntu
    ssh -i key101.pem ubuntu@WEB-2-PUBLIC_IP
    ls
    sudo mv * /var/www/html
    ```

1.  Modify index.html, add web-3 somewhere in H1 or page title

1.  Copy the original HTML and CSS file inside 'web-3'

    ```pwsh
    scp -i key101.pem  D:\git\aws-kpit\demos\src\index.html  ubuntu@WEB-3-PUBLIC_IP:/home/ubuntu
    scp -i key101.pem  D:\git\aws-kpit\demos\src\main.css  ubuntu@WEB-3-PUBLIC_IP:/home/ubuntu
    ssh -i key101.pem ubuntu@WEB-3-PUBLIC_IP
    ls
    sudo mv * /var/www/html
    ```

1.  Verify if application is running in ALL THREE instances

    Open THREE browser windows, each trying access Public IP of each EC2 instance

## Create a Target group with HTTP Health probe

1.  In `EC2 Console`, scroll down navigation bar (left sidebar) for "Load Balancering". Click "Target Groups"

1.  Click `Create Target Group`, then choose `Instances` 

    - Provide target group name `webapp-group`
    - Choose protocol `HTTP` > HTTP/1
    - Choose VPC (same as EC2 instances)
    - In Health probe, select HTTP and click `Advance Health check settings`
        * Either modify or accept the default values for
            - Healthy Threshold
            - Unhealthy Threshold
            - timeout
            - interval
            - Success Code [200]
    - Click Next button
    - Select all the EC2 instance and click `Include as pending below`
    - Click `Create Target group` button

## Create a new Application Load Balancer

1.  In `Load Balancing` select Load Balancer > Click `Create Load Balancer`
1.  Choose `Application Load Balancer` -> `Create`
1.  Provide following details for new load balancer
    - Name: app1-l
    - Scheme: internet [Public IP]
    - VPC : Same as EC2 instances
    - Subnet : Select Any TWO minimum
    - Security Group : Choose same one as EC2 instances
    - Listener : Port-> 80, Target Group -> webapp-group
1.  Now click `Create load balancer` button
1.  Wait for 2-3 minutes and check the `Status` of load balancer, once status is `Active`, use the DNS name of load balancer in new browser it should be similar to `http://app1-lb-1840556944.us-east-1.elb.amazonaws.com/`

## Clean Up

1.  All the resources should be delete in THIS order

    1. Load Balancer
    2. Target Group
    3. EC2 Instance
    4. Security Group
    5. VPC







# Python (Flask) Web application on BeanStalk

1. Create a new folder for python project

    ```cmd
    mkdir flask-app
    cd flask-app
    ```

1.  Inside 'flask-app' folder create a new file `app.py`

    ```python
    from flask import Flask, render_template

    app = Flask(__name__)

    @app.route("/")
    def hello():
        return render_template('index.html')
    ```

1.  Create HTML Template `index.html` inside folder 'templates' 

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <link href="{{ url_for('static',filename='css/main.css') }}" rel="stylesheet"/>
        <title>Docker [Python] Demo </title>
    </head>
    <body>
        <div class="header">
        <h1>Hello Python World!</h1>
        </div>
        <div class="content">
        <p>Welcome to FlaskApp!</p>
        </div>
    </body>
    </html>
    ```

1.  Create the CSS file `main.css` in a another folder `static\css`

    ```css
    * {
        margin: 0px;
        padding: 0px;
    }

    .header {
        padding: 10px;
        background-color: cadetblue;
        font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
        border-bottom: 5px solid darkkhaki;
    }

    .content {
        background-color: wheat;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        padding: 5px;
        text-align: justify;
        height: 700px;
    }
    ```









# Creating IAM Role for EC2 instances in ELB Environment

> This one is `One time Activity` and follow these steps only if you get ERROR while creating BeanStalk environment `Choose EC2 Profile` or `Incorrect EC2 profile`

1. Search for  `IAM` and open IAM Console
1. In `IAM Console` on left side menu, click on `Roles` and then `Create Role`

1. Choose Trusted entity type `AWS Services` and then use-case `EC2`

1.  Search for Permissions `AWSElasticBeanstalkWebTier` and once found, use checkbox to select and then click `Next`

1.  Provide a new name for the role, you should use this role as `EC2 profile` later in Elastic BeanStalk Environment.