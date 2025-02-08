import schedule
import time
import threading
from django.core.mail import send_mail
from django.utils.timezone import now
from .models import BookIssue
from django.conf import settings

def send_due_reminders():
    """Check overdue books and send reminder emails."""
    overdue_books = BookIssue.objects.filter(due_date__lt=now(), returned=False)
    
    for book in overdue_books:
        subject = "Library Book Due Reminder"
        message = f"Hello {book.user.username},\n\nYour book '{book.book.title}' was due on {book.due_date}. Please return it soon.\n\nThanks,\nLibrary Management"
        recipient_email = book.user.email
        
        send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient_email])

    print(f"📧 Sent {overdue_books.count()} reminder emails.")

# Schedule the task to run every day at 9 AM
schedule.every().day.at("09:00").do(send_due_reminders)

def run_scheduler():
    """Runs the scheduler in a separate thread to avoid blocking Django."""
    while True:
        schedule.run_pending()
        time.sleep(60)  # Wait 1 minute before checking again

# Start the scheduler in a separate thread
def start_scheduler():
    scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
    scheduler_thread.start()
