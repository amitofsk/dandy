# Data Acquisition aNd DisplaY

## 1.0 Introduction
### 1.1 What is DANDY?
DANDY is a set of reuseable python examples and a library of python functions to help display sensor data in a graphical user interface (GUI).

### 1.2 What are we building?
Here's a typical hardware setup. A sensor is connected to a microcontroller. The microcontroller sends the sensor data to a computer either over USB or wirelessly. Data is displayed in a GUI on the laptop, perhaps numerically, as a needle rotating in a dial, using a slider, or on a chart plot.
<br><br>
All of these steps can be implemented using existing open software, but some steps are easier than others. For example, Arduino makes writing the microcontroller software easy, and Tkinter and Qt are user-friendly libraries for writing GUIs. Where are the challenges in writing the software? First, the code for the microcontroller and the code for the GUI on the laptop are typically written in different languages. Multiple languages are not a problem for an experienced coder, but they are an obstacle for a novice or a hobbyist. Second, libraries for writing GUI software typically have reusable widgets like buttons and sliders, but they don't have ones made specifically for handling inputs from analog sensors. Third, the software on the laptop has to both continually read from the sensors and continually update the GUI. These should appear to the user to happen simultaneously, without either task blocking the other.
<br><br> 
This project addresses all of these challenges. The goal of this project is not to show a new application of a sensor. Instead, it is to make writing software for this typical setup easier. 


### 1.3 Who is this tutorial for?

This guide is intended for:
 - Students interested in learning about sensor hardware, microcontroller programming,  and writing GUI software.
 - Engineers who want to learn a new way to perform data acquisition using the Python language. 
 - People with at least a little Python coding experience. For example, you should know how to write functions in Python, and you should know what classes and objects are. 
<br><br>
This guide is NOT for you if:
 - You have not programmed before.
 - You want to acquire sensor data with precise timing. In this project, data collection happens with an inexpensive microcontroller without a real time operating system.
 - You want to collect data using elaborate equipment. This project involves small discte sensors.  



## 2.0 Instal software and gather supplies

### 2.1 Check your Python installation

This tutorial requires at least Python version 3.7. If you do not know what verison you have, use the following command on the command line.

 ```python
 py --version
 ```
Python comes with a minimalist Integrated Developement Environment (IDE) named IDLE. This tutorial assumes you will use IDLE to write Python code that will be run on the computer. However, you can use another IDE such as Pycharm or Thonny if you prefer, or you can use your favorite text editor.    
 
### 2.2 Install the pyserial library 

In the command line, execute
```python
pip install pyserial
```


### 2.3 Download the DANDY library.

Change to the directory that you want work in. Then, use the following command in the command line to download the DANDY repository from github. 
 
 ```python
 git clone https://github.com/amitofsk/dandy.git
 ```
 
### 2.4 Download and install the MU IDE
This tutorial will involve both writing Python code for a computer as well as writing Micropython, Circuitpython, or Arduino code for a microcontroller. We'll write Python code for the computer using the IDLE IDE. We'll write Micropython or Circuitpyton code for the microcontroller using the MU IDE. However, you can use other IDE's for the microcontroller programming, such as Thonny, if you prefer. If you are using an Arduino microcontroller, Arduino has its own IDE.
<br><br>
One advantage of using a different IDE for the computer code and the microcontroller code is that the IDE will remind you which hardware you are programming for. 
<br><br>
Download the MU IDE from https://codewith.mu/en/download. Install it. 

### 2.4 Supplies needed
Coming soon ...


## 3.0 Displaying Digital Inputs

### 3.1 What Tkinter is?
Tk is a cross-platform set of tools for writing graphical user interfaces (GUIs). Tkinter is a python's version of the library for making GUIs, and it comes preinstalled with python. 
<br><br>
Tkinter has lots of built in widgets including labels, buttons, scales, and spinboxes. For a nice list along with the API reference, see https://tkdocs.com/pyref/. 

### 3.2 Tkinter widgets 
Let's write our first GUI program using Python and Tkinter. In this example, we use two Tkinter widgets: Label and Button. The pack function puts the widget into the window. 
<br><br>
Try out the example below. You should see a window with a label and a working quit button. If you downloaded the DANDY library, these examples are in the src/examples directory.

