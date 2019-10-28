#ENV = 'PROD'
ENV = 'DEV'
if ENV == 'DEV':
    #formato: postgres+psycopg2://<NOMBRE_USUARIO>:<CONTRASEÑA>@<DIRECCIÓN_IP>:<PUERTO>/<NOMBRE_BASE_DE_DATOS>
    DATABASE_URI = 'postgres+psycopg2://postgres:020584@localhost:5432/restaurante'
elif ENV == 'PROD':
    DATABASE_URI = '?'