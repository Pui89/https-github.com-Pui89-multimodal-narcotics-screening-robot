FROM python:3.12-slim

WORKDIR /app
COPY pyproject.toml .
COPY src ./src
COPY evaluation ./evaluation
COPY schemas ./schemas

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -e .

CMD ["python", "-c", "print('Screening platform container ready; no actuator control exposed.')"]
