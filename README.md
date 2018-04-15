pyusbmodule
===========

[![Circleci Build Status](https://circleci.com/gh/laigui/pyusbmodule/tree/master.svg?style=shield)](https://circleci.com/gh/laigui/pyusbmodule) [![Travis Build Status](https://travis-ci.org/laigui/pyusbmodule.svg?branch=master)](https://travis-ci.org/laigui/pyusbmodule) 

Python interface to expansion modules via USB connection.


## Installation

```
pip3 install -U pyusbmodule
```


## Usage

```
>from usbmodule import r4i4d
>instr = r4i4d.RelayModule('/dev/ttyUSB0', 1) 
>instr.get_digital_inputs()
```

## License

[Apache](http://www.apache.org/licenses/LICENSE-2.0)

