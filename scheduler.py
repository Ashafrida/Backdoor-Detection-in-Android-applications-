import schedule
import time

def add_new_Applications():
    # Retrieve the data from the frontend system
    # Check if the data already exists in the database to avoid duplicates
    # If the data does not exist, insert it into the database
    pass

schedule.every().hour.do(add_new_Applications)

while True:
    schedule.run_pending()
    time.sleep(1)
