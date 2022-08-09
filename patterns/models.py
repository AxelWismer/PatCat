from distutils.log import error
from textwrap import indent
from django.db import models
import unicodedata

# Common fields
NAME = models.CharField(max_length=200, unique=True, verbose_name="Nombre")
TITLE = models.CharField(max_length=200, unique=True, verbose_name="Titulo")
DESCRIPTION = models.TextField(verbose_name="Descripción", blank=True)

# Business Processes
class UseCaseCategory(models.Model):
    name = NAME
    description = DESCRIPTION

    def __str__(self): return self.name

    class Meta:
        verbose_name = "Categoria de caso de uso"
        verbose_name_plural = "Categorias de caso de uso"


class UseCase(models.Model):
    name = NAME
    description = DESCRIPTION
    category = models.ForeignKey(UseCaseCategory,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Categoria")

    def __str__(self): return self.name

    class Meta:
        verbose_name = "Caso de uso"
        verbose_name_plural = "Casos de uso"


# Catalogue
class SmartContract (models.Model):
    title = TITLE
    description = DESCRIPTION
    date = models.DateField(auto_now=True, verbose_name="Fecha de creacion")
    business_process = models.ForeignKey(
        UseCase, on_delete=models.PROTECT, verbose_name="Caso de uso")

    def __str__(self): return self.title

    class Meta:
        verbose_name = "Contrato inteligentes"
        verbose_name_plural = "Contratos inteligentes"


# Patterns
class PatternType(models.Model):
    name = NAME
    def __str__(self): return self.name

    class Meta:
        verbose_name = "Tipo de patrón"
        verbose_name_plural = "Tipos de patrones"

    def get_words(self):
        return f'{self.name} {self.intent} {self.motivation} {self.applicability} {self.paricipants} {self.consequences} {self.example}'.split()


def structure_path(instance, filename):
    extension = filename[filename.index(".", len(filename) - 5):]
    return f'structure/{instance.name}-{instance.type.name}{extension}'

class Pattern(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre", null=True, blank=True)
    description = DESCRIPTION
    structure = models.ImageField(upload_to=structure_path, verbose_name="Estructura")
    type = models.ForeignKey(
        PatternType, on_delete=models.PROTECT, verbose_name="Tipo de Patrón")
    catalogue = models.ForeignKey(
        SmartContract, on_delete=models.PROTECT, verbose_name="Catálogo")
    intent = models.TextField(verbose_name="Intención")
    motivation = models.TextField(verbose_name="Motivación")
    applicability = models.TextField(verbose_name="Aplicación")
    paricipants = models.TextField(verbose_name="Participantes")
    consequences = models.TextField(verbose_name="Consequencias")
    example = models.TextField(verbose_name="Ejemplo")
    related_pattens = models.TextField(verbose_name="Patrones relacionados")
    source_credit = models.TextField(verbose_name="Creditos a la fuente")

    def __str__(self): return f'{self.name} ({self.type})'

    class Meta:
        verbose_name = "Patrón"
        verbose_name_plural = "Patrones"
        unique_together = (("name", "type"),)

    def get_words(self):
        words = unicodedata.normalize(
            'NFKD', f'{self.name} {self.description} {self.type.name} {self.catalogue.title}'.lower()).encode('ASCII', 'ignore').split()
        thesaurus = {}
        for word in words:
            thesaurus[word] = thesaurus[word] + 1 if word in thesaurus else 1
        return thesaurus


# Paper
class Paper(models.Model):
    title = TITLE
    date = models.DateField(auto_now=True, verbose_name="Fecha de creacion")
    editor = models.TextField(verbose_name="Editor")
    abstract = models.TextField()
    catalogue = models.ForeignKey(
        SmartContract, on_delete=models.PROTECT, verbose_name="Catálogo")

    def __str__(self): return self.title

    class Meta:
        verbose_name = "Paper"
        verbose_name_plural = "Papers"
