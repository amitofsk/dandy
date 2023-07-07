#API for the Dandy project
I haven't used .md files before... let's see if this works.

##API for the Widgets Directory

###LEDDisplay class
####Description
A LEDDisplay object is used to display a digital input bit. 

#####Member Functions 
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


#####Options
#####Examples
```
led1=LEDDisplay.LEDDisplay(self.main_window)
```






