FROM python:3.10-slim
RUN pip install flask --no-cache-dir --progress-bar off
COPY ./static /home/myapp/static/
COPY ./templates /home/myapp/templates/
COPY sample_app.py /home/myapp/
EXPOSE 5050
CMD python3 /home/myapp/sample_app.py
