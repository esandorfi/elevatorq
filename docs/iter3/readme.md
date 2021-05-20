# Elevator Q / Iteration 3

## Duet : Product Manager and Engineer

We simplify our [second iteration](../iter2/readme.md), and focus on the result we want : optimize UX, keep the LOOK algorithm, fixed use cases for the elevators fleet. We keep the technology : python, django api, javascript.

## Goals UX for an Elevator

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

| Apps         |                                             |
| ------------ | ------------------------------------------- |
| server       | settings for django api server with psql db |
| elevatorq    | django python app                           |
| elevatorq_ui | front javascript                            |
| docs         | thoses readme                               |
