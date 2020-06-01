from django.db import models

# Create your models here.
'''
foto max 3	                Obrigatorio minimo 1
nome 	
idade aproximada	        Obrigatorio filhote - adulto-idoso
porte	                    Pequeno-médio-grande
sexo	                    Obrigatorio masculino - feminino - não identificado
vascinas	
especie	                    Obrigatorio felino  canino OU cachorro - gato
caracteristicas unicas	
cor	                        varias minimo 1?
cirurgias	
status	                    Encontrado doação 
raça	
descrição                   historia 	
postado por...	            id da ong ou usuario E qual entidade
como foi acolhido	        Obrigatorio doado - machucado - atropelado - saudavel
local encontrado	        Obrigatorio encontrado(rural / urbano) - endereço
horario acolhido	        Obrigatorio

'''
class Age(models.Model):
    name = models.CharField(max_length=20)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=20)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Sex(models.Model):
    name = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Castrated(models.Model):
    name = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Species(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=20)
    color_palette = models.CharField(max_length=10)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class UserType(models.Model):
    name = models.CharField(max_length=20)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Breed(models.Model):
    name = models.CharField(max_length=20)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Treatments(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    date = models.DateTimeField()
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Disease(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Animal(models.Model):
    image1 = models.CharField(max_length=50, null=False, blank=False)
    image2 = models.CharField(max_length=50)
    image3 = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    age = models.ForeignKey(Age, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE)
    treatments = models.ForeignKey(Treatments, on_delete=models.CASCADE)
    species = models.ForeignKey(Species, on_delete=models.CASCADE, null=False, blank=False, related_name='species')
    unique_characteristics = models.TextField(max_length=500)
    color1 = models.ForeignKey(Color, on_delete=models.CASCADE, null=False, blank=False, related_name='color1')
    color2 = models.ForeignKey(Color, on_delete=models.CASCADE, null=True, related_name='color2')
    color3 = models.ForeignKey(Color, on_delete=models.CASCADE, null=True, related_name='color3')
    castrated = models.ForeignKey(Castrated, on_delete=models.CASCADE, null=False, blank=False)
    surgery = models.TextField(max_length=500)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, null=False, blank=False)
    description = models.TextField(max_length=500)
    posted_by = models.ForeignKey(UserType, on_delete=models.CASCADE)
    how_was_it_welcomed = models.ForeignKey(Species, on_delete=models.CASCADE, related_name='how_was_it_welcomed')
    found_location = models.CharField(max_length=50)
    welcome_date = models.DateTimeField()
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.nome

