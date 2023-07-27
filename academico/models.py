from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Aluno(models.Model):
    nome = models.CharField(max_length=100, default="")
    matricula = models.CharField(max_length=14, unique=True)
    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=100, default="")
    carga_horaria = models.IntegerField(default=0)
    def __str__(self):
        return self.nome

class Diario(models.Model):
    codigo = models.CharField(max_length=100, default="")
    num_aulas = models.IntegerField(default=0)
    ano = models.IntegerField(default=0)
    semestre = models.IntegerField(default=0)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    def percent_conclusao():
        return 0.0
    def __str__(self):
        return self.codigo + "." + str(self.ano) + "." + str(semestre)

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
    def media():
        return int((nota1 * 2 + nota2 * 3) / 5)
    def percent_faltas():
        return 
    def aprovado():
        return (self.media() >= 70 and self.percent_faltas() < 25) 
    def __str__(self):
        return str(self.media())


