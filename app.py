from flask import Flask
import pickle
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
import time
import os

network_traffics="./DATASET/network_traffics.csv"
permission="./TrainedModel/gnb_model_permissions.pkl"
train_randomforest= "./train_randomforest.py"
train_keras="./train_keras.py"
train_svm="./train_svm"

schedular= BlockingScheduler


def home():
    print("---Android Backdoor Detection---")
    
@schedular.scheduled_job(IntervalTrigger(hours=3))
def permission():
    return permissions 
schedular.start()

@schedular.scheduled_job(IntervalTrigger(hours=3))
def traffics():
    return network_traffics 
schedular.start()

