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

ctx = snow.connect(
    user='bijay_first',
    account='uzvqfza-js07323',
    private_key=pkb,
    #warehouse=WAREHOUSE,
    database='HOME_DB',
    #schema='students'
    )

cs = ctx.cursor()
cs.status()
#cs.execute("USE DATABASE HOME_DB;")
#cs.execute("CREATE TABLE courses(course_id INT PRIMARY KEY, course_name VARCHAR(20) NOT NULL, course_fee INT NOT NULL);")