```python
import tkinter as tk

#Define the ButtonGUI class
class ButtonGUI:
    # The function __init__ is the constructor for the class.
    def __init__(self):
        self.main_window=tk.Tk()
        self.label1=tk.Label(self.main_window, text="Welcome")
        self.button_quit=tk.Button(self.main_window, text="Quit", \
                            command=self.main_window.destroy)
        #We pack widgets to put them in the window.
        self.label1.pack()
        self.button_quit.pack()
        tk.mainloop()

# Here is our main function which creates an object of class ButtonGUI.
if __name__=="__main__":
    mygui=ButtonGUI()
```
![ButtonGUI output](docPics/buttongui.png)
<br><br><br>
Let's try another example to get more familiar with Tkinter. This example will have a label which shows an image, a quit button, and a second button. If you press that button, the label toggles between two images. Here we write our own function, named toggle_me, that is executed when the button is pressed. 
<br><br> Try out this example too.
```python
import tkinter as tk

class ButtonPicGUI:
    def __init__(self):
        self.main_window=tk.Tk()
        self.smileOn=tk.PhotoImage(file='./smileOn.png')
        self.smileOff=tk.PhotoImage(file='./smileOff.png')
        self.image_number=0

        #This label contains a PhotoImage instead of text.
        self.label1=tk.Label(self.main_window, image=self.smileOn)
        #When button1 is pressed, the instructions in the function
        #toggle_me are followed. We define this function below.
        self.button1=tk.Button(self.main_window, text="Press Me", \
                               command=self.toggle_me)
        self.button_quit=tk.Button(self.main_window, text="Quit", \
                                   command=self.main_window.destroy)

        self.label1.pack()
        self.button1.pack()
        self.button_quit.pack()

        tk.mainloop()

        
    #Here we define the toggle_me function
    def toggle_me(self):
        if self.image_number==0:
            self.label1.configure(image=self.smileOff)
            self.image_number=1
        else:
            self.label1.configure(image=self.smileOn)
            self.image_number=0


if __name__=="__main__":
    mygui=ButtonPicGUI()
```
![Buttonpicgui example output](docPics/buttonpicgui.png)


### 3.3 DANDY widgets for digital inputs
Our examples so far have used widgets that are part of the Tkinter library that comes with Python. The DANDY library, which you just installed, has additional widgets. These widgets are related to data acquisition. The next example uses the DANDY widget LEDDisplay. When you run it, you will see two buttons and an image of an LED. When you press the button, the LED color changes. Try it out.
<br><br>
You may need to change the third line to point to the location of the widgets folder of the DANDY library that you downloaded. This example is also available in the examples folder of the DANDY library. If you open that version, Python should find the widgets folder correctly.


```python
import tkinter as tk
import sys
#We need to import the file for the LEDDisplay widget
sys.path.append('../widgets')
import LEDDisplay as ld

class DigitalNoHW:
    def __init__(self):
        self.main_window=tk.Tk()
        #The class LEDDisplay is defined in the file ../widgets/LEDDisplay.py
        self.led1=ld.LEDDisplay(self.main_window)
        self.button1=tk.Button(self.main_window, text="Press Me", \
                               command=self.toggle_me)
        self.button_quit=tk.Button(self.main_window, text="Quit", \
                                   command=self.main_window.destroy)

        self.led1.pack()
        self.button1.pack()
        self.button_quit.pack()

        tk.mainloop()

        
    #Here we define the toggle_me function
    def toggle_me(self):
        if(self.led1.get_color()=="yellow"):
            self.led1.change_LED_color("blue")
        elif (self.led1.get_color()=="blue"):
            self.led1.change_LED_color("yellow")


if __name__=="__main__":
    mygui=DigitalNoHW()
```

![LEDDisplay widget picture](docPics/ledwidget.png)

### 3.4 Hardware: LED, button, Microcontroller

#### 3.4.1 Solder headers on Micrpcontroller (if needed)
(TODO Andy, put pictures) If there are not headers on the RPi then they can be soldered.


#### 3.4.2 Option A: Micropython and RPiPico
##### 3.4.2.1 Build the circuit
Connect a button and a resistor between GP16 & 5V (pin 39) <br>
Connect a resistor and LED between GP19 & GND

Here is the link of the circuit https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf <br>
![](docPics/PiAndButton3.png)
##### 3.4.2.2 Installation

**Steps**
1. Download the latest release from https://micropython.org/download/rp2-pico/
2. Hold the botton down and plug in the Rpi by using the USB cable
3. In windows explorer should see now the Rpi Drive available 
4. In windows explorer drag the file you just downloaded to that drive
5. Unplug the USB cable, without plugging the button in (BOOTSEL)
6. In this example we are using MU Integrated Development Environment (IDE), download it from this website codewith.mu/en/download . Thonny could also be used instead of MU.
7. Open the MU editor, select Micropython and the Raspberry PiPico (it may ask for this option or select the Mode button)

##### 3.4.2.3 Blinky lights

**Steps**
1. In the python file in the MU editor, print hello

```python
print ("Hello")
```

2. Run the file to make sure it works
3. We are ready to use the push button you wired earlier


