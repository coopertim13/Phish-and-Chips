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



## Including Your Own Templates

**Phish and Chips** has been built to be adaptable. If you have a HTML template you want to include, it's easy to add it in.

### 1. Make a New Class

First thing you are going to need is a new class. Make a new Python file in the root directory with the same name as your class (for example, ***Happy.py***) and setup a class that inherits the **EmailTemplate** class.

For example:

**Happy.py**

```python
import EmailTemplate

class Happy(EmailTemplate.EmailTemplate):
	def __init__(self, email, full_name, first_name, record, sender_name, recipient):
		super().__init__(email, full_name, first_name, record, sender_name, recipient, content, "Happy Subject")

content = """
  <!DOCTYPE html>
  <head>
  <title>Happy Email</title>
  </head>
  <body>
  Hello {first_name}, I hope you're happy!
  </body>
  </html>
"""
```

You'll need to include a variable, **content**, that is passed as the second last parameter of the ***super().\_\_init\_\_()*** function. You'll also need to pass in the subject for all emails sent with this template. In this example, the subject is ***Happy Subject***. 

#### Some Notes About HTML Content

- All HTML content is automatically formatted via the **EmailTemplate** parent class

- Any instance of **{first_name}**, **{full_name}**, **{record}** and **{email}** will be replaced with the receiver's first name, full name, record and email

- If you include any other curly brackets within your HTML content, for example in CSS styling, you'll need to double-wrap them.

- Notice the style component in the following example:

  - ```python
    content = """
      <!DOCTYPE html>
      <head>
      <title>Happy Email</title>
      <style>
      body {{
        background-color: red;
      }}
      </style>
      </head>
      <body>
      Hello {first_name}, I hope you're happy!
      </body>
      </html>
    """
    ```



### 2. Add Your Template as an Option

Next, you'll need to revisit **phish.py** and add in your new template in the ***options*** variable on line 11.

For example:

```python
options = {"1": "LinkedIn", "2": "Happy"}
```

Ensure the option name is **exactly the same** as your class name.



### 3. Include Images in Your Template (Optional)

If you'd like to include images within your template, you'll need to set them up within your newly-created class.

To ensure images aren't included as attachments within your email, **Phish and Chips** recommends the use of **MIMEImage**.

#### Example

Let's say that we'd like to include a smiley face picture, **smiley.jpg** within our ***Happy*** email template.

##### 1. Include Image in HTML Content

Firstly, we need to decide on a name for the image -- in this example, the name assigned is **smiley**. Next, configure your HTML like this:

```python
content = """
  <!DOCTYPE html>
  <head>
  <title>Happy Email</title>
  <style>
  body {{
    background-color: red;
  }}
  </style>
  </head>
  <body>
  Hello {first_name}, I hope you're happy!
  <img src="cid:smiley"></img>
  </body>
  </html>
"""
```

Notice the **src** of the image has been set to ***cid:smiley***.

##### 2. Edit the Classes Build Function

Now you'll need to override the **EmailTemplate** **build** function. Below is an example of how to do this:

**Happy.py**

```python
import EmailTemplate
from email.mime.image import MIMEImage

class Happy(EmailTemplate.EmailTemplate):
	def __init__(self, email, full_name, first_name, record, sender_name, recipient):
		super().__init__(email, full_name, first_name, record, sender_name, recipient, content, "Happy Subject")
    
    def build(self):
        msg = super().build()
        
        fp = open('happy/smiley.jpg', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        
        msgImage.add_header('Content-ID', '<smiley>')
        msg.attach(msgImage)
        
        return msg

content = """
  <!DOCTYPE html>
  <head>
  <title>Happy Email</title>
  <style>
  body {{
    background-color: red;
  }}
  </style>
  </head>
  <body>
  Hello {first_name}, I hope you're happy!
  <img src="cid:smiley"></img>
  </body>
  </html>
"""
```



