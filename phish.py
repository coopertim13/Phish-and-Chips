import argparse
import sys
import smtplib
from pydoc import locate

username = '' # provide as command line argument, or just chuck it in this variable
password = '' # provide as command line argument, or just chuck it in this variable
server_address = ''  # provide as command line argument, or just chuck it in this variable
server_port = ''  # provide as command line argument, or just chuck it in this variable

options = {"1": "LinkedIn"} # add to this as required

header = """                                                                                                         
,------. ,--.     ,--.       ,--.                            ,--.     ,-----.,--.     ,--.               
|  .--. '|  ,---. `--' ,---. |  ,---.      ,--,--.,--,--,  ,-|  |    '  .--./|  ,---. `--' ,---.  ,---.  
|  '--' ||  .-.  |,--.(  .-' |  .-.  |    ' ,-.  ||      \' .-. |    |  |    |  .-.  |,--.| .-. |(  .-'  
|  | --' |  | |  ||  |.-'  `)|  | |  |    \ '-'  ||  ||  |\ `-' |    '  '--'\|  | |  ||  || '-' '.-'  `) 
`--'     `--' `--'`--'`----' `--' `--'     `--`--'`--''--' `---'      `-----'`--' `--'`--'|  |-' `----'  
                                                                                          `--'           
                                                                                          """

print(header)

parser = argparse.ArgumentParser(description='A phishing email framework.')
parser.add_argument("-e", metavar='email template', help="email template to send", required=True)
parser.add_argument("-s", metavar='sender name', help="name of sender for phishing email", required=True)
parser.add_argument("-u", metavar='username', help="SMTP username")
parser.add_argument("-p", metavar='password', help="SMTP password")
parser.add_argument("-a", metavar='server address', help="SMTP server address")
parser.add_argument("-c", metavar='server port', help="SMTP server port")
parser.add_argument("-v", action='store_true', help="enable verbose output")
args = parser.parse_args()

# Check existence of username / password
if not args.u and username == '':
    if not args.p and password == '':
        parser.print_help()
        print()
        print('Error: Username & password have not been supplied.')
        sys.exit()
    else:
        parser.print_help()
        print()
        print('Error: Username has not been supplied.')
        sys.exit()
if not args.p and password == '':
    parser.print_help()
    print()
    print('Error: Password has not been supplied.')
    sys.exit()

# Replacement of username/password when there are multiple entries (command line arguments prioritised)
if username != '' and args.u:
    print('Multiple usernames entered - using ' + args.u)
if password != '' and args.p:
    print('Multiple passwords entered - using ' + args.p)

# Check existence of server address / port
if not args.a and server_address == '':
    if not args.c and server_port == '':
        parser.print_help()
        print()
        print('Error: SMTP server address & port have not been supplied.')
        sys.exit()
    else:
        parser.print_help()
        print()
        print('Error: SMTP server address has not been supplied.')
        sys.exit()
if not args.c and server_port == '':
    parser.print_help()
    print()
    print('Error: SMTP server port has not been supplied.')
    sys.exit()

# Replacement of SMTP server address/port when there are multiple entries (command line arguments prioritised)
if server_address != '' and args.a:
    print('Multiple SMTP server addresses entered - using ' + args.a)
if server_port != '' and args.c:
    print('Multiple SMTP server ports entered - using ' + args.c)

# Main setup
with open("email-list") as f:
    content = f.readlines()

print()
print("Sending emails...")
print()

count = 0

for person in content:
    new = person.split(":")

    email = new[0].strip()
    full_name = new[1].strip()
    first_name = new[2].strip()
    record = new[3].strip()
    recipient = full_name + ' <' + email + '>'

    if(email[0] != '#'):
        mailObject = locate(options.get(args.e)+'.'+options.get(args.e))(email, full_name, first_name, record, args.s, recipient)
        msg = mailObject.build()
        mailServer = smtplib.SMTP(args.a if args.a is not None else server_address, int(args.c) if args.c is not None else int(server_port))
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(args.u if args.u is not None else username, args.p if args.p is not None else password)
        mailServer.sendmail(args.s, recipient, msg.as_string())
        mailServer.close()
        
        if args.v:
            print("Email sent to " + full_name + " (" + email + ")")
        
        count = count + 1

print()
print("Sent " + str(count) + " email(s)")