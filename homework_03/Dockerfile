FROM python:3.9-buster

ENV PYTHONUNBUFFERED=1

# dir for our app
WORKDIR /app

# install dependencies
COPY webproject/requirements.txt .
RUN pip install -r requirements.txt

# copy folder  with project
COPY webproject .

# run uvicron after run docker
CMD ["uvicorn", "app:app", "--host=0.0.0.0", "--port=8000"]