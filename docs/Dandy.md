# Data Acquisition aNd DisplaY

## 1.0 Introduction

### 1.1 Audience 
This guide is intended for,
 - New Engineering students with python background
 - Engineers willing to learn new way to perform data acquisition using python language
 - People no prior experiece with python
 - People with python in their computer at version 3.7. 
 


### 1.2 What is Dandy?
I plan to write a set of reusable python examples or a library of python functions to help display sensor data in a graphical user interface (GUI).

What am I building?
Here's a typical hardware setup. A sensor is connected to a microcontroller. The microcontroller sends the sensor data to a laptop either over USB or Bluetooth. Data is displayed in a GUI on the laptop, perhaps numerically, as a needle rotating in a dial, or on a chart plot. 

All of these steps can be implemented using existing open software, but some steps are easier than others. For example, Arduino makes writing the microcontroller software easy, and Tkinter and Qt are user-friendly libraries for writing GUIs. Where are the challenges in writing the software? First, the code for the microcontroller and the code for the GUI on the laptop are typically written in different languages. Multiple languages are not a problem for an experienced coder, but they are an obstacle for a novice or a hobbyist. Second, libraries for writing GUI software typically have reusable widgets like buttons and sliders, but they don't have ones made specifically for handling inputs from analog sensors. Third, the software on the laptop has to both continually read from the sensors and continually update the GUI. These should appear to the user to happen simultaneously, without either task blocking the other. 

The goal of this project is not to show a new application of sensors. Instead, it is to make writing software for this typical setup easier. More specifically, I plan to write a set of reusable examples that show how to solve the problems described above. These examples will use MicroPython for the microcontroller code and Python for laptop code. The GUI will be written using Tkinter and will show example reusable widgets for displaying the analog sensor data. 

Who is this project for?
This project has tutorials and widgets to help you connect sensors, a microcontroller, and a computer. It aims to simplify the step of writing Python code for displaying the sensor data.

Here's who this project is not for ... This library is intended to be used by Python programmers. If you haven't programmed before or haven't programmed in Python, this library isn't for you. This library is intended to help you connect your hardware and your computer quickly but in an unpolished way. It doesn't involve real time operating systems. Also, it isn't for highly customizable and polished products. You'll want more developed tools for that task.

## 2.0 Installation

### 2.1 Check python version

If you do not know what verison you have, you can execute the below command in the cmd line

 ```python
 py --version
 ```
 
### 2.2 GitHub Dandy
 
 Download Dandy repository, open the command prompt and execute the command of below.
 
 ```python
 git clone https://github.com/amitofsk/dandy.git
 ```
 
### 2.3 Install the pyserial library

In the command line execute
```python
pip install pyserial
```


## 3.0 Displaying Didital Inputs

### 3.1 Tkinter widgets 

```python
import tkinter as tk

# We re defining a class named DigitalNoHW here.
class DigitalNoHW:

# The function __init__ is the constructor for the class.
    def __init__(self):
        self.main_window=tk.Tk()
        self.button_quit=tk.Button(self.main_window, text="Quit", \
                            command=self.main_window.destroy)
        self.button_quit.pack()
        tk.mainloop()

# Here is our main function which creates an object of class DigitalNoHW.
if __name__=="__main__":
    mygui=DigitalNoHW()

```
Run the code of above, you will see a window with a working quick button.

(TODO Andy, put pictures)

```python
import tkinter as tk

# We re defining a class named DigitalNoHW here.
class DigitalNoHW:

# The function __init__ is the constructor for the class.
    def __init__(self):
        self.main_window=tk.Tk()
        self.button_quit=tk.Button(self.main_window, text="Quit", \
                            command=self.main_window.destroy)
        self.button2=tk.Button(self.main_window, text="Toggle", \
                            command=self.main_window.getValue)
        self.button_quit.pack()
        self.button2.pack()
        tk.mainloop()
    def getValue(self):
        print ("Comming soon")
        
# Here is our main function which creates an object of class DigitalNoHW.
if __name__=="__main__":
    mygui=DigitalNoHW()
```

(TODO Andy, put pictures)

Run the code of above and you will see two button in a window, when you press the Toggle button you will see the message Comming Soon in the command line.

### 3.2 Dandy Widgets
Until, we have only using python with the tkinter library, now we are using the widgets of the Dandy library

```python
import tkinter as tk
import sys
sys.path.append ('../widgets') 
import LEDDisplay as ld

# We re defining a class named DigitalNoHW here.
class DigitalNoHW:

# The function __init__ is the constructor for the class.
    def __init__(self):
        self.main_window=tk.Tk()
        self.button_quit=tk.Button(self.main_window, text="Quit", \
                            command=self.main_window.destroy)
        self.button2=tk.Button(self.main_window, text="Toggle", \
                            command=self.main_window.getValue)
        self.led1.LEDDisplay(self.main_window)
        self.button_quit.pack()
        self.button2.pack()
        self.led1.pack()
        tk.mainloop()
        
    def getValue(self):
        if (self.led1.get_color()=='yellow'):
             self.led1.change_LED_color ("blue")
        elif (self.led1.get_color()=='blue'):
             self.led1.change_LED_color ("yellow")
# Here is our main function which creates an object of class DigitalNoHW.
if __name__=="__main__":
    mygui=DigitalNoHW()
```

When executing the code of above, you will two button & an LED and when you press the Toggle button the LED color changes.

(TODO Andy, put pictures)

### 3.3 Hardware: LED, button, RPiPico

#### 3.3.1 Solder headers on RPiPico
(TODO Andy, put pictures) If there are not headers on the RPi then they can be soldered.

#### 3.3.2 Build the circuit
Connect a button and a resistor between GP16 & 5V (pin 39) <br>
Connect a resistor and LED between GP19 & GND

(TODO Andy, put pictures)

#### 3.3.3 Install Micropython on the RPiPico
Follow the instructions provided by Thonny link thru the Use digital inputs and outputs.

### 3.4 Hardware & Dandy Widgets
### 3.5 Hrdware, Dandy, Widgets & asyncio

## 2.0 Analog Sensors