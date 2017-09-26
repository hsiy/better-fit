
## Generic sensor interaction code

This code provides a refreence implementation for integrating multiple sensor APIs. 

The main code is readsensor.py which continuously reads from a sensor and outputs the readings to a specified display. Its usage is:

```
python readsensor.py mpu|lsm|dummy [print|plotly]
```
Choose a sensor from:
* mpu (MPU6050)
* lsm (LSM9DS0) 
* dummy (random generator for testing)

Choose a display from:
* print (print to text output, this is the default if blank)
* plotly (send to plot.ly)

The code structure is organized as follows:

![Code structure](https://yuml.me/diagram/plain;dir:LR/class/[readsensor]-%3E[%3C%3Cdisplay%3E%3E],%20[%3C%3Cdisplay%3E%3E]%5E-.-[printOut],%20[%3C%3Cdisplay%3E%3E]%5E-.-[plotlyOut],%20[readsensor]-%3E[%3C%3Csensorapi%3E%3E],%20[%3C%3Csensorapi%3E%3E]%5E-.-[dummysensor],%20[%3C%3Csensorapi%3E%3E]%5E-.-[mpu6050api],%20[%3C%3Csensorapi%3E%3E]%5E-.-[lsm9ds0api])

<!--- 
Original code passed to yuml.me:
https://yuml.me/diagram/plain;dir:LR/class/[readsensor]->[<<display>>], [<<display>>]^-.-[printOut], [<<display>>]^-.-[plotlyOut], [readsensor]->[<<sensorapi>>], [<<sensorapi>>]^-.-[dummysensor], [<<sensorapi>>]^-.-[mpu6050api], [<<sensorapi>>]^-.-[lsm9ds0api] 
--->

Note that sensorapi and display are just placeholders representing the real modules.



