FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip

WORKDIR /app
#RUN groupadd -r user_auth_gp && useradd -r -g user_auth_gp user_auth
#RUN chown -hR user_auth:user_auth_gp /app/
#USER user_auth
#RUN whoami

#RUN python -m venv venv
#RUN source ./venv/bin/activate

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

COPY startup.sh .
#CMD ["/bin/bash", "-c", "./startup.sh"]
#CMD ["/bin/bash", "-c", "mv", "env_docker.example", ".env"]
#CMD ["/bin/bash", "-c", "python", "manage.py", "makemigrations"]
#CMD ["/bin/bash", "-c", "python", "manage.py", "migrate"]
