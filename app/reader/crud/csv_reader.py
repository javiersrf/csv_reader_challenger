import pandas as pd
from django.core.files.storage import FileSystemStorage
import os
def read_csv(file):
    with open(f'./results/{file.name}.txt', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

