FROM python

FROM tensorflow/tensorflow

COPY requirements.txt .

RUN pip install google-cloud-storage

RUN pip install pandas

RUN pip install -r requirements.txt

COPY gcs.py /app/gcs.py
