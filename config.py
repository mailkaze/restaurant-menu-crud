#ENV = 'PROD'
ENV = 'DEV'
if ENV == 'DEV':
    #formato: postgres+psycopg2://<NOMBRE_USUARIO>:<CONTRASEÑA>@<DIRECCIÓN_IP>:<PUERTO>/<NOMBRE_BASE_DE_DATOS>
    DATABASE_URI = 'postgres+psycopg2://postgres:020584@localhost:5432/restaurante'
elif ENV == 'PROD':
    DATABASE_URI = 'postgres://gfzcwugijretzl:0824327e90b0734b5f56b36c2071e1262a93b5605ce1e05d7412dabb44406d24@ec2-54-243-239-199.compute-1.amazonaws.com:5432/d9cpl25vaho7op'