# base image
FROM python:latest
# working directory that docker will use for files
WORKDIR /app
# copy everything from the current directory to the WORKDIR
COPY . .
# run this command when we run docker <image name>
CMD python3 /app/paskahousu.py
