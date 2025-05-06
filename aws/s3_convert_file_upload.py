import os
import boto3
from security.security import Security

# Criação do objeto de segurança
security = Security()

# Obtendo as credenciais AWS do objeto security
AWS_BUCKET_NAME_ID = security.aws_access_key
AWS_SECRET_ACCESS_KEY = security.aws_secret_key
AWS_REGION = security.aws_region
AWS_BUCKET_NAME_CSV = security.aws_bucket_name_csv
AWS_BUCKET_NAME_JSON = security.aws_bucket_name_json
AWS_BUCKET_NAME_PARQUET = security.aws_bucket_name_parquet

class S3BucketCreator:
    def __init__(self, access_key, secret_key, region='us-east-1'):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region
        )

    def create_bucket(self, bucket_name):
        """
        Cria um novo bucket no S3.
        """
        try:
            self.s3_client.create_bucket(Bucket=bucket_name)
            print(f"Bucket '{bucket_name}' criado com sucesso.")
        except Exception as e:
            print(f"Falha ao criar o bucket: {e}")

class FileUploader:
    def __init__(self, access_key, secret_key, region='us-east-1'):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region
        )

    def upload_file(self, file_path, bucket_name, object_name=None):
        """
        Faz o upload de um arquivo para o bucket do S3.
        :param file_path: Caminho do arquivo local a ser enviado
        :param bucket_name: Nome do bucket do S3
        :param object_name: Nome do arquivo no S3 (se não for fornecido, usa o nome do arquivo original)
        """
        if object_name is None:
            object_name = os.path.basename(file_path)

        try:
            self.s3_client.upload_file(file_path, bucket_name, object_name)
            print(f"Arquivo '{file_path}' enviado com sucesso para o bucket '{bucket_name}'.")
        except Exception as e:
            print(f"Falha ao enviar o arquivo '{file_path}' para o S3: {e}")

    def upload_csv(self, file_path):
        """ Faz o upload de um arquivo CSV """
        self.upload_file(file_path, AWS_BUCKET_NAME_CSV)

    def upload_json(self, file_path):
        """ Faz o upload de um arquivo JSON """
        self.upload_file(file_path, AWS_BUCKET_NAME_JSON)

    def upload_parquet(self, file_path):
        """ Faz o upload de um arquivo Parquet """
        self.upload_file(file_path, AWS_BUCKET_NAME_PARQUET)

# === USAGE ===
if __name__ == "__main__":
    # Substitua com suas credenciais AWS
    ACCESS_KEY = AWS_BUCKET_NAME_ID
    SECRET_KEY = AWS_SECRET_ACCESS_KEY

    # Criando o objeto do uploader
    uploader = FileUploader(ACCESS_KEY, SECRET_KEY)

    # Exemplo de upload de um arquivo CSV
    uploader.upload_csv("path/to/your/file.csv")

    # Exemplo de upload de um arquivo JSON
    uploader.upload_json("path/to/your/file.json")

    # Exemplo de upload de um arquivo Parquet
    uploader.upload_parquet("path/to/your/file.parquet")

    # Criando um bucket (se necessário)
    bucket_creator = S3BucketCreator(ACCESS_KEY, SECRET_KEY)
    bucket_creator.create_bucket(AWS_BUCKET_NAME_CSV)
