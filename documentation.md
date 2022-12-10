Snowflake supports using key pair authentication for enhanced authentication security as an alternative to basic authentication (i.e. username and password).

This authentication method requires, as a minimum, a 2048-bit RSA key pair. You can generate the Privacy Enhanced Mail (i.e. PEM) private-public key pair using OpenSSL. Some of the Supported Snowflake Clients allow using encrypted private keys to connect and authenticate to Snowflake. 

Snowflake also supports rotating public keys in an effort to allow compliance with more robust security and governance postures. [Source](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)

To generate and encrypted version, use the following
$ openssl genrsa 2048 | openssl pkcs8 -topk8 -v2 des3 -inform PEM -out rsa_key.p8

From the terminal, generate the public key by referencing the private key. The following cmd assumes the private key is encrypted and contained in the file named `rsa_key.p8`
$ openssl rsa -in rsa_key.p8 -pubout -out rsa_key.pub

#PRoblem
$ pip install --upgrade pyopenssl==22.0.0 to solve snowflake import error

# USE SYSADMIN ROLE TO NEW USER BIJAY_FIRST FOR CREATING DATABASES AND WAREHOUSES. 
# WARNING: DONOT GIVE USERADMIN ROLE TO NEW USER BIJAY_FIRST.