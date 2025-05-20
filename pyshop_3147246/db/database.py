from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

#Variable cadena de conexión:
MARIADB_URL='mysql+pymysql://root:admin@localhost:3306/pyshop-3147246'

#Crear el objeto colección de la base de datos 
engine = create_engine(MARIADB_URL) 

#Plantilla base para los modelos 
Base = declarative_base()