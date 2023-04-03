from flask import Flask
import pickle
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
import time
import os

network_traffics="./TrainedModel/"
permission="./gnb_model_permissions.pkl"
schedular= BlockingScheduler


def home():
    print("Welcome")
    
@schedular.scheduled_job(IntervalTrigger(hours=3))
def permission():
    return permissions 


@schedular.scheduled_job(IntervalTrigger(hours=3))
def traffics():
    return network_traffics 
schedular.start()

