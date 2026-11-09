FROM python:3.12-slim

ENV VIRTUAL_ENV=/opt/venv \
    TZ=Asia/Kolkata
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /srv
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["python", "./app.py"]
