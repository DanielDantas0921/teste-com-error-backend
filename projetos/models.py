from django.db import models

class Projeto(models.Model):
    nome_projeto = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_inicio = models.DateField()
    data_termino = models.DateField(blank=True, null=True)
    # prazo = models.DateField()
    numero_emenda = models.CharField(max_length=50, blank=True, null=True)
    financiador = models.CharField(max_length=255)
    conta_bancaria = models.CharField(max_length=50)
    termo_fomento = models.TextField(blank=True, null=True)
    detalhamento = models.CharField(max_length=255)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Tipo(models.TextChoices):
        CUSTEIO = "Custeio", "Custeio"
        INVESTIMENTO = "Investimento", "Investimento"
        AQUISICAO_EQUIPAMENTO = "Aquisição de equipamento", "Aquisição de equipamento"
        OUTROS = "Outros", "Outros"
    class Status (models.TextChoices):
        EM_EXECUCAO = "Em execução",
        EM_PROSPECAO = "Em prospecção",
        CONCLUIDO = "Concluído",
        
    tipo = models.CharField(max_length=50, choices=Tipo.choices)
    status = models.CharField(max_length=50, choices=Status.choices)
    
    
    def __str__(self):
        return self.nome_projeto


        
class ProjetoTeste(models.Model):
    nome_projeto = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.nome_projeto

