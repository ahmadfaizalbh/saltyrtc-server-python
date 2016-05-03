# SaltyRTC Signalling Server

This is an implementation of the SaltyRTC Signalling Server which allows end-to-end
encrypted signalling for WebRTC and ORTC.

## Note

On machines where Python 3 is not the default Python runtime, you should use
``pip3`` instead of ``pip``.

## Prerequisites

    $ sudo apt-get install python3 python3-pip

We recommend using [venv](https://docs.python.org/3/library/venv.html) to
create an isolated Python environment:

    $ pyvenv venv

You can switch into the created virtual environment *venv* by running this
command:

    $ source venv/bin/activate

All packages you install now with `pip` will be installed into your virtualenv.

To deactivate the virtual environment, just run:

    $ deactivate

## Installation

If you are using a virtual environment, activate it first.

Install the module by running:

```
$ pip install git+https://github.com/saltyrtc/saltyrtc-server-python.git
```

The dependency ``libnacl`` will be installed automatically. However, you may need to
[install ``libsodium``](https://download.libsodium.org/doc/installation/index.html) for ``libnacl``
to work. 

## Command Line Usage

TODO
