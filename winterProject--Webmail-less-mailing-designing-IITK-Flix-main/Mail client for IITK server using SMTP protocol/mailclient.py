import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Setup port number and server name
smtp_port = 25                # Standard secure SMTP port
smtp_server = "mmtp.iitk.ac.in"  # iitk SMTP Server

# Set up the email lists
email_from = input('Enter your email id:')
email_list = []
n=int(input("Enter the number of recipients:"))
for i in range(0,n):
    emailID=input("Enter email id of recipient")
    email_list.append(emailID)
password = input('Enter your email password:') 
subject = input("Enter subject:")

def send_emails(email_list):
     # Make the body of the email
    body = input("Enter body:")
    for person in email_list:
        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = person
        msg['Subject'] = subject

        # Attach the body of the message
        msg.attach(MIMEText(body, 'plain'))

        # Define the file to attach
        filename =input("enter attachment path:")
        attachment= open(filename, 'rb')  
        attachment_package = MIMEBase('application', 'octet-stream')
        attachment_package.set_payload((attachment).read())
        encoders.encode_base64(attachment_package)
        attachment_package.add_header('Content-Disposition', "attachment; filename= " + filename)
        msg.attach(attachment_package)

        # Cast message as string
        text = msg.as_string()

        # Connect with the server
        print("Connecting to server...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(email_from, password)
        print("Succesfully connected to server")
        print()


        # Send emails to "person" as list is iterated
        print(f"Sending email to: {person}...")
        TIE_server.sendmail(email_from, person, text)
        print(f"Email sent to: {person}")
        print()

    # Close the port
    TIE_server.quit()


# Run the function
send_emails(email_list)
