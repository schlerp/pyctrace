FROM python:alpine

# set workingdir
WORKDIR /app

# set up virtual env
ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# copy relevant files into the image
COPY ./pyctraceapi /app/pyctraceapi
COPY ./requirements.txt /tmp/requirements.txt

# install dependancies
RUN python -m pip install -U pip wheel && python -m pip install -r /tmp/requirements.txt

# run the script
CMD ["python", "-m", "pyctraceapi"]
