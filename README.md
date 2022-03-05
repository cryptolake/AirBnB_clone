# AirBnB clone - The console

## Description

HolbertonBnB is a complete web application, integrating database storage, 
a back-end API, and front-end interfacing in a clone of AirBnB.
The project currently only implements the back-end console.


## Storage

Every time the backend is initialized, HolbertonBnB instantiates an instance of 
`FileStorage` called `storage`. The `storage` object is used to load
any class instances stored in the JSON file `model.json`. As class instances are 
created, updated, or deleted, the `storage` object is used to register 
corresponding changes in the file.

## Console

The console is a command line interpreter that permits management of the backend 
of HolbertonBnB. It can be used to handle and manipulate all classes utilized by 
the application (achieved by calls on the `storage` object defined above).

### Using the Console


To use the HolbertonBnB console, run the file `console.py` by itself:

```bash
$ ./console.py
```

To quit the console, enter the command `quit` or  `ctrl-D`.

```bash
$ ./console.py
(hbnb) quit
$
```

```bash
$ ./console.py
(hbnb) EOF
$
```

### Console Commands

The HolbertonBnB console supports the following commands:

* usage: `create <class>`
* show: `show <class> <id>`
* destroy: `destroy <class> <id>` 
* all: `all [class]`
* update: `update <class name> <id> <attribute name> "<attribute value>"`

## Testing

To run the whole test suit, execute the following command:

```bash
$ python3 -m unittest discover tests
```

Alternatively, you can specify a single test file to run at a time:

```bash
$ python3 -m unittest tests/test_models/test_base_model.py
```

## Authors
[Dhia Dahmeni](https://github.com/cryptolake)
