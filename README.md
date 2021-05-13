# Phish and Chips
A phishing email framework.

## About
**Phish and Chips** is an extendable phishing email framework designed to send realistic, personalised emails to as many people as you would like. If you have a template you'd like to use that isn't already here, you can easily add your own and keep firing away emails.

## General Usage
**Phish and Chips** is simple to use. Setup your list of recipients, specify your SMTP server details, choose your template and specify the sender name of your phishing email, and you are ready to go.

### 1. Setup Your List of Recipients
Before anything, you'll need to setup your list of recipients to send your phishing emails to.

Each recipient you specify needs 4 components:  

<ul>
<li>The recipient's email address</li>
<li>The recipient's full name</li>
<li>The recipient's first name</li>
<li>A 'record' entry for the recipient</li>
</ul>


These recipients must then be added to the **email-list** file, where each element is separated by a "**:**".

Below is an example of a valid **email-list** file:

```
sample@samples.com:Sample Guy:Sample:sample.guy
bobby@junior.com.au:Bobby Junior:Bobby:bobby.junior
#inactive@user.com:Inactive Fella:Inactive:inactive.fella
```

#### Commenting Out Users

Observing the above **email-list** file, you'll notice the third recipient, *inactive@user.com*, has a **#** as the first character.

The **#** is used to comment out a recipient. If you'd like to keep a recipient within your **email-list** file, but you don't want to send a phishing email to them right now, you can comment them out, and they will be ignored. Simply remove the **#** to include them in the next batch of phishing emails you send.



### 2. Specify Your SMTP Server Details

To send your phishing emails, you'll need the details of the SMTP server you are using.

This consists of:

<ul>
<li>SMTP server address</li>
<li>SMTP server port</li>
<li>SMTP username</li>
<li>SMTP password</li>
</ul>

You can either provide these details within **run.py** (see the first 4 empty variables), or supply them as command line arguments.



### 3. Start Phishing!

Once you've set up your list of recipients and SMTP details, you can start phishing.

Below is an example 

