# CP-mailer

CP-mailer is a Python-based automation tool designed to send welcome emails containing OnlineJudge account credentials to students. It reads student data from a CSV file, generates a random password for each student, checks for duplicate accounts, and sends a personalized email via SMTP. The email content is available in both Chinese and English, making it suitable for bilingual environments.

---

## Features

- **Automated Email Sending:** Sends emails using SMTP with secure authentication.
- **Customizable Email Templates:** Easily modify the subject and body of the emails.
- **Random Password Generation:** Generates a random 16-character password for each new account.
- **CSV-based Data Input:** Reads student information from a CSV file.
- **Duplicate Account Check:** Verifies if an account already exists using an existence file.

---

## Prerequisites

- Python 3.6 or higher
- Dependencies listed in [requirements.txt](./requirements.txt):
  - [python-dotenv](https://pypi.org/project/python-dotenv/)
  - [pandas](https://pypi.org/project/pandas/)

---

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/dark9ive/CP-mailer.git
   cd CP-mailer
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**

   - Copy the provided `.env.template` to a new file named `.env`.
   - Edit the `.env` file and update the following variables as needed:
     - **EMAIL_ADDR** – Your email address used for sending emails.
     - **EMAIL_KEY** – Your email password or SMTP key.
     - **SENDER_NAME** – The name you want displayed as the sender.
     - **SMTP_SERVER** – The address of your SMTP server.
     - **SMTP_PORT** – The port for your SMTP server.
     - **CSV_FN** – Path to your input CSV file containing student data.
     - **CSV_NAME_FIELD** – The CSV column name for student names.
     - **CSV_ID_FIELD** – The CSV column name for student IDs.
     - **EXIST_FN** – Path to a file listing existing account IDs (one per line).
     - **CLASS_NAME** – The name of your class (used in the email subject and body).
     - **WEBSITE** – URL of the OnlineJudge system.
     - **OUTPUT_CSV_FN** – Path where the output CSV with email details will be saved.

4. **Prepare Your CSV File:**

   - Ensure the CSV file specified in `CSV_FN` contains the columns as defined by `CSV_NAME_FIELD` and `CSV_ID_FIELD`.

---

## Usage

For testing your SMTP configuration, you can run:

```bash
python mail.py
```

This sends a test email to your configured email address.

To send emails with account credentials, run the main script:

```bash
python main.py
```

The script will:
- Read student data from the CSV file.
- Parse student names and IDs.
- Generate a random password for each student.
- Check if the account already exists using the file specified by `EXIST_FN`.
- Send a personalized email with account details.
- Save a log of sent emails to the output CSV file specified by `OUTPUT_CSV_FN`, which can later be imported into [QDUOJ System](https://github.com/QingdaoU/OnlineJudge).

---

## File Structure

- **constant.py:**  
  Loads environment variables and defines configuration constants and email templates.

- **mail.py:**  
  Handles SMTP initialization and email sending functionality.

- **main.py:**  
  Main script that processes the CSV file, generates passwords, checks for duplicates, sends emails, and saves the results.

- **parse.py:**  
  Contains functions to parse student names and IDs from the CSV and check for existing accounts.

- **passwd.py:**  
  Provides a function for generating random passwords.

- **requirements.txt:**  
  Lists the project dependencies.

---

## Customization

- **Email Templates:**  
  Modify `SUBJECT_TEMPLATE` and `BODY_TEMPLATE` in `constant.py` to customize the content and language of your emails.

- **Password Generation:**  
  Adjust the logic in `passwd.py` if you need different criteria for password complexity or length.

- **ID and Name Parse:**  
  Adjust the logic in `parse.py` if you need different parser for name or id field.

---

## License

This project is licensed under the MIT License.

---

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to open an issue or submit a pull request for any improvements or bug fixes.
