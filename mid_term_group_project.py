import logging
import requests as r
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

Sheety_URL = "https://api.sheety.co/link/task/manager"

class Task_Manager:
    def read_task_data(self):
        response = r.get(Sheety_URL)
        result = response.json()
        data = result.get('manager', [])
        
        for index, contact in enumerate(data, start=1):
            print(f"{index}.")
            for key, value in contact.items():
                print(f"    {key}: {value}")
            print()
    
    def add_task_data(self, name, email, task, priority, status):
        URL = Sheety_URL
        response = r.post(URL, json={
            "manager": {
                "name": name,
                "email": email,
                "task": task,
                "priority": priority,
                "status": status,
            }}, headers={'Content-Type': 'application/json'})
        print(response.status_code)
        print("The Task is Added.")
    
    def update_task_data(self, id, name, email, task, priority, status):
        URL = Sheety_URL + f"/{id}"
        response = r.get(URL)
        current_data = response.json().get("manager", {})
        change_data = {
            "manager": {
                "name": name if name else current_data.get("name"),
                "email": email if email else current_data.get("email"),
                "task": task if task else current_data.get("task"),
                "priority": priority if priority else current_data.get("priority"),
                "status": status if status else current_data.get("status")
            }
        }
        headers = {'Content-Type': 'application/json'}
        response = r.put(URL, json=change_data, headers=headers)
        print(response.json())
    
    def delete_task_data(self):
        id = int(input("Enter the id num to delete person: "))
        URL = Sheety_URL + f"/{id}"
        response = r.delete(URL)
        if response.status_code == 204:
            print(f"Person with id {id} successfully deleted.")
        else:
            try:
                print(response.json())
            except ValueError:
                print(f"Failed to delete Person task with id {id}. Status code: {response.status_code}")

    def filter_tasks(self):
        response = r.get(Sheety_URL)
        result = response.json()
        data = result.get('manager', [])
        
        logging.debug(f"Filtering tasks from data: {data}")
        
        pending_tasks = [task for task in data if task['status'].strip() == 'pending' and task['priority'].strip() in ('medium', 'high')]
        
        logging.debug(f"Filtered pending tasks: {pending_tasks}")
        
        return pending_tasks

    def send_pending_task_emails(self):
        tasks = self.filter_tasks()
        if not tasks:
            print("No pending tasks with high or medium priority found.")
            return

        for task in tasks:
            name = task['name']
            email = task['email']
            task_name = task['task']
            priority = task['priority']
            subject = f'Pending Task Notification: {task_name}'
            body = f'Hello {name},\n\nThis is a reminder that you have a pending task: {task_name}.\nPriority: {priority}\n\nPlease address it as soon as possible.\n\nBest regards,\nTask Manager'
            
            try:
                self.send_email(subject, body, email, priority)
            except Exception as e:
                logging.error(f"Failed to send email to {email}: {e}")

    def send_email(self, subject, body, to_email, priority):
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_user = 'abdulhadistmstudent@gmail.com'
        smtp_password = 'password' # Saved in .env file
        
        msg = MIMEMultipart()
        msg['From'] = smtp_user
        msg['To'] = to_email
        msg['Subject'] = subject
        
        if priority.lower() == 'high':
            msg['X-Priority'] = '1'
        elif priority.lower() == 'medium':
            msg['X-Priority'] = '3'
        
        msg.attach(MIMEText(body, 'plain'))
        
        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_user, smtp_password)
                server.sendmail(smtp_user, to_email, msg.as_string())
            logging.info(f"Email sent to {to_email} with {priority} priority.")
        except Exception as e:
            logging.error(f"Failed to send email: {e}")

    def main(self):
        print("Task Management System: \n", "--" * 100)
        while True:
            try:
                choice = int(input("=> Enter What to do: \n1. Read All Task with Detail \n2. Add New Task with Detail \n3. Update Task Detail \n4. Remove Task \n5. Send Pending Task Emails \n-> Enter the Option: "))
                match choice:
                    case 1:
                        self.read_task_data()
                    case 2:
                        try:
                            name = input("Enter the New User: ").title()
                            task = input("Enter the Task name: ").lower()
                            email = input(f"Enter the email of {name}: ")
                            priority = input("Enter the Priority (low, medium, high): ").lower()
                            status = input("Enter the Task Status (pending / completed): ").lower()
                            self.add_task_data(name, email, task, priority, status)
                        except Exception as e:
                            print(e)
                    case 3:
                        try:
                            id = int(input("Enter the id to update task detail: "))
                        except Exception as e:
                            print(e)
                        name = input("Enter the updated Name (If unchanged then "" string): ")
                        task = input("Enter the updated task (If Unchanged then give ""): ")
                        email = input("Enter the Updated Email (If Unchanged then give "" string): ")
                        priority = input("Enter the updated Priority (If Unchanged then give ""): ")
                        status = input("Enter the updated Status (If Unchanged then give ""): ")
                        self.update_task_data(id, name, email, task, priority, status)
                    case 4:
                        self.delete_task_data()
                    case 5:
                        self.send_pending_task_emails()
                    case _:
                        break
            except Exception as e:
                print(e)

task = Task_Manager()
task.main()