# kbaseapp

Kotoko basic app structure.

## Usage

```python

from kbaseapp.wamp_app import WampApp, register_method

class MyApplication(WampApp):
    def init(self):
        # Initialize things here instead of
        # overloading __init__ method.
        pass

    @register_method('kotoko.my_method')
    def my_method(self, x):
        return x * 10

```
