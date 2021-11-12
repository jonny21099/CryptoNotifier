# CryptoNotifier

## Introduction
### This is a configurable email notification program that notifies users when crypto prices have reached a specified amount. *This program uses API to retrieve prices, therefore users must be a member of either coinbase or coinmarketcap.* 

## Screenshots
### Running Program
![image](https://user-images.githubusercontent.com/43177180/127956167-38d09bf7-e888-42cf-9c81-57f77783ff1a.png)
### Sent Email
![image](https://user-images.githubusercontent.com/43177180/127956252-c1c356fe-f135-4539-a1a6-d81602eaa8e6.png)


## Setup
#### 1. (Coinbase Users) Obtain coinbase access key and secret key (grant these permissions: wallet:buys:read, wallet:sells:read, wallet:accounts:read).
####    (CoinMarketCap Users) Obtain coinmarketcap API key.
#### 2. Create a new file called .env the choice of program (either coinbase/ or coinmarketcap/).
#### 3. Copy template.env file to .env file.
#### 4. Copy access key and secret key into .env file depending on choice of method.
#### 5. Fill in the rest of the .env file.
#### 6. MORE DETAILS GUIDE ON HOW TO SETUP AWS SNS COMING SOON

## Environment Variables
#### Here are all the environment variable meanings followed by an example:
#### *Pick either COINBASE or CMC don't use both*
#### COINBASE_API_KEY: *for coinbase only Coinbase API Key.
#### COINBASE_API_SECRET: *for coinbase only Coinbase API Secret.
#### CMC_PRO_API_KEY: *for coinmarketcap only CoinMarketCap API Key.
```
COINBASE_API_KEY='yourapikey'
COINBASE_API_SECRET='yourapisecret'
            OR
CMC_PRO_API_KEY='yourapikey'
```
#### AWS_ACCESS_KEY_ID: aws acccount access key, works with IAM users as well.
#### AWS_SECRET_ACCESS_KEY: aws acccount secret key, works with IAM users as well.
#### SNS_TOPIC_ARN: aws sns topic arn.
```
AWS_ACCESS_KEY_ID='yourawsaccesskey'
AWS_SECRET_ACCESS_KEY='yourawssecretkey'
SNS_TOPIC_ARN='snstopicarn'
```
#### CURRENCY: Currency of price.
```
CURRENCY='USD'
```
#### *The order of these values must match*
#### CRYPTOS: The cryptos to get notifications about (Support multiple).
#### SELL_NOTIFICATION_VALUE: Get notifications to sell when crypto has reached this value (Support multiple). 
#### BUY_NOTIFICATION_VALUE: Get notifications to buy when crypto has reached this value (Support multiple).
```
CRYPTOS='BTC,ETH'
SELL_NOTIFICATION_VALUE='50,000,4,000'
BUY_NOTIFICATION_VALUE='20,000,1,000'
```
#### UPDATE_INTERVAL: How often to fetch value from Coinbase in seconds.
#### MESSAGE_INTERVAL: How often to send email (used to prevent spamming) in hours.
#### EMAIL_SENDER: What email you would like to send from.
#### EMAIL_SENDER_PASSWORD: Password of the sender email.
#### SMTP_SERVER: SMTP Server of the sender.
#### EMAIL_RECEIVER: Emails to receive notifications (Support multiple).
```
UPDATE_INTERVAL='300'
EMAIL_SENDER='senderemail@domain.com'
EMAIL_SENDER_PASSWORD='senderemailpassword'
SMTP_SERVER='smtp.domain.com'
EMAIL_RECEIVER='receiver1@domain.com,receiver2@domain.com,receiver3@domain.com'
```

## Run Program
#### The program takes in arguments to run the options are shown below.
```
python main.py smtp
or
python main.py sns
```

## Credits
#### All rights and credits for HTML and css [template](https://github.com/leemunroe/responsive-html-email-template) goes to Lee Munroe.

## Warnings
#### Do not give out your API_KEY or API_SECRET to anyone, this can give someone full access to your account.
#### When using a sender email it is recommended to create a new email for sending notifications.
