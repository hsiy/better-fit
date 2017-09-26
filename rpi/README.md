
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

![Code structure](https://yuml.me/diagram/plain;dir:LR/class/[readsensor]->[<<display>>], [<<display>>]^-.-[printOut], [<<display>>]^-.-[plotlyOut], [readsensor]->[<<sensorapi>>], [<<sensorapi>>]^-.-[dummysensor], [<<sensorapi>>]^-.-[mpu6050api], [<<sensorapi>>]^-.-[lsm9ds0api])

Note that sensorapi and display are just placeholders representing the real modules.



