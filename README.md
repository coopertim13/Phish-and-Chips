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

You can either provide these details within **phish.py** (see the first 4 empty variables), or supply them as command line arguments.  



### 3. Start Phishing!

Once you've set up your list of recipients and SMTP details, you can start phishing.

A list of available templates can be found within the *options* variable in **phish.py**:

```python
options = {"1": "LinkedIn"} # add to this as required
```

For example, if you'd like to send your phishing emails using the *LinkedIn* template, you'll need to specify `-e 1` when running **phish.py**.  

 

Below is a basic example run of **Phish and Chips**:

```bash
$ python3 phish.py -e 1 -s "LinkedIn Security Team" -v

,------. ,--.     ,--.       ,--.                            ,--.     ,-----.,--.     ,--.
|  .--. '|  ,---. `--' ,---. |  ,---.      ,--,--.,--,--,  ,-|  |    '  .--./|  ,---. `--' ,---.  ,---.
|  '--' ||  .-.  |,--.(  .-' |  .-.  |    ' ,-.  ||      ' .-. |    |  |    |  .-.  |,--.| .-. |(  .-'
|  | --' |  | |  ||  |.-'  `)|  | |  |    \ '-'  ||  ||  |\ `-' |    '  '--'\|  | |  ||  || '-' '.-'  `)
`--'     `--' `--'`--'`----' `--' `--'     `--`--'`--''--' `---'      `-----'`--' `--'`--'|  |-' `----'
                                                                                          `--'

Sending emails...

Email sent to Sample Guy (sample@samples.com)
Email sent to Bobby Junior (bobby@junior.com.au)

Sent 2 email(s)
```

In the above example, it is assumed that the SMTP details have been supplied within **phish.py**.

If you'd like to supply this information via command line arguments instead, you can do something like the following:

```bash
$ python3 phish.py -e 1 -s "LinkedIn Security Team" -a smtp.gmail.com -c 587 -u fake@gmail.com -p ILoveFakeStuff!! -v
```

You can use both command line arguments and the in-built variables to specify the SMTP server details, but the command line arguments will take precedence.  



## Command Line Arguments

Below are all of the command line arguments for **Phish and Chips**:

```bash
$ python3 phish.py -h      

,------. ,--.     ,--.       ,--.                            ,--.     ,-----.,--.     ,--.
|  .--. '|  ,---. `--' ,---. |  ,---.      ,--,--.,--,--,  ,-|  |    '  .--./|  ,---. `--' ,---.  ,---.
|  '--' ||  .-.  |,--.(  .-' |  .-.  |    ' ,-.  ||      ' .-. |    |  |    |  .-.  |,--.| .-. |(  .-'
|  | --' |  | |  ||  |.-'  `)|  | |  |    \ '-'  ||  ||  |\ `-' |    '  '--'\|  | |  ||  || '-' '.-'  `)
`--'     `--' `--'`--'`----' `--' `--'     `--`--'`--''--' `---'      `-----'`--' `--'`--'|  |-' `----'
                                                                                          `--'

usage: phish.py [-h] -e email template -s sender name [-u username] [-p password] [-a server address] [-c server port] [-v]

A phishing email framework.

optional arguments:
  -h, --help         show this help message and exit
  -e email template  email template to send
  -s sender name     name of sender for phishing email
  -u username        SMTP username
  -p password        SMTP password
  -a server address  SMTP server address
  -c server port     SMTP server port
  -v                 enable verbose output
```

