import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def create_email_heading(heading):
    """
    Create the heading/title section for an HTML email.
    
    :param heading: The email's heading/title
    :return: HTML for the heading section
    """
    heading_html = f"""
    <h1 style="color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px;">
        {heading}
    </h1>
    """
    return heading_html

def create_email_body(body_content):
    """
    Create the body section for an HTML email with proper paragraph formatting.
    
    :param body_content: The main content of the email
    :return: HTML for the body section with formatted paragraphs
    """
    # Split the content by newlines or double newlines
    paragraphs = body_content.split('\n\n')
    if len(paragraphs) == 1:  # If no double newlines, try single newlines
        paragraphs = body_content.split('\n')
    
    # Wrap each paragraph in <p> tags with margin
    formatted_paragraphs = ""
    for paragraph in paragraphs:
        paragraph = paragraph.strip()
        if paragraph:  # Only add non-empty paragraphs
            formatted_paragraphs += f'<p style="margin-bottom: 1em;">{paragraph}</p>\n'
    
    body_html = f"""
    <div style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
        {formatted_paragraphs}
    </div>
    """
    return body_html

def create_simple_email_template(heading, body):
    """
    Create a simple, flexible HTML email template.
    
    :param heading: The email's heading/title
    :param body: The main content of the email
    :return: Formatted HTML email content
    """
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{heading}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                color: #333;
            }}
            h1 {{
                color: #2c3e50;
                border-bottom: 2px solid #3498db;
                padding-bottom: 10px;
            }}
        </style>
    </head>
    <body>
        <h1>{heading}</h1>
        <div>
            {body}
        </div>
    </body>
    </html>
    """
    return html_template

def create_solidliquidity_email_template(body):
    """
    Create a SolidLiquidity TLDR email template with light blue borders.
    
    :param body: The main content of the email
    :return: Formatted HTML email content
    """
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SolidLiquidity; TLDR</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                max-width: 600px;
                margin: 20px auto;
                padding: 0;
                color: #333;
                border: 10px solid #B0E0E6;  /* Light blue border */
                box-sizing: border-box;
            }}
            .container {{
                padding: 20px;
            }}
            .header {{
                background-color: #B0E0E6;  /* Light blue */
                color: #333;
                text-align: center;
                padding: 15px;
                font-size: 24px;
                font-weight: bold;
            }}
            .content {{
                padding: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="header">
            SolidLiquidity; TLDR
        </div>
        <div class="container">
            <div class="content">
                {body}
            </div>
        </div>
    </body>
    </html>
    """
    return html_template

def send_html_email(sender_email, sender_password, recipient_email, subject, html_content):
    """
    Send an HTML email using SMTP.
    
    :param sender_email: Email address of the sender
    :param sender_password: Password for the sender's email account
    :param recipient_email: Email address of the recipient
    :param subject: Subject line of the email
    :param html_content: HTML content of the email body
    """
    # Create the email message
    message = MIMEMultipart('alternative')
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject

    # Create HTML part
    html_part = MIMEText(html_content, 'html')
    
    # Attach HTML part to the message
    message.attach(html_part)

    try:
        # Connect to the SMTP server (example uses Gmail's SMTP server)
        # Note: You might need to use app passwords or adjust settings based on your email provider
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            # Start TLS for security
            server.starttls()
            
            # Login to the email account
            server.login(sender_email, sender_password)
            
            # Send email
            server.sendmail(sender_email, recipient_email, message.as_string())
        
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")