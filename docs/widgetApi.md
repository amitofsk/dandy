# API for the Widgets Directory of the  Dandy project


## AMKRDisplay Class
### Description
This class displays an Arduino MKR1010.

### Member Functions
### Options
### Examples
### Notes
### Similar Classes 
AMKRDisplay is a child of MCDisplay. The class ANanoEveryDisplay displays an Arduino Nano Every. AUnoDisplay displays an Arduino Uno.

## AnalogInDisplay Class
### Description
AnalogInDisplay is the parent class of a number of widgets used to display analog input values coming from a sensor, through a microcontroller, to a computer. You should declare objects of child classes instead of AnalogInDisplay.
### Member Functions
### Options
### Examples
### Notes
### Similar Classes 
SlideDisplay, VectorDisplay, SimplePlotDisplay, and DialDisplay are child classes of AnalogInDisplay.


## ANanoEveryDisplay
### Description
This class displays an Arduino Nano Every.
### Member Functions
### Options
### Examples
### Notes
### Similar Classes 
ANanoEveryDisplay is a child of MCDisplay. AMKRDisplay displays an Arduino MKR1010. AUnoDisplay displays an Arduino Uno.


## AUnoDisplay
### Description
This class displays an Arduino Uno.
### Member Functions
### Options
### Examples
### Notes
### Similar Classes 
AUnoDisplay is a child of MCDisplay. AMKRDisplay displays an Arduino MKR1010. ANanoEveryDisplay displays an Arduino Nano every.


## Cy8cprotoDisplay
### Description
This class displays an Infineon Cyc8proto microcontroller.
### Member Functions
### Options
### Examples
### Notes
### Similar Classes 
Cyc8protoDisplay is a child of MCDisplay.


## DialDisplay
### Description
A DialDisplay object displays analog input values as a needle on a dial.
### Member Functions
### Options
### Examples
### Notes
### Similar Classes 
DialDisplay is a child of AnalogInDisplay. SlideDisplay, TricolorDisplay,  and SimplePlotDisplay also display analog input values.


## KnobDisplay
### Description
A KnobDisplay object displays a knob, and it can be used for generating an analog value.
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
I may eventually cut this class. Alternatively, I may modify it so that it can show either LEDs or other symbols.
### Similar Classes 


## LEDDisplay class
### Description
A LEDDisplay object displays a digital bit in a widget that looks like an LED. 

### Member Functions 
The constructor is:
```python
___init___(self, LED_window, height=100, width=100, color="yellow")
```

Setter and getter member functions:

```python
get_color(self)
```

```python
change_LED_color(self, new_color)
```

```python
get_bg_color(self) #bg stands for background
```

```python
change_bg_color(self, new_color) 
```

```python
set_size(self, width=100, height=100)
```

```python
get_pin_number(self) 
```
LEDDisplay widgets can be numbered by a pin number. If the number is nonzero, it will be displayed on
 the widget. Input `pin_value` should be an integer.

```python
set_pin_number(self, pin_value=0) 
```

```python
get_orientation(self)
```

LEDDisplay widgets can be rotated with the `set_orientation` function. The parameter `LED_orientation` can be `north`, `south`, `east`, or `west`. 

```python
set_orientation(self, LED_orientation="north")
```

Member functions related to packing: 

`Pack` puts a Tkinter widget in a window. The `bar_orientation` optional parameter may be `vertical` or `horizontal`. It is only used with an `LEDBarDisplay` widget.
```python
pack(self, bar_orientation="vertical")
```

`Pack_forget` removes a Tkinter widget from a window.
```python
pack_forget(self)
```

Member functions related to drawing an LED in different orientations:

The parameter `orientation` may be `north`, `south`, `east`, or `west`.
```python
draw_LED(self, orientation="north")
```

```python
draw_LED_north(self)
```

```python 
draw_LED_south(self)
```

```python
draw_LED_east(self)
```

```python
draw_LED_west(self)
```


### Examples
```python
import tkinter
import sys
sys.path.append('../widgets')
import LEDDisplay 

main_window=tkinter.Tk()
led1= LEDDisplay.LEDDisplay(main_window)
led1.change_LED_color("purple")
led1.set_orientation("east")
led1.pack()
tkinter.mainloop()
```
![LEDDisplay widget](./docPics/LEDDisplay.png)

### Similar Classes
`LEDBarDisplay` displays multiple `LEDDisplay` or `SymbolDisplay` widgets.

## MCDisplay class
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
SlideDisplay is used to display an analog input value as a slider along a bar.
### Member Functions
### Options
### Examples
### Notes
### Similar Classes 
SlideDisplay is a child of AnalogInDisplay. TricolorDisplay, DialDisplay, and SimplePlotDisplay also display analog input values. 

## SymbolDisplay
### Description
The SymbolDisplay class displays static symbols including ground and power symbols. When drawing a microcontroller, use these static symbols to display other pins which are neither inputs nor outputs. 
### Member Functions
### Options
### Examples
### Notes
### Similar Classes 

## TricolorDisplay 
### Description
The TricolorDisplay clas displays an analog input as if it went through a comparator to a tricolor LED. If the analog input is below one value, the LED is green. If it is between that value and a second value, the LED is yellow. If the analog input is above the second value, the LED is red.
### Member Functions
### Options
### Examples
### Notes
### Similar Classes 
TricolorDisplay is a child of the LEDDisplay class. The classes DialDisplay, SlideDisplay, and SimplePlotDisplay also display analog input values.

## VectorDisplay
### Description
VectorDisplay displays three analog input values as a vector. Use this class to display velocity, magnetic field at a point, or other vector quantities. 
### Member Functions
### Options
### Examples
### Notes
### Similar Classes 
VectorDisplay is a child of class AnalogInDisplay.



