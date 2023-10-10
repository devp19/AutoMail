'''
Email Automation using CSV Data
GitHub: devp19
'''

# -------------------------------------
# Libraries / Modules
# -------------------------------------
import smtplib
import csv
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# -------------------------------------------
# Function to read the template.txt file
#   and to pass it through TEMPLATE module
#     for string substitution (editing)
# -------------------------------------------
def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def main():
    message_template = read_template('/Users/devpatel/Desktop/Personal Codes/Email Automation/template.txt')
    
    # -----------------------
    # Email Credentials
    # -----------------------
    MY_ADDRESS = '**********@gmail.com'
    PASSWORD = '******'
    
    # ------------------------------------------------------------
    #  Establishes a connection to a Gmail SMTP server
    #   and logs into an email account using the smtplib library
    # ------------------------------------------------------------
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # -----------------------------------------------------------------
    # Reads csv file and creates it's respective object. 
    #   Uses delimiter to specify values are seperated by commas (csv)
    #     Skips first row since CSV files are usually header-based
    # ------------------------------------------------------------------
    with open("/Users/devpatel/Desktop/Personal Codes/Email Automation/employee-database.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
       
        next(csv_reader)
        
        # -------------------------------------------------------------------------------------------
        # Iterates through each row, where 'lines' represents values of the CSV file.
        #   Creates new MIMEMultipart() object for msg
        #     Substitues placeholders from template (template.txt) with CSV data
        #       Fills email layout (subject, recipent etc.) and sends email using SMTP connection.
        # -------------------------------------------------------------------------------------------
        for lines in csv_reader:
            msg = MIMEMultipart()
            message = message_template.substitute(PERSON_NAME=lines[0], SUPERVISOR=lines[2], SUPEMAIL=lines[3], EMPLOYEE_ID=lines[4], DATE=lines[5])
            print(message)
            msg['From'] = 'Dev Patel'
            msg['To'] = lines[1]
            msg['Subject'] = "Email Automation - Python"
            
            msg.attach(MIMEText(message, 'plain'))
            s.send_message(msg)
            
            #Clears msg object (memory-efficiency)
            del msg

    s.quit()

if __name__ == '__main__':
    main()
