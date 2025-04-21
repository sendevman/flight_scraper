from celery import Celery

celery_app = Celery("tasks", broker="redis://localhost:6379/0")

@celery_app.task
def async_scrape_flight_data(airline, number, date):
    pass