#instruction video: https://www.youtube.com/watch?v=DrjIexCTF70

from datetime import datetime, timedelta
#from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
from azure.storage.filedatalake import FileSystemClient, generate_file_sas, FileSasPermissions
import pandas as pd

#enter credentials | get them from azure portal > storage accounts > Security+Networking>Access Keys
account_name = 'sagefruitstorage'
account_key = 'g7rqwrNjeOlr/kHEAEUrbN2NlI806gFpYL5zqVYT8oPAmvk81JNYJiiUe6CKaRi5bx+pucVVs1Cg7oixfbdMqg=='
directory_name = 'Historical_Sales'
#testing 123


#create a client to interact with blob storage
connect_str = 'DefaultEndpointsProtocol=https;AccountName=' + account_name + ';AccountKey=' + account_key + ';EndpointSuffix=core.windows.net'
file_service_client = FileSystemClient.from_connection_string(connect_str)

#use the client to connect to the container
container_client = file_service_client.get_directory_client(directory_name)

#get a list of all blob files in the container
blob_list = []
for blob in container_client.list_directories(name_starts_with='Sage_Weekly_Sales.csv'):#this only works if the file is in the main directory. not a subdirectly folder.
    print("\t" + blob.name)

