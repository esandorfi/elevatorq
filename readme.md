# WAVE&EVOL - An elevator dispatch system


## timeframe @emmanuel

- friday 14 may : 3h15
  - reading objectif
  - first design as a product manager
  - from hand sketchs, turn it in markdown and git init


## as a product manager

We'll use a **Destination dispatch** elevator control system.  
Please read about it : [here on elevation.fandom.com](https://elevation.fandom.com/wiki/Destination_dispatch).

![sample](docs\dispatch_elevator_system.png)
*ref: a dispatch system in a business building*

But we'll use a mix wide test case instead of only business uses as in an entreprise building. 
We'll focus on a fleet of elevators inside an hotel.   
Go to **the Marriott Marquis midtown** (NYC/Broadway), and make a mixing of Professional, Personal and Leisure use cases.

We'll divide our system in two essential parts : the hotel setup (admin) and the people experience (ux).

## the hotel setup (admin)

![sketch](docs/pm_hotel_setup_1.jpg)b
*ref: first notes - half right*

Of course, every building/hotel is different. Here's the case of the Mariott we should build now.

### 1) physical building setup
Info | Values | More |
--- | --- | -- |
| nb of floors | 47 |
| roof | 47 |  **the view restaurant** :  [have a look in images](https://www.google.com/search?q=marriott+marquis+the+view+restaurant&tbm=isch)<br>If the project is sucessfull, we go and book !|
| rooms | 46 to 5 | hotel rooms |
| meeting | 4 to 1 | convention center |
| lobby | 0 | public entrance |
| nb of elevators | 6 |
| elevators name | A, B, C, D, E, F |

### 2) elevator dispatch versionning

By elevator dispatch, it's how to say which elevator is assign to witch group of floors.
And it's necessary to have a versionning of a setup, as it can change on daily time, with public influence.

Who change ? Cron, building manager, captors... More to expect.


We group elevators from people needs and uses and time :
- daylight version 
  - direct roof : the view
  - first floors and meeting only
  - rooms only
- night version :
  - direct roof : the view
  - rooms only 
  - rooms only and roof from rooms
- specific event version :
  - direct roof : the view
  - event meeting floor and rooms 
  - rooms only and roof from rooms
  



## the people experience (ux)

![sketch](docs/pm_ux_1.jpg)
*ref: first notes - half left*

### 1) mulitple main touch system 5 meters in front

### 2) less secondary touch system near the elevators

### 3) waiting or dispatch message

### 4) see elevators movements and status

### 5) extra 

- scan your marriott id card to get access to your direct room floor
- meetings screens : select to go to your elevator
 