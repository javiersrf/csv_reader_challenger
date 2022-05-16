import pandas as pd
from django.core.files.uploadedfile import InMemoryUploadedFile
import datetime
from typing import List
import pandas as pd
import pandas as pd
from io import BytesIO, StringIO
import itertools
from ..models import Operation, ProviderSell, RegisterSell

def normalize_data(file:BytesIO):
    file.seek(0)
    encoding = 'utf-8'
    file = str(file.read(),encoding)    
    file = file.replace('\t',',')
    dt = pd.read_csv(StringIO(file))    
    dt["Custo total"] = dt["Preço Unitário"]* dt["Quantidade"]
    counts:List[dict] = []

    for x in dt.iloc:
        cnt = len([y for y in dt.iloc if y["Fornecedor"] == x["Fornecedor"]])
        total = sum([y["Custo total"] for y in dt.iloc if y["Fornecedor"] == x["Fornecedor"]])
        if x["Fornecedor"] not in list(itertools.chain.from_iterable([list(z.keys()) for z in counts])):
            counts.append(
                {   "provider":x["Fornecedor"],
                    "orders":cnt,
                    "total":total
                }
            )

    return  {
        "total":dt.sum()["Custo total"],
        "quantity":dt.sum()["Quantidade"],
        "providers": counts,
        "registers": [{
            "buyer":x["Comprador"],
            "quantity":x["Quantidade"],
            "total":x["Custo total"]
        } for x in dt.iloc]
    }


def send_to_database(data:dict, file_name:str):
    providers_list = data["providers"]
    registers_list = data["registers"]
    operation_data = {
        "total":data["total"],
        "quantity":data["quantity"],
        "date":datetime.datetime.now()
    }
    new_operation = Operation(
        quantity = operation_data["quantity"],
        total = operation_data["total"],
        name = file_name,
    )
    new_operation.save()
    last_insert = Operation.objects.last()
    for x in providers_list:
        new_provider = ProviderSell(
            provider = x["provider"],            
            quantity = x["orders"],
            total =x["total"],
            operation = last_insert
        )
        new_provider.save()
    for x in registers_list:
        new_register = RegisterSell(
            buyer = x["buyer"],
            quantity = x["quantity"],
            total =x["total"],
            operation = last_insert
        )
        new_register.save()

    
def read_csv(file:InMemoryUploadedFile, file_name:str):
    file.seek(0)
    data = normalize_data(file.file)
    data["name"] = file.name
    send_to_database(data, file_name)