# DANDY - Data Acquisition aNd DisplaY

## What is DANDY?

[DANDY](https://github.com/amitofsk/dandy) is a set of reusable python examples and a library of python functions to help display sensor data in a graphical user interface (GUI).

## What are we building?

Here's a typical hardware setup. A sensor is connected to a microcontroller. The microcontroller sends the sensor data to a computer either over USB or wirelessly. Data is displayed in a GUI on the laptop, perhaps numerically, as a needle rotating in a dial, using a slider, or on a chart plot.


All of these steps can be implemented using existing open software, but some steps are easier than others. For example, Arduino makes writing the microcontroller software easy, and Tkinter and Qt are user-friendly libraries for writing GUIs.

**Where are the challenges in writing the software?**

First, the code for the microcontroller and the code for the GUI on the laptop are typically written in different languages. Multiple languages are not a problem for an experienced coder, but they are an obstacle for a novice or a hobbyist. Second, libraries for writing GUI software typically have reusable widgets like buttons and spinboxes, but they don't have ones made specifically for handling inputs from analog sensors. Third, the software on the laptop has to both continually read from the sensors and continually update the GUI. These should appear to the user to happen simultaneously, without either task blocking the other.


This project addresses all of these challenges. The goal of this project is not to show a new application of a sensor. Instead, it is to simplify writing software for this typical setup easier.
![Overview Diagram](./docs/docPics/OverviewDiagram2.png)


## Who is this project for?

This project is intended for:
 - Students interested in learning about sensor hardware, microcontroller programming,  and writing GUI software.
 - Engineers who want to learn a new way to perform data acquisition using the Python language.
 - People with at least a little Python coding experience. For example, you should know how to write functions in Python, and you should know what classes and objects are.


This project is NOT for you if:
 - You have not programmed before.
 - You want a plug-and-play solution. This is a software library, so you will have to program.
 - You want to acquire sensor data with precise timing. In this project, data collection happens with an inexpensive microcontroller without a real time operating system.
 - You want to collect data using elaborate equipment. This project involves small discrete sensors.


## What is in DANDY?

This project contains:
 - Example MicroPython, CircuitPython, and Arduino programs for reading from sensors connected to a Raspberry Pi Pico, Arduino, or PSoC6 microcontroller
 - Example Python programs for displaying sensor data graphically on a computer
 - A set of reusable widgets designed for displaying numerical data from sensors or sending numerical data to actuators
![](./docs/docPics/summaryWidgets.png)
 
 - Additional widgets designed to look like specific microcontrollers
![](./docs/docPics/summaryPicMC.png)

 - An [API](./docs/widgetApi.md) describing how to use the widgets
 - A [tutorial](./docs/Dandy.md) demonstrating how to use everything


## What should I do next?

 **READ THE [TUTORIAL](./docs/Dandy.md)!!!**

