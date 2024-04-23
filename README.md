# Birthday Wishing Through Email

## Introduction
This Django Rest Framework (DRF) project automates birthday wishes by sending emails to customers on their birthdays. The system features a RESTful API endpoint (`/customer/register`) for adding customers with their birthdays and automatically dispatches birthday emails containing a personalized message.

## Features
- RESTful API endpoint (`/customer/register`) for adding customers with their birthdays.
- Automatic sending of birthday emails to customers on their birthdays.
- Simulated email-sending process for testing purposes, in absence of actual email credentials.
- Task scheduling/background task integration for sending birthday emails (using CELERY+REDIS).
- API Documentation available at `/api-docs/`.

## Installation
1. Clone the repository to your local machine:
```bash
git clone https://github.com/NoManNayeem/BirthdayWisher.git
```


2. Navigate to the project directory and create a `.env` file as demonstrated in `Env-Example.txt`, then:
```bash
cd BirthdayWisher
```


3. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
```

4. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

5. Install the required dependencies:
```bash
pip install -r requirements.txt
```


6. Run database migrations:
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```


7. Start the development server:
```bash
python manage.py runserver
```

- (Optional): You may need to create a superuser using: `python manage.py createsuperuser`

8. Start Celery Worker:
```bash
celery -A BirthdayWisher worker
```
9. Start Celery Beat Scheduler:
```bash
celery -A BirthdayWisher beat
```


*** Note: Update setuptools if needed: ***

```bash
pip install --upgrade setuptools
```


## Usage
1. Use the API endpoint (`/customer/register`) to add customers with their birthdays.
2. The system will automatically send birthday emails to customers on their birthdays.

## Simulation of Email Sending
Emails are simulated in the absence of actual email credentials for testing purposes. No actual emails are sent, but the system triggers a simulated process.



## Task Scheduling/Background Tasks
Task scheduling and background task functionality are integrated into the project to automate the process of sending birthday emails.


## Testing
To run the tests, execute the following command:

- You can test the test case for the register API using 
```bash
python manage.py test customers
```
- You can trigger the Scheduled Task using 

```bash
python manage.py test_birthday_wishes
```

## License and Copyright Information

License and Copyright Information can/will be added here.