```python
from machine import Pin
import time
print ("hello")

button = Pin(16, Pin.IN, Pin.PULL_DOWN)
led=Pin(25, Pin.OUT)
while True:
    if button.value():
        print("T")
        led.value(True)
    else:
        print("F")
        led.value(False)
    time.sleep(1)
```
The fifth line tells the RPPico that we will call pin GP25, the built in LED, the name led. This line also says GP25 will be a digital output.  <br><br>
The fourth line tells the RPPico that we will call pin GP16, which is also called pin 21 in the pinout diagram, button. This line also say as GP16 will be a digital input. 
The Pin.PULL_DOWN option connects the pin to an internal resistor so that when nothing is connected to it, the pin will be low.   
4. Run the code of step 3, when you hold down the button it will print T otherwise it prints F.

![](./docPics/Section3.4.3.2_step4.png)

#### 3.4.2 Option B: Circuitpython and RPiPico
##### 3.4.2.1 Build the circuit
##### 3.4.2.2 Installation

**Steps**
1. Download the latest release from https://circuitpython.org/board/raspberry_pi_pico/
2. Hold the botton down and plug in the Rpi by using the USB cable
3. In windows explorer should see now the Rpi Drive available 
4. In windows explorer drag the file you just downloaded to that drive
5. Unplug the USB cable, without plugging the button in (BOOTSEL)
6. In this example we are using MU Integrated Development Environment (IDE), download it from this website codewith.mu/en/download . Thonny could also be used instead of MU.
7. Open the MU editor, select Circuitpython and the Raspberry PiPico (it may ask for this option or select the Mode button)

##### 3.4.2.3 Blinky lights

**Steps**
1. In the python file in the MU editor, print hello

```python
print ("Hello")
```

2. Run the file to make sure it works
3. We are ready to use the push button you wired earlier


```python
import time
import board
import digitalio

print ("hello")
led=DigitalInOut(board.LED)
led.direction=digitalio.Direction.OUTPUT
button=DigitalInOut(board.GP16)
button.direction=digitalio.Direction.INPUT
while True:
    if button.value():
        print("T")
        led.value(True)
    else:
        print("F")
        led.value(False)
    time.sleep(1)
```
The fifth line tells the RPPico that we will call pin GP25, the built in LED, the name led. This line also says GP25 will be a digital output.  <br><br>
The fourth line tells the RPPico that we will call pin GP16, which is also called pin 21 in the pinout diagram, button. This line also say as GP16 will be a digital input. 
The Pin.PULL_DOWN option connects the pin to an internal resistor so that when nothing is connected to it, the pin will be low.  
Reference: https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/traffic-light-and-pedestrian-crossing  
4. Run the code of step 3, when you hold down the button it will print T otherwise it prints F.

![](./docPics/Section3.4.3.2_step4.png)


#### 3.4.2 Option C: Micropython& CY8CPROTO
#### 3.4.2.1 Build the circuit
##### 3.4.2.2 Installation
##### 3.4.2.3 Blinky lights
#### 3.4.2 Option D: Arduino
#### 3.4.2.1 Build the circuit
##### 3.4.2.2 Installation
##### 3.4.2.3 Blinky lights

Follow the instructions provided by Thonny link thru the Use digital inputs and outputs.

### 3.5 Displaying digital data from the microcontroller on the computer
1. Close the MU editor. 
2. Open IDLE or your favourite text editor.
3. Copy or type the following example. We will run this code on the computer, not the microcontroller.
```python
import serial
import serial.tools.list_ports as port_list

print('Hello')
ports=list(port_list.comports())
port=(ports[0].device)
print(ports[0].device)
#If you are on Windows and get an error saying port not found, try the next line.
#port='COM1'
#If you are on Linux and get an error saying port not found, try the next line.
#port='/dev/ttyACM0'
baudrate=115200
serialPort=serial.Serial(port=port, baudrate=baudrate, bytesize=8, timeout=0.1, stopbits=serial.STOPBITS_TWO)
while True:
    serialString=serialPort.read()
    print(serialString)
serialPort.close()
```
4. Run this code. You should see output that contains the characters T and F.
### 3.6 Sending data, now with widgets and asyncio
#### 3.6.1 What is asyncio and why do we need it here.
Tkinter is the graphics library. Typically, tkinter runs in a loop to continually refresh the graphical user interface. In the previous example, we used a loop to continually read serially.
The problem is we want both loops to run continuously in parallel. One possible solution would be to put each of these tasks in different threads. 
We are not quite doing this, but we are doing something quite similar. 
<br><br>
We will be using the asyncio python library. This library isn't quite multithreadding, but it accomplishes the same task. 
Also, instead of telling tkinter to loop continually, we will tell it to manually update inside a loop. 
The asyncIO library is new to python, so make sure you are at least using version 3.7 of python.
<br><br> 
More info on asyncIO can be found at https://realpython.com/async-io-python.
Information on using asyncIO with tkinter came from https://stackoverflow.com/questions/47895765/use-asyncio-and-tkinter-or-another-gui-lib-together-without-freezing-the-gui 

