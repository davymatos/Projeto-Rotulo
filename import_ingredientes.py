import csv
from app.models import Ingredientes

def csv_to_list(filename: str) -> list:
    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        csv_data = [line for line in reader]
    return csv_data

def save_data(data):
    aux = []
    for item in data:
        nome_en = str(item.get('nome_en'))
        nome_alt = str(item.get('nome_alt'))
        nome_br = str(item.get('nome_br'))
        origem = str(item.get('origem'))
        funcao_principal = str(item.get('funcao_principal'))
        referencia = str(item.get('referencia'))
        obj = Ingredientes(
            nome_en=nome_en,
            nome_alt=nome_alt,
            nome_br=nome_br,
            origem=origem,
            funcao_principal=funcao_principal,
            referencia=referencia,
        )
        aux.append(obj)
    Ingredientes.objects.bulk_create(aux)

data = csv_to_list('fix/saneantes.csv')
save_data(data)