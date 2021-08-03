# CryptoNotifier

## Introduction
### This is a configurable email notification program that notifies users when crypto prices have reached a specified amount. *This program uses coinbase API to retrieve prices, therefore users must be a member of coinbase.* 

## Screenshot
### Running Program
![image](https://user-images.githubusercontent.com/43177180/127956167-38d09bf7-e888-42cf-9c81-57f77783ff1a.png)
### Sent Email
![image](https://user-images.githubusercontent.com/43177180/127956252-c1c356fe-f135-4539-a1a6-d81602eaa8e6.png)


## Setup
#### 1. Obtain coinbase access key and secret key (no permissions needed to use this program).
#### 2. Create a new file called .env in the same directory as main.py.
#### 3. Copy template.env file to .env file.
#### 4. Copy coinbase access key and secret key into .env file.
#### 5. Fill in the rest of the .env file.

## Environment Variables
#### Here are all the environment variable meanings followed by an example:
#### COINBASE_API_KEY: Coinbase API Key.
#### COINBASE_API_SECRET: Coinbase API Secret.
#### CURRENCY: Currency of price.
```
COINBASE_API_KEY='yourapikey'
COINBASE_API_SECRET='yourapisecret'
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
#### UPDATE_INTERVAL: How often to fetch value from Coinbase.
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

## Credits
#### All rights and credits for HTML and css [template](https://github.com/leemunroe/responsive-html-email-template) goes to Lee Munroe.

## Warning
#### Do not give out your API_KEY or API_SECRET to anyone, this can give someone full access to your account.
#### When using a sender email it is recommended to create a new email for sending notifications.
