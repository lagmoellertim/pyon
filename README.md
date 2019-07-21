# Pyon
<p align="center">
  <img src="https://github.com/lagmoellertim/pyon/raw/master/pyon.png" width="40%"/>
</p>

## Introduction
**Pyon** (Pythonic JSON) is a Python library which allows you to **easily convert native objects into JSON objects**.

It also supports **filesystem-like path-structure**, 
which allows you to easily construct you JSON objects just the way you like it.

Additionally, it uses recursion in order to also **convert every connected object** into a usable form.

## Prerequisites

- Python >= 3.2

## Installation
The installation via pip is as easy as typing
```sh
pip install pyon-lib
```
If you want to install the newest version manually, you can also do this:
```sh
git clone https://github.com/lagmoellertim/pyon.git

cd pyon

python3 setup.py install
```

## Build

```sh
git clone https://github.com/lagmoellertim/pyon.git

cd pyon

python3 setup.py sdist bdist_wheel
```

## Usage

### Import Pyon

```python3
from pyon import PyonObject
```

### Create a basic Object

```python3
class Test(PyonObject):
    def __init__(self):
        self.var1 = "Variable 1"
        self.var2 = 5.5
```

### Convert an object into JSON

```python3
test = Test()
json = test.generate_json()
```
And this is the output:
```python3
{'var1': 'Variable 1', 'var2': 5.5}
```

### Write the JSON object to a file

```python3
test = Test()
json = test.generate_json(file_object=open("test.json","w+"))
```

### Hide certain variables
Let's say your Test-Class only needs the variable var2 for it's own calculation, but you don't want it to
end up in your final JSON object. You can avoid this by adding the prefix "_"

```python3
class Test(PyonObject):
    def __init__(self):
        self.var1 = "Variable 1"
        self._var2 = 5.5
        
test = Test()
json = test.generate_json()
```
And this is the output:
```python3
{'var1': 'Variable 1'}
```

### Use multiple objects / classes
As an example, I use the concept of a store with products

```python3
class Store(PyonObject):
    def __init__(self, store_name):
        self.store_name = store_name
        self.products = [
            Product(0, "Smartphone"),
            Product(1, "Laptop")
        ]
        
class Product(PyonObject):
    def __init__(self, article_id, name):
        self.article_id = article_id
        self.name = name
        
store = Store("Generic Store")
json = store.generate_json()
```
And this is the output:

```python3
{
    'store_name': 'Generic Store',
    'products': 
        [
            {'article_id': 0, 'name': 'Smartphone'},
            {'article_id': 1, 'name': 'Laptop'}
        ]
}
```

### Specifying object paths
This time, the JSON structure should not be based on the class structure, but rather on the path string
that we supply.

Path Strings are very similar to your filesystem paths. You can navigate inside the JSON object using
these Path Strings.

Here are some example:

```python3
path1 = "/store/"

path2 = "/test/../store/./" # Identical to path1 since ../ means one layer up and ./ can be ignored

path3 = "/store/products/*" #The star symbol tells pyon to create a list instead of a dict in this location
```
Let's modify our Store / Products Class in order for it to use custom paths

```python3
class Store(PyonObject):
    def __init__(self, store_name):
        super().__init__("/stores/*")
        self.store_name = store_name
        self.products = [
            Product(0, "Smartphone"),
            Product(1, "Laptop")
        ]
        
class Product(PyonObject):
    def __init__(self, article_id, name):
        super().__init__("products/*")
        self.article_id = article_id
        self.name = name
        
store = Store("Generic Store")
json = store.generate_json()
```
And this is the output:
```python3
{
    'stores':
    [
        {'store_name': 'Generic Store', 'products': 
            [
                {'article_id': 0, 'name': 'Smartphone'},
                {'article_id': 1, 'name': 'Laptop'}
            ]
        }
    ]
}

```
As you can see in the example above, relative paths are also possible as long as the object has a parent.

### Use object variables for the Path String
To use object variables inside of you Path String, simply specify them in the String using brackets like
this: {var1}

The value of {var1} is self.var1 , so you just leave the 'self.' away.

```python3
class Test(PyonObject):
    def __init__(self):
        super().__init__("/test/{var1}-{_var2}/")
        self.var1 = "Variable 1"
        self._var2 = 5.5
        
test = Test()
json = test.generate_json()
```
And this is the output:
```python3
{
    'test':
    {
        'Variable 1-5.5': {'var1': 'Variable 1'}
    }
}
```

### Allow Overwrite
Finally, there is Overwrite Protection. Since Paths allow you to freely choose the location where the
object should end up, it is possible for them to overlap. To allow / stop overwriting, you can do this:

```python3
json = test.generate_json(allow_overwrite=True)
```
The default value for allow_overwrite is False

## Documentation

If you get stuck at some point while trying to use the API, take a look the code. It is fully commented and well-labeled,
which should help you understand what's going on.

## Contributing

If you are missing a feature or have new idea, go for it! That is what open-source is for!

## Author

**Tim-Luca Lagmöller** ([@lagmoellertim](https://github.com/lagmoellertim))

## Donate

You can also contribute by [buying me a coffee](https://www.buymeacoffee.com/lagmoellertim).

## License

[MIT License](https://github.com/lagmoellertim/pyon/blob/master/LICENSE)

Copyright © 2019-present, [Tim-Luca Lagmöller](https://en.lagmoellertim.de)

## Have fun :tada:
