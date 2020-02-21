# Dockerfile for Solar Charge Controller backend
FROM python:3
WORKDIR /solar_charge_controller
COPY . ./solar_charge_controller
RUN [ "pip3", "install", "flask" ]

CMD [ "python app.py" ]
