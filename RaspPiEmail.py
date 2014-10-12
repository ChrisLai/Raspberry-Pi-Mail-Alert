import smtplib
#-*-coding:utf8-*-
import RPi.GPIO as GPIO, time
import urllib2
import time, datetime

def RCtime(PiPin):
        measurement = 0
        GPIO.setup(PiPin, GPIO.OUT)
        GPIO.output(PiPin, GPIO.LOW)
        time.sleep(0.1)

        GPIO.setup(PiPin, GPIO.IN)

        while (GPIO.input(PiPin) == GPIO.LOW):
                measurement += 1

        return measurement


def main():

    GPIO.setmode(GPIO.BCM)
    ON = 1        #Constant to indicate that lights are on
    OFF = 2       #Constant to indicate that lights are off

    lights=OFF # Current status
    flag = 0
# The loop routine runs over and  over again forever
    while True:
            timestamp = int (time.mktime(datetime.datetime.utcnow().timetuple()))
            print RCtime(2)
            
            if RCtime(2) > 35: #This is the value limit between day or night with or LDR sensor and our capacitor. Maybe you need adjust this value
                    new_lights = OFF
                    flag = 0
                    print ("Mail OFF")
            else:
                    new_lights = ON
                    print ("Mail ON")

            if new_lights == ON and flag == 0:  # Check if we have a change in status
                    flag = 1
                    lights = new_lights  # Status update and send stream
                    smtpUser = 'danhnguyen0902@gmail.com'
                    smtpPass = 'Micadangiu'

                    toAdd = 'danhnguyen0902@gmail.com'
                    fromAdd = smtpUser

 
                    subject = 'Mail Alert'
                    header = 'To: ' + toAdd + '\n' + 'From: " + fromAdd' + '\n' + 'Subject: ' + subject
                    body = 'Your mail has been delivered'

                    print header + '\n' + body

                    s = smtplib.SMTP('smtp.gmail.com', 587)

                    s.ehlo()
                    s.starttls()
                    s.ehlo()

                    s.login(smtpUser, smtpPass)
                    s.sendmail(fromAdd, toAdd, header + '\n\n' + body)

                    s.quit()

                

if __name__ == '__main__':
        main()