#### 3.6.2 A first example using tkinter widgets

Make sure the microcontroller is plugged in and still running the previous example.
<br><br>
Run this example. You will see a small icon and a quit button.
When you press the pushbutton on the circuit connected to the microcontroller, the small icon will change.

```python
#Read the instructions in Dandy.md. 
#Before running this program, upload the serialRead.py to your microcontroller.
#When this runs, you will see a small icon and a quit button.
#When you press the pushbutton on the circuit connected to the microcontroller, 
#the small icon will change.

#Information on asyncIO came from:
#https://realpython.com/async-io-python
#Information on getting tkinter and asyncio to work together came from:
#https://stackoverflow.com/questions/47895765/use-asyncio-and-tkinter-or-another-gui-lib-together-without-freezing-the-gui-lib-together-without-freezing-the-gui-lib-together-without-freezing-the


import asyncio
import tkinter as tk
import itertools as it
import time
import serial
import serial.tools.list_ports as port_list

class DigDisplay(tk.Tk):
    #Here's the constructor for the class DigDisplay.
    #This is a child of tk.Tk which opens a window.
    def __init__(self, loop, interval=1/40):
        super().__init__()
        self.loop=loop
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.q=asyncio.Queue()
        self.tasks=[]
        #We'll have three async tasks, named checkdigin, consumeQueue, and updater.
        #Each of these are detailed in their own function.
        self.tasks.append(loop.create_task(self.checkdigin(1/20,self.q)))
        self.tasks.append(loop.create_task(self.consumeQueue(1/20, self.q)))
        self.tasks.append(loop.create_task(self.updater(interval)))
        #Set up the widgets and pack them into the window.
        self.digBit=1
        self.buttonQuit=tk.Button(self, text="Quit", command=self.close)
        self.smileOn=tk.PhotoImage(file='./smileOn.png')
        self.smileOff=tk.PhotoImage(file='./smileOff.png')
        self.label1=tk.Label(self, image=self.smileOn)
        self.label1.pack()
        self.buttonQuit.pack()


    async def checkdigin(self, interval, qIn:asyncio.Queue):
        #This asyncio function reads from the serial port and writes to the queue if it finds T or F.
        ports=list(port_list.comports())
        print(ports[0].device)
        port=ports[0].device
        #If you are on windows and you get an error saying it can't find the port, try the line below.
        #port='COM6'
        #If you are on linux and you get an error saying it can't find the port, try the line below.
        #port='/dev/ttyACM0'
        baudrate=115200
        serialPort=serial.Serial(port=port, baudrate=baudrate, bytesize=8, timeout=0.1, stopbits=serial.STOPBITS_TWO)
        imax=10000
        for ii in range(imax):
            await asyncio.sleep(interval)
            serialByte=serialPort.read()
            serialInt=int.from_bytes(serialByte, "big")
            if serialInt != 0:
                await qIn.put(serialByte)
                print(serialByte)
        serialPort.close()
        

    async def consumeQueue(self, interval, qIn: asyncio.Queue):
        #This asyncio function reads from the queue and sets the appropriate picture if necessary
        while True:
            await asyncio.sleep(interval)
            i=await qIn.get()
            #The character T has ascii value 84. The character F has 
            #ascii value 70. We're actually reading in individual bytes.
            #The next line converts bytes to integers.
            intval=int.from_bytes(i, "big")
            print(intval)
            if intval==84:
                print("Found T")
                self.label1.configure(image=self.smileOn)
            if intval==70:
                print("Found F")
                self.label1.configure(image=self.smileOff)
                


    async def updater(self, interval):
        #This async function manually updates the tkinter GUI.
        while True:
            self.update()
            await asyncio.sleep(interval)

    def close(self):
        for task in self.tasks:
            task.cancel()
        self.loop.stop()
        self.destroy()
        
        
if __name__=="__main__":
    loop=asyncio.get_event_loop()
    app=DigDisplay(loop)
    loop.run_forever()
    loop.close()
```

#### 3.6.3 A second example using tkinter and DANDY widgets


## 4.0 Displaying analog inputs

### 4.1 DANDY widgets for analog inputs

### 4.2 Hardware: Potentiometers, sensors, and a Microcontroller

#### 4.2.1 Option A: Micropython and RPiPico
##### 4.2.1.1 Build the circuit
##### 4.2.2.2 Write the microcontroller code

#### 4.2.1 Option B: Circuitpython and the RPiPico
#### 4.2.1 Option C: Micropython and the CY8CPROTO
#### 4.2.1 Option D: Arduino

#### 4.3 Displaying analog data from the microcontroller on the computer
#### 4.4 Displaying analog data, now with widgets and asyncio
#### 4.5 Displaying vector data
## 5.0 Additional DANDY widgets

### 5.1 Examples with the microcontroller-like widgets...
