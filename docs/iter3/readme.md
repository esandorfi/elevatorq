# Elevator Q / Iteration 3

check the demo at http://elevatorq.herokuapp.com
to access the admin, login with user _emmanuel_ and pwd _sandorfi_

## Duet : Product Manager and Engineer

We simplify our [first](../iter1/readme.md) and [second](../iter2/readme.md) design thinking iteration, and focus on the result we want : optimize UX, keep the LOOK algorithm, fixed use cases for the elevators fleet. We keep the technology : python, django api, javascript.

## Goals UX for Elevator Q

### Clarity : people input and system display

1. INPUT_FIXED_CASES :  
   Demonstration interface focused on **fixed use cases** :  
   Have a dataset of people who press the elevator button, depart floor to arrival floor

```
ex: Floor 0 to Floor 17, Floor 3 to Floor 0, etc...
```

2. RESPONSE_ELEVATOR_NAME,
3. RESPONSE_WAITING_INDICATOR :  
   After running people use case, immediate transition (or waiting indicator if needed) to **display the elevator name dispatched** to this travel, with a **waiting indicator before door open** at people floor.

```
ex: Elevator A has 10 floors, 2 stops before arrival
ex: Elevator A arrival very soon/in a minute/is long sorry...
```

4. DISPLAY_ELEVATORQ,
5. BEAT_ELEVATORQ_ONOFF :  
   Demonstration interface **display the elevator queue**, as an independant monitoring system, with an **on/off toggle** the start or shutdown the system.

```
ex: start the beat / simulate the elevator system
ex: direct stop or bring all elevators to last case and stop
```

### Performance : people waits and people lifted

6. RESPONSE_WAITING_INDICATOR (already saw)
7. CONTROL_SYSTEM : Use the distributed server django api and the look algorithm.

## Directory structure

| Apps         |                                                     |
| ------------ | --------------------------------------------------- |
| ...          | misc files for project settings                     |
| algo         | sandbox for personnal testing                       |
| docs         | thoses readme                                       |
| elevatorq    | backend app ( python, django )                      |
| elevatorq_ui | frontend app ( vitejs, vue3 )                       |
| server       | django server settings                              |
| staticfiles  | django package staticfiles, automatically generated |

## Build

### django as backend + vite as frontend

run django server

```
python manage.py runserver 127.0.0.1:81 (or 8000 by default)
```

run vite server for dev

```
elevatorq_ui\yarn dev (no connection with django)
```

build vite frontend to be served by django

```
elevatorq_ui\yarn build (keep the dist directory and use to serve asserts and template in django)
```

make django default url to elevatorq_ui\dist\index.html

### serve as heroku

collectstatic if packages updated before deploy

```
python manage.py collectstatic
```

deploy on elevatorq.herokuapp.com

```
git push heroku
```

## Coding day

Before the coding day, check :

-   LOOK from the net : make it work
-   FLEET : just get a look...
-   MODEL : create raw python model and validation for people input

#### Day 1 ( 9am to 1pm )

1. Create the orm

-   PRESSBTNQ
-   ELEVATORQ
-   BUILDINGELEVATOR

2. Create the api

-   /api/pressbtnq/
-   /api/elevatorq/
-   /api/building/
