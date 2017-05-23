from django.shortcuts import render
import RPi.GPIO as GPIO
import time

# Create your views here.
def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'dashboard/pages/index.html')

def conforto(request):
    return render(request, 'dashboard/pages/conforto.html')

def liga1(request):
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	
	pinList = [5]
	
	for i in pinList: 
    	GPIO.setup(i, GPIO.OUT)

    try:
  		GPIO.output(5, GPIO.LOW)
  	except KeyboardInterrupt:
  		GPIO.cleanup()


def liga2(request):
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	
	pinList = [6]
	
	for i in pinList: 
    	GPIO.setup(i, GPIO.OUT)

    try:
  		GPIO.output(6, GPIO.LOW)
  	except KeyboardInterrupt:
  		GPIO.cleanup()


def liga3(request):
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	
	pinList = [12]
	
	for i in pinList: 
    	GPIO.setup(i, GPIO.OUT)

    try:
  		GPIO.output(12, GPIO.LOW)
  	except KeyboardInterrupt:
  		GPIO.cleanup()

def liga4(request):
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	
	pinList = [13]
	
	for i in pinList: 
    	GPIO.setup(i, GPIO.OUT)

    try:
  		GPIO.output(13, GPIO.LOW)
  	except KeyboardInterrupt:
  		GPIO.cleanup()

def liga5(request):
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	
	pinList = [19]
	
	for i in pinList: 
    	GPIO.setup(i, GPIO.OUT)

    try:
  		GPIO.output(19, GPIO.LOW)
  	except KeyboardInterrupt:
  		GPIO.cleanup()

def liga6(request):
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	
	pinList = [16]
	
	for i in pinList: 
    	GPIO.setup(i, GPIO.OUT)

    try:
  		GPIO.output(16, GPIO.LOW)
  	except KeyboardInterrupt:
  		GPIO.cleanup()

def liga7(request):
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	
	pinList = [26]
	
	for i in pinList: 
    	GPIO.setup(i, GPIO.OUT)

    try:
  		GPIO.output(26, GPIO.LOW)
  	except KeyboardInterrupt:
  		GPIO.cleanup()

def liga8(request):
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	
	pinList = [20]
	
	for i in pinList: 
    	GPIO.setup(i, GPIO.OUT)

    try:
  		GPIO.output(20, GPIO.LOW)
  	except KeyboardInterrupt:
  		GPIO.cleanup()

def desliga1(request):
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	
	pinList = [5]
	
	for i in pinList: 
    	GPIO.setup(i, GPIO.OUT)

    try:
  		GPIO.output(5, GPIO.HIGH)
  	except KeyboardInterrupt:
  		GPIO.cleanup()


def desliga2(request):
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	
	pinList = [6]
	
	for i in pinList: 
    	GPIO.setup(i, GPIO.OUT)

    try:
  		GPIO.output(6, GPIO.HIGH)
  	except KeyboardInterrupt:
  		GPIO.cleanup()


def desliga3(request):
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	
	pinList = [12]
	
	for i in pinList: 
    	GPIO.setup(i, GPIO.OUT)

    try:
  		GPIO.output(12, GPIO.HIGH)
  	except KeyboardInterrupt:
  		GPIO.cleanup()

def desliga4(request):
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	
	pinList = [13]
	
	for i in pinList: 
    	GPIO.setup(i, GPIO.OUT)

    try:
  		GPIO.output(13, GPIO.HIGH)
  	except KeyboardInterrupt:
  		GPIO.cleanup()

def desliga5(request):
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	
	pinList = [19]
	
	for i in pinList: 
    	GPIO.setup(i, GPIO.OUT)

    try:
  		GPIO.output(19, GPIO.HIGH)
  	except KeyboardInterrupt:
  		GPIO.cleanup()

def desliga6(request):
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	
	pinList = [16]
	
	for i in pinList: 
    	GPIO.setup(i, GPIO.OUT)

    try:
  		GPIO.output(16, GPIO.HIGH)
  	except KeyboardInterrupt:
  		GPIO.cleanup()

def desliga7(request):
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	
	pinList = [26]
	
	for i in pinList: 
    	GPIO.setup(i, GPIO.OUT)

    try:
  		GPIO.output(26, GPIO.HIGH)
  	except KeyboardInterrupt:
  		GPIO.cleanup()

def desliga8(request):
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	
	pinList = [20]
	
	for i in pinList: 
    	GPIO.setup(i, GPIO.OUT)

    try:
  		GPIO.output(20, GPIO.HIGH)
  	except KeyboardInterrupt:
  		GPIO.cleanup()

