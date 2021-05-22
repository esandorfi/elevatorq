# elevatorq_ui : frontend interface

Made with Vite and Vue3 - Javascript

## Directory structure

| Apps                     |                                                                                                        |
| ------------------------ | ------------------------------------------------------------------------------------------------------ |
| dist                     | build ui from `yarn build` served by django - connected to a template view and a assets static storage |
| public                   | favicon - duplicate with django server faveico in static                                               |
| src                      | vue3 application                                                                                       |
| src.assets               |                                                                                                        |
| src.components           |                                                                                                        |
| src.components.elevatorq |
| src.json                 | mock json resturn if api failed or for initial build                                                   |
| src.store                |                                                                                                        |
| src.store.elevatorq      |                                                                                                        |
| src.utils                |                                                                                                        |
| index.html               | home                                                                                                   |
| .env                     | dev environment                                                                                        |

## Build

run vite server for dev

```
yarn dev
```

build vite frontend to be served by django

```
yarn build (keep the dist directory and use to serve asserts and template in django)
```
