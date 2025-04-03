def send_notification(email, subject, message):
    # Function to send an email notification to HR
    import smtplib
    from email.mime.text import MIMEText

    # Email configuration
    sender_email = "your_email@example.com"
    sender_password = "your_password"
    hr_email = email

    # Create the email content
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = hr_email

    # Send the email
    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, hr_email, msg.as_string())
    except Exception as e:
        print(f"Error sending notification: {e}")

def notify_hr_of_new_grievance(grievance_details):
    # Function to notify HR of a new grievance submission
    subject = "New Grievance Submitted"
    message = f"A new grievance has been submitted:\n\n{grievance_details}"
    hr_email = "hr@example.com"  # Replace with actual HR email
    send_notification(hr_email, subject, message)