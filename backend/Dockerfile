FROM python:3.9

WORKDIR /microblog
COPY requirements.txt backend/
RUN pip install -r backend/requirements.txt

COPY . backend/

CMD uvicorn backend.api.app:create_app --host 0.0.0.0 --port 8000
