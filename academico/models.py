from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Aluno(models.Model):
    nome = models.CharField(max_length=100, default="")
    matricula = models.CharField(max_length=14, unique=True)
    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=100, default="")
    carga_horaria = models.IntegerField(default=1)
    def __str__(self):
        return self.nome

class Diario(models.Model):
    codigo = models.CharField(max_length=100, default="")
    num_aulas = models.IntegerField(default=0)
    ano = models.IntegerField(default=0)
    semestre = models.IntegerField(default=0)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    def percent_conclusao(self):
        diarios = Diario.objects.filter(disciplina=self.disciplina)
        total_aulas = 0
        for diario in diarios:
            total_aulas += diario.num_aulas
        return total_aulas / self.disciplina.carga_horaria
    def __str__(self):
        return "código: " + self.codigo + ", " + "ano: " + str(self.ano) + ", " + "semestre: " + str(self.semestre) + ", " + "percentual de conclusão: " + str(self.percent_conclusao())

class Rendimento(models.Model):
    nota1 = models.IntegerField(default=0)
    nota2 = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )
    num_faltas = models.IntegerField(default=0)
    diario = models.ForeignKey(Diario, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    def media(self):
        return int((nota1 * 2 + nota2 * 3) / 5)
    def percent_faltas(self):
        
        return 
    def aprovado(self):
        return (self.media() >= 70) and (self.percent_faltas() < 25) 
    def final(self):
        return media < 70
    def __str__(self):
        return str(self.media())


