---
draft: true 
date: 2023-03-03
categories:
  - Python
  - Multiprocessing
---

# Caution with Classes in Python`s Multiprocessing
Multiprocessing can be a great way of scaling Python applications beyond one CPU core, especially due slow speed compared to other lower-level languages like C or Java. However, one has to be very careful when passing Python class instance!

Let us consider the following minimal example:
```python
import multiprocessing
import time
from dataclasses import dataclass

# Set Multiprocessing "Fork" Method:
multiprocessing.set_start_method("fork")

@dataclass
class MyClass:
    attribute: str

    def __del__(self):
        self.attribute = "ups"


def modify_attribute(my_class: MyClass, value: str, wait_time: int) -> str:
    # Wait time to be sure that previous process has been finished:
    time.sleep(wait_time)

    # Store old attribute value to return it later:
    message = f"Old value was '{my_class.attribute}'. Assigning new value '{value}'."

    # Change attribute value on class instance:
    my_class.attribute = value

    return message

# Create class instance in parent process:
my_class_instance = MyClass(attribute="initial value")

# Run 3 child processes that modify the class instance one after another:
with multiprocessing.Pool(processes=3) as pool:
    messages = pool.starmap(
        modify_attribute,
        [
            (my_class_instance, "first change", 0),
            (my_class_instance, "second change", 1),
            (my_class_instance, "third change", 2),
        ],
    )

# Print out messages from the child processes:
for message in messages:
    print(message)

```

From this script, we usually would expect:

    Old value was 'initial value'. Assigning new value 'first change'.
    Old value was 'first change'. Assigning new value 'second change'.
    Old value was 'second change'. Assigning new value 'third change'.

but what we get if we run the script is:
  
    Old value was 'initial value'. Assigning new value 'first change'.
    Old value was 'initial value'. Assigning new value 'second change'.
    Old value was 'initial value'. Assigning new value 'third change'.

The reason behind this behaviour is that in order to run the function `modify_attribute` in a different process, **Python has fork the complete Python  interpreter in the child process**. This basically means, that at the start of each subprocess, all 3 child processes will have the same state that is [identical to the parent process](https://docs.python.org/3/library/multiprocessing.html#contexts-and-start-methods). This will erase all correlation between the different `my_class` instances, such that the attribut changes will not be seen by the other processes (since the objects point to completely different memory adresses).
