import snowflake.connector as snow
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization

with open("./rsa_key.p8", "rb") as key:
    p_key= serialization.load_pem_private_key(
        key.read(),
        password=os.environ['PRIVATE_KEY_PASSPHRASE'].encode(),
        backend=default_backend()
    )

pkb = p_key.private_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption())

conn = snow.connect(
    user='BIJAY_FIRST',
    account='UZVQFZA-JS07323',
    private_key=pkb,
    #warehouse='DEMO',
    database='HOMES_DB',
    schema='COURSES',
    client_session_keep_alive=True
    )

#cs.execute("USE DATABASE home_db;")
#cs.execute("CREATE TABLE courses(course_id INT PRIMARY KEY, course_name VARCHAR(20) NOT NULL, course_fee INT NOT NULL);")
try:
    #conn.cursor().execute("CREATE DATABASE testdb_mg")
    conn.cursor().execute("USE DATABASE homes_db")
    conn.cursor().execute("USE SCHEMA courses")
    conn.cursor().execute("CREATE TABLE dummy(dum_id INT PRIMARY KEY, dum_name VARCHAR(20) NOT NULL)")
finally:
    conn.close()