### Email Automation using CSV Data

This script automates the process of sending emails to multiple recipients using data from a CSV file. It utilizes the smtplib library for sending emails and the Template module for string substitution.

### Prerequisites

- Python 3.x
- smtplib
- email
- string

### Usage

1. Create a CSV file with the recipient's email addresses and their corresponding details.

2. Create a template.txt file with the email content. Use placeholders like ${NAME} and ${EMAIL} to represent the recipient's details.
  
3. Edit the ADDRESS and PASSWORD variables with your email-address and password in a string.

4. Run the script by executing the following command in your terminal:
   ```
   python3
   python3 email_automation.py
   ```
5. The script will then send personalized emails to each recipient listed in the CSV file.

### Example

Here's an example of how you can use this script:

1. Create a CSV file named 'recipients.csv' with the following content:

NAME,EMAIL
John Doe,john.doe@example.com
Jane Smith,jane.smith@example.com

2. Create a template.txt file with the following content:

Subject: Personalized Email

Dear ${NAME},

This is a personalized email for you, ${EMAIL}.

Best Regards,
Your Name

3. Run the script by executing the following command in your terminal:

   ```
   python3
   python3 email_automation.py
   ```
​
​
3. The script will send personalized emails to John Doe and Jane Smith with their respective names and email addresses.
​
### License
​
This project is licensed under the MIT License - see the LICENSE.md file for details.
​


Please note that this script is for educational purposes only. Sending unsolicited emails to recipients without their consent is illegal and unethical. Always ensure that you have the recipient's permission before sending any email.

Feel free to modify this script according to your specific requirements. If you have any questions or need assistance, please don't hesitate to ask.
