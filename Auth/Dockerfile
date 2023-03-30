FROM python:latest

COPY . .

#install connexion
RUN pip install connexion

#install yaml
RUN pip install pyyaml
CMD [ "python", "./app.py" ]