FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install Flask
RUN pip install scikit-learn
ENV FLASK_APP=app.py
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]