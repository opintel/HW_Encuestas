# EncuestasDGM
Herramienta para generar encuestas en datos.gob.mx. La herramienta esta construida en Django 1.9.7 y diseñada para correr en ambientes con sistema operativo Linux.

*Nota. Los comandos para la instalación corren sobre Ubuntu 15.10.*

# Instalación Local

### Requerimientos Locales
- [Python 2.7](https://www.python.org/download/releases/2.7/)
- [Virtualenv](https://virtualenv.pypa.io/en/stable/)
- [Postgres 9.4](https://www.postgresql.org/download/linux/ubuntu/)
- [MongoDB 3.2](https://www.mongodb.com/mongodb-3.2)

### Instalación
Los siguientes pasos asumen que se han instalado los requerimientos señalados anteriormente. Correr los siguientes comandos:
```shell
  git clone git@github.com:opintel/HW_Encuestas.git
  virtualenv {{TU_VIRTUALENV}}
  . {{TU_VIRTUALENV}}/bin/activate
  pip install -r HW_Encuestas/requirements.txt
```

### Uso
Para poder ver la herramienta corra el siguiente comando:
```
   python HW_Encuestas/EncuestasDGM/manage.py runserver
```
Despues en la barra del navegador:
```
http://127.0.0.1:8000/encuestas/
```

# Instalación Docker
### Instalación
Para los siguientes pasos se require tener instalada la plataforma [Docker](https://www.docker.com/products/overview) en el servidor aplicativo.

En el servidor aplicativo construimos la imagen del contenedor:
```
  git clone git@github.com:opintel/HW_Encuestas.git
  docker build -t encuestas HW_Encuestas/Docker/.
```
### Uso
Una vez construida la imagen Docker de la herramienta, ya es posible generar el contenedor donde estara ejecutandose la herramienta. Un punto a considerar antes de avanzar con la creación del contenedor es que hace uso de la tecnologia **MongoDB** como motor de base de datos NO RELACIONAL, donde se almacenan los datos relacionados con las encuestas, por lo que se necesita crear un contenedor Docker con **MongoDB** y conectarlo al contenedor aplicativo.

Otro punto importante de la aplicación es el uso de **PostgreSQL** como base de datos RELACIONAL, donde guarda la información de los usuarios administradores de la herramienta. Debido a esto es necesario crear ademas un contenedor Docker con **PostgreSQL** y ligarlo al contenedir aplicativo.

Los comandos de consola para correr la aplicacion con toda la arquitectura necesaria son los siguientes:
```
  docker run --name postgres-encuesta -e POSTGRES_PASSWORD={{securepass}} -e POSTGRES_USER={{db_user}} -e POSTGRES_DB={{db}} -p 5433:5432 -d postgres
  docker run --name mongo-encuestas -p 27017:27017 -d mongo
  docker run --name encuestas \
        -e POSTGRES_HOST="{{host}}" \
        -e POSTGRES_PORT="{{port}}" \
        -e MONGO_DB="{{mongo_db}}" \
        --link postgres-encuesta:postgresencuesta \
        --link mongo-encuestas:mongoencuestas \
        -p 8001:8001 \
        -d encuestas

```

Despues en la barra del navegador:
```
http://tudominio.com/encuestas/
```

