# MS_Microservices

Ich habe einen kleinen Microservices geschrieben mit dem man Gerichte abfragen und speichern kann. 
Der Services kann wie nachfolgend über Docker zum laufen gebracht werden. 

Des weiteren habe ich eine Abfrage plus Visualisierung mit Postman an die Api gemacht, wie im Screenshot zu sehen ist. 
Die Abfrage kann auch dem JSON Export aus dem Repo entnommen werden. 

# Microservices mit Docker starten

```bash
# Repo klonen
cd MS_Microservices/M1
docker build -t ms_image .
docker run -d --name ms_dishes -p 80:80 ms_image
```
Aufruf der Seite http://127.0.0.1:80/docs#/

