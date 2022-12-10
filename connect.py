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
    user='bijay_first',
    account='uzvqfza-js07323',
    private_key=pkb,
    warehouse='DEMO',
    database='HOME_DB',
    schema='STUDENTS'
    )

#cs.execute("USE DATABASE home_db;")
#cs.execute("CREATE TABLE courses(course_id INT PRIMARY KEY, course_name VARCHAR(20) NOT NULL, course_fee INT NOT NULL);")

conn.cursor().execute("CREATE DATABASE IF NOT EXISTS testdb_mg")
conn.cursor().execute("USE DATABASE testdb_mg")
conn.cursor().execute("CREATE SCHEMA IF NOT EXISTS testschema_mg")
