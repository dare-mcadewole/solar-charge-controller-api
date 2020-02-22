# Solar Charge Controller API

> Flask + MongoDB + Pusher

Base URL: [https://solarchargecontroller.herokuapp.com/api](https://solarchargecontroller.herokuapp.com/api)

## Installation

**Make sure you have [git](https://git-scm.com/) installed**

- Clone this repository

```bash
git clone https://github.com/dare-mcadewole/solar-charge-controller-api.git
```  

- Install dependencies (using whatever version of Python you have installed)

```bash
pip3 install -r requirements.txt
```  

## Run

- Run the following command in bash

```bash
python3  app.py
```

## Documentation

Base URL: [https://solarchargecontroller.herokuapp.com/api](https://solarchargecontroller.herokuapp.com/api)

- Update Component data:  
    PUT `/api/component/<component>`  
    `<component>` can be any of 'solar_irradiance', 'exporting', 'current_usage', 'temperature', 'humidity',
    'depth_of_discharge', 'load', 'battery_status', 'module_id'  

    Request:

```http
    PUT /api/component/solar_irradiance HTTP/1.1
    content-type: application/json

    {
        "value": 100
    }
```
  
- Get Component data:  
    GET `/api/component/<component>`  
    `<component>` can be any of 'solar_irradiance', 'exporting', 'current_usage', 'temperature', 'humidity',
    'depth_of_discharge', 'load', 'battery_status', 'module_id'  

    Request:

```http
    GET /api/component/solar_irradiance HTTP/1.1
    content-type: application/json
```
  
- Send Power data:  
    POST `/api/power`  

    Request:

```http
    POST /api/power HTTP/1.1
    content-type: application/json

    {
        "value": 23
    }
```
