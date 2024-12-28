import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "rishabh@fixmechanic.com"
receiver_email = "mrgoldentrader.mumbai@gmail.com"
password = "A123456798@a"

# SMTP server details
smtp_server = "smtp.hostinger.com"
smtp_port = 587  # Use 465 for SSL, 587 for STARTTLS

# Create the email
subject = "Account Verification Required"
body = """\
<html>
  <body>
    <p>Dear [User],</p>
    <p>We have detected suspicious activity on your [XYZ Service] account. As a result, your account access will be locked within 24 hours unless you verify your identity.</p>
    <p>To continue using your account, please click on the link below and verify your account details:</p>
    <p><a href='http://localhost/phishing_attack/index.html'>Click here to verify your account</a></p>
    <p>Failure to act will result in permanent suspension of your account.</p>
    <p>If you believe this is a mistake, please contact our support team immediately.</p>
    <p>Thank you, <br>[Service Provider] Security Team</p>
  </body>
</html>
"""

# Create MIME object
message = MIMEMultipart()
# Spoof the sender name
message["From"] = "Support Team <rishabh@fixmechanic.com>"
message["To"] = receiver_email
message["Subject"] = subject

# Attach email body (use 'html' for HTML content)
message.attach(MIMEText(body, "html"))

try:
    # Connect to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Start TLS encryption
    server.login(sender_email, password)

    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()

