# Elevator Q / Iteration 3 / v1.1

We simplify our [first](../iter1/readme.md) and [second](../iter2/readme.md) design thinking iteration, and focus on the result we want : optimize UX, keep the LOOK algorithm, fixed use cases for the elevators fleet. 

*Last documentation update : 24 may 2021*

---

**[Go for an online demo : elevatorq.herokuapp.com](http://elevatorq.herokuapp.com)**

-   to login the admin : user _**admin**_, pwd _**admin**_
-   _might take a little time to load at the first access_

---

[[_TOC_]]



---

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

## Application and directory structure

| Apps           |                                                     |
| -------------- | --------------------------------------------------- |
| ...            | misc files for project settings                     |
| docs           | thoses readme                                       |
| elevatorq      | backend app : orm, admin                            |
| elevatorq.api  | rest api for the front                              |
| elevatorq.algo | elevator fleet alogrithms                           |
| elevatorq_ui   | frontend app ( vitejs, vue3 )                       |
| sandbox        | code for personnal testing                          |
| server         | django server settings                              |
| staticfiles    | django package staticfiles, automatically generated |

We use :

- **django** as backend orm, http and api server
- **vite/vuejs/bootstrap5** as front interface
- **heroku** as deployed container with standard sqllite/static : online data are erased at each deploy
- **mypy** for python typing 

In future :

- add pytest
- convert javascript to typescript
- add jest, cypress

## Coding days

### Before the coding days

#### Think about the project as Product Manager and an Engineer

- do sketches 
- design thinking
- build thinking
- read the thinking with the constraints and the objectives 
- iterate again if needed

#### Do some python exercises

-   LOOK from the net : make it work
-   FLEET : just get a look...
-   MODEL : create raw python model and validation for people input

#### Setup the application and do some front exercises

- install django ecosystem
- install vite/vuejs ecosystem
- create bootstrap starting template
- connect django and vite 
- deploy on online cloud - this case : heroku

### Part 1 : the datas

1. Create the orm : [elevatorq.models](../../elevatorq/models.py)

-   `PressBtnQ`
-   `ElevatorQ`
-   `BuildingElevator`

2. Setup the admin  : [elevatorq.admin](../../elevatorq/admin.py)
3. Create the api : [elevatorq.api.urls](../../elevatorq/api/urls.py)

-   `/api/pressbtnq/`
-   `/api/elevatorq/`
-   `/api/building/`

4. Update navbar of the front : [elevatorq_ui](../../elevatorq_ui/readme.md)

### Part 2 : the algo

1. Algo input and dispatch : [elevatorq.algo.eq](../../elevatorq/algo/eq.py)

### Part 3 : the algo (part 2)



### Part 4 : the front

1. Add lobby elevator control summary
2. Update the components architecture with a store
3. Connect with `/api/building/`
4. Manage errors as alerts
5. Prepare `pressbtnq` and `elevatorq` display





## Sketches

### Design thinking

| User interface            | Elevators Administration  |
| ------------------------- | ------------------------- |
| ![design_1](design_1.jpg) | ![design_2](design_2.jpg) |
| ![design_3](design_3.jpg) |                           |

### Build thinking

| Data                    | Algorithm               |
| ----------------------- | ----------------------- |
| ![build_1](build_1.jpg) | ![build_2](build_2.jpg) |
|                         | ![build_3](build_3.jpg) |

## Build and deploy

### django as backend

run django server

```
python manage.py runserver 127.0.0.1:81 (or 8000 by default)
```

### vite as frontend

run vite server for dev

```
elevatorq_ui\yarn dev (no connection with django)
```

build vite frontend to be served by django

```
elevatorq_ui\yarn build (keep the dist directory and use to serve asserts and template in django)
```

make django default url to elevatorq_ui\dist\index.html

### deploy on heroku

collectstatic if packages updated before deploy

```
python manage.py collectstatic
```

deploy on elevatorq.herokuapp.com

```
git push heroku
```

## Changelog

v1.0 : initial release for coding challenge (21 may)

v1.1 : build and design enhancement (24 may)

