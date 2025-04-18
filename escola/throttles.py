#este arquivo configuraremos todas as trottles que serão utilizadas na aplicação.
from rest_framework.throttling import AnonRateThrottle

#Para personalizar para minhas views limitações de acesso por usuários e anônimos, vamos criar uma classe para os AnonRate e sobrescrever o valor de acesso premitido. Na view estuntes então definiremos os acessos personalizados exlusivamente para ela. 
class MatriculaAnonRateThrottle(AnonRateThrottle):
    # Definindo o limite de requisições para 5 requisições por dia
    rate = '5/day'


