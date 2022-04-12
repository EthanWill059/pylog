# pylog
 A module to import for simple, custom, hackable live log messages in a python progam.

## Use

import pylog into program by having it in the same folder and then use
`import pylog`

Then the log object must be defined

**Example**

`log = pylog.log()`

To output a message then use

`log.out(msg='This is a log message', type='msg')` This would show up green as a message

`log.out(msg='This is a log error', type='error')` This would show up red as an error
