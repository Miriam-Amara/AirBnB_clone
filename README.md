# **AirBnB Clone Project**


## Table of Contents

1. [Project Overview](#project-overview)
2. [Phases](#phases)
    - [The Console](#the-console)
    - [Web Static](#web-static)
    - [MySQL](#mysql)
    - [Deploy Static](#deploy-static)
    - [Web Framework](#web-framework)
    - [RESTful API](#restful-api)
    - [Web Dynamic](#web-dynamic)
3. [Technologies Used](#technologies-used)
4. [Features](#features)
5. [Project Stat](#project-stat)

---



## Project Overview

This project is a clone of AirBnB web application for learning purposes. AirBnB is an online application that connects property owners with travelers looking for short-term rentals.

The project is divided into **7 phases*, each building upon the previous to replicate key functionality of Airbnb:
1. **The Console**
2. **Web Static**
3. **MySQL**
4. **Deploy Static**
5. **Web Framework**
6. **RESTful API**
7. **Web Dynamic**

---



## Phases

### The Console

- **Created** a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of instances.
- **Implemented** a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- **Developed** all classes used for AirBnB (User, State, City, Place, Amenity and Review) that inherit from BaseModel.
- **Designed** the first abstracted storage engine of the project: File storage.
- **Wrote** all unittests to validate all classes and storage engine.

Additionally, **built** a command Interperter (interactive shell) to manage the objects with the following commands:

1. **create:** - Creates a new object (ex: a new User or a new Place)
2. **all:** - Retrieves all objects or specified objects from a file, database, etc...
3. **show:** - Displays an object based on its ID.
4. **count:** - Computes the number of objects for a given class.
5. **update:** - Updates attributes of an object.
6. **destroy:** - Deletes an object from storage.

---



## Technologies Used

**Programming Language:** Python
**Storage:** JSON-based file storage
**Version control:** Git/GitHub
**Testing:** Unittest

---



## Features

- Object serialization and deserialization.
- Dynamic command parsing (ex: ClassName.command(arguments))
- Modular structure for scalability.
- Interactive and non-interactive modes.


## Project Stat

Ongoing

This project is actively under development, README will be updated accordingly..
