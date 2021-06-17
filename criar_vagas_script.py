import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from vagas.models import Vaga, Requisitos, Desejavel
import random
from django.contrib.auth import get_user_model
User = get_user_model()

cargos = [
'Desenvolvedor PYTHON','Desenvolvedor PHP','Desenvolvedor JAVA',
'Desenvolvedor REACT','Desenvolvedor BACK','Desenvolvedor TESTE']

faixas_salariais = [
'Até 1.000','De 1.000 a 2.000','De 2.000 a 3.000',
'Acima de 3.000']

escolaridades = [
    'Ensino fundamental', 'Ensino médio', 'Tecnólogo', 'Ensino superior',
    'Pós / MBA / Mestrado', 'Doutorado'
]


def criando_vagas(quantidade):
    for _ in range(quantidade):
        user = User.objects.get(id=1)

        cargo = cargos[random.randrange(0, 6)]
        faixa_salarial = faixas_salariais[random.randrange(0, 4)]
        escolaridade = escolaridades[random.randrange(0, 6)]



        vaga = Vaga.objects.create(cargo=cargo, faixa_salarial=faixa_salarial, escolaridade=escolaridade,
                                   descricao='Vaga criado com o objetivo de realizar testes',
                                   empresa=user)
        vaga.save()

        print(vaga)

        contador = 0

        while contador < 5:
            requisito = Requisitos.objects.create(vaga=vaga, requisito='Teste')
            requisito.save()
            contador = contador + 1
            print(contador)

        contador = 0

        while contador < 5:
            desejavel = Desejavel.objects.create(vaga=vaga, desejavel='Teste')
            desejavel.save()
            contador = contador + 1


criando_vagas(30)
print("sucesso")