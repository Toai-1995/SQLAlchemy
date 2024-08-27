FROM python:3.9
RUN apt-get update

RUN python -m pip install -i https://pypi.org/simple --upgrade pip
COPY requirements.txt .
RUN pip install -i https://pypi.org/simple -r requirements.txt
CMD ["fastapi", "run", "main.py", "--port", "80"]
