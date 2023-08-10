from lib.arquivo import *
from lib.interface import *

arq = 'pessoasCadastradas.txt'
if not arquivoexiste(arq):
    criararquivo(arq)

programa_principal()


