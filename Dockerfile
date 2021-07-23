
FROM python:3.8-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONFAULTHANDLER=1
ENV PYTHONBUFFERED=1
WORKDIR /app
COPY Pipfile /app/
COPY Pipfile.lock /app/
RUN pip install pipenv
RUN pipenv install 
COPY . ./
EXPOSE 8000
