# dandy
Data Acquisition aNd DisplaY

## What is DANDY?

[`DANDY`](https://github.com/amitofsk/dandy) is a set of reusable python examples and a library of python functions to help display sensor data in a graphical user interface (GUI).

## What are we building?

Here's a typical hardware setup. A sensor is connected to a microcontroller. The microcontroller sends the sensor data to a computer either over USB or wirelessly. Data is displayed in a GUI on the laptop, perhaps numerically, as a needle rotating in a dial, using a slider, or on a chart plot.
<br><br>
All of these steps can be implemented using existing open software, but some steps are easier than others. For example, Arduino makes writing the microcontroller software easy, and Tkinter and Qt are user-friendly libraries for writing GUIs.

**Where are the challenges in writing the software?**

First, the code for the microcontroller and the code for the GUI on the laptop are typically written in different languages. Multiple languages are not a problem for an experienced coder, but they are an obstacle for a novice or a hobbyist. Second, libraries for writing GUI software typically have reusable widgets like buttons and spinboxes, but they don't have ones made specifically for handling inputs from analog sensors. Third, the software on the laptop has to both continually read from the sensors and continually update the GUI. These should appear to the user to happen simultaneously, without either task blocking the other.
<br><br>
This project addresses all of these challenges. The goal of this project is not to show a new application of a sensor. Instead, it is to simplify writing software for this typical setup easier.
![Overview Diagram](./docs/docPics/OverviewDiagram2.png)


## Who is this library for?

This guide is intended for:
 - Students interested in learning about sensor hardware, microcontroller programming,  and writing GUI software.
 - Engineers who want to learn a new way to perform data acquisition using the Python language.
 - People with at least a little Python coding experience. For example, you should know how to write functions in Python, and you should know what classes and objects are.
<br><br>

This guide is NOT for you if:
 - You have not programmed before.
 - You want a plug-and-play solution. This is a software library, so you will have to program.
 - You want to acquire sensor data with precise timing. In this project, data collection happens with an inexpensive microcontroller without a real time operating system.
 - You want to collect data using elaborate equipment. This project involves small discrete sensors.


## What is in the library?

This library contains
 - Example code for four microcontrollers
 - Example code for displaying ... Python on computer
 - Code for asyncio ...
 - Reusable widgets specifically for displaying numerical data from sensors... and a resuable widget for sendign numerical data to ...
 - Widgets designed to look like specific microcontrollers
 - A tutorial explaining how to use everything
 - An API describing how to use the widgets 
![](./docs/docPics/summaryWidgets.png)
![](./docs/docPics/summaryPicMC.png)

## What should I do next?

Download the library from github...

Read the tutorial ...

Find a microcontroller, and try it out!
