pyusbmodule
===========

[![Travis Build Status](https://travis-ci.org/laigui/pyusbmodule.svg?branch=master)](https://travis-ci.org/laigui/pyusbmodule) 
[![Test coverage report](https://codecov.io/gh/laigui/pyusbmodule/coverage.svg?branch=master)](https://codecov.io/gh/laigui/pyusbmodule) 

Python interface to expansion modules via USB connection.


## Installation

```
pip3 install -U pyusbmodule
```


## Usage

```
# the package
from usbmodule import r4i4d

# using class
instr = r4i4d.RelayModule('/dev/ttyUSB0', 1) 
instr.debug = True

# using module method
instr.get_digital_inputs()
```

## License

[Apache](http://www.apache.org/licenses/LICENSE-2.0)

