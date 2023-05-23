FROM python:3.8-slim-buster

WORKDIR /home/app/

COPY requirements.txt /home/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY requirements-dev.txt /home/app/
RUN pip install --no-cache-dir -r requirements-dev.txt

COPY ./ /home/app/

ENV PYTHONPATH=${PYTHONPATH}:/home/app/
ENV FLASK_ENV=production

CMD ["gunicorn", "main:app", "-b", "0.0.0.0:5000"]

