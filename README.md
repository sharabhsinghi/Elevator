# Elevator

To run, import Elevator

## Pre added code
```
b = Manager(12,-2)
e1 = Elevator("E1",0,0)
e2 = Elevator("E2",10,-1)
b.add_elevators(e1,e2)
```

## Usage
To simply use it as it is,
add calls to the manager-
```
#b.ping(from,to)
b.ping(0,10)
b.ping(1,5)
b.ping(6,3)
b.ping(7,9)
b.ping(5,-1)
b.run_ele()
```

else, edit Elevator.py
and configure the manager yourself.
