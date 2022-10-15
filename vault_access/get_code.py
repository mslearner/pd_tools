from os import environ as env
from azure.keyvault.secrets import SecretClient
from azure.identity import ClientSecretCredential

TENANT_ID = env.get("AZURE_TENANT_ID", "")
CLIENT_ID = env.get("AZURE_CLIENT_ID", "")
CLIENT_SECRET = env.get("AZURE_CLIENT_SECRET", "")
KEYVAULT_NAME = env.get("AZURE_KEYVAULT_NAME", " ")
keyVaultName = "silvervault"
KEYVAULT_URI = f"https://{keyVaultName}.vault.azure.net"


_credential = ClientSecretCredential(
    tenant_id=TENANT_ID, client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
_sc = SecretClient(vault_url=KEYVAULT_URI, credential=_credential)
print(
    f"Retrieving your secret from {keyVaultName}."+_sc.get_secret("mysecret").value)


print(" done.")
