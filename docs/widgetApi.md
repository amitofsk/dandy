# API for the Widgets Directory of the  Dandy project
I haven't used .md files before... let's see if this works.

## AMKRDisplay Class
### Description
This class is used to display an Arduino MKR1010.

### Member Functions
### Options
### Examples
### Notes
### Similar Classes 


## AnalogInDisplay Class
### Description
AnalogInDisplay is the parent class of a number of widgets used to display analog input values coming from a sensor, through a microcontroller, to a computer. You should declare objects of its child classes, not itself.
### Member Functions
### Options
### Examples
### Notes
### Similar Classes 


## ANanoEveryDisplay
### Description
This class is used to display an Arduino Nano Every.
### Member Functions
### Options
### Examples
### Notes
### Similar Classes 


## AUnoDisplay
### Description
This class is used to display an Arduino Uno.
### Member Functions
### Options
### Examples
### Notes
### Similar Classes 


## Cyc8protoDisplay
### Description
This class is used to display an Infineon Cyc8proto.
### Member Functions
### Options
### Examples
### Notes
### Similar Classes 


## DialDisplay
### Description
A DialDisplay object displays analog input values as a needle on a dial.
### Member Functions
### Options
### Examples
### Notes
### Similar Classes 


## LEDBarDisplay 
### Description
An LEDBarDisplay object displays multiple digital input bits as an LED bar. 
### Member Functions
### Options
### Examples
### Notes
### Similar Classes 


## LEDDisplay class
### Description
A LEDDisplay object is used to display a digital input bit. 

### Member Functions 
```
Here's the constructor
___init___(self, LED_window, height=100, width=100, color="yellow")
```
Here are the other member functions...

```
pack(self, LED_orientation="vertical")
```
In the function above, LED_orientation may be horizontal or vertical.

```
change_LED_color(self, new_color)
```

```
change_BG_color(self, new_color)
```

```
draw_LED(self)
```


### Options
### Examples
```
led1=LEDDisplay.LEDDisplay(self.main_window)
```
### Notes
### Similar Classes

## MCDisplay class
### Description
### Member Functions
### Options
### Examples
### Notes
### Similar Classes 


## RPiDisplay class
### Description
### Member Functions
### Options
### Examples
### Notes
### Similar Classes 


## RPiPicoDisplay class
### Description
### Member Functions
### Options
### Examples
### Notes
### Similar Classes 


## SimplePlotDisplay class
### Description
### Member Functions
### Options
### Examples
### Notes
### Similar Classes 

## SlideDisplay
### Description
### Member Functions
### Options
### Examples
### Notes
### Similar Classes 

## SymbolDisplay
### Description
### Member Functions
### Options
### Examples
### Notes
### Similar Classes 

## TricolorDisplay 
### Description
### Member Functions
### Options
### Examples
### Notes
### Similar Classes 

## VectorDisplay
### Description
### Member Functions
### Options
### Examples
### Notes
### Similar Classes 



