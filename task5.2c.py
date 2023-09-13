import RPi.GPIO as GPIO  
import tkinter as tk

LED1_PIN = 15
LED2_PIN = 16
LED3_PIN = 18


GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1_PIN, GPIO.OUT)
GPIO.setup(LED2_PIN, GPIO.OUT)
GPIO.setup(LED3_PIN, GPIO.OUT)


def Complete_proccess():
    GPIO.output(LED1_PIN, GPIO.LOW)
    GPIO.output(LED2_PIN, GPIO.LOW)
    GPIO.output(LED3_PIN, GPIO.LOW)


radio_button1 = tk.Radiobutton(root, text="Red Light", value=1, command=lambda: button_click(1))
radio_button2 = tk.Radiobutton(root, text="Blue Light", value=2, command=lambda: button_click(2))
radio_button3 = tk.Radiobutton(root, text="Green light", value=3, command=lambda: button_click(3))

def button_click(led_num):
    Complete_proccess()
    if led_num == 1:
        GPIO.output(LED1_PIN, GPIO.HIGH)
    elif led_num == 2:
        GPIO.output(LED2_PIN, GPIO.HIGH)
    elif led_num == 3:
        GPIO.output(LED3_PIN, GPIO.HIGH)

exit_button = tk.Button(root, text="Complete the proccess", command=root.quit)

radio_button1.pack()
radio_button2.pack()
radio_button3.pack()
exit_button.pack()

root = tk.Tk()
root.title("Traffic system")

root.mainloop()


GPIO.cleanup()
