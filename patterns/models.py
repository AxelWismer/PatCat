from django.db import models
import unicodedata

# Common fields
NAME = models.CharField(max_length=50, unique=True, verbose_name="Nombre")
TITLE = models.CharField(max_length=50, unique=True, verbose_name="Titulo")
DESCRIPTION = models.TextField(verbose_name="Descripción")


# Business Processes
class BusinessProcessCategory(models.Model):
    name = NAME
    description = DESCRIPTION

    def __str__(self): return self.name

    class Meta:
        verbose_name = "Categoria de proceso de negocio"
        verbose_name_plural = "Categorias de procesos de negocio"


class BusinessProcess(models.Model):
    name = NAME
    description = DESCRIPTION
    category = models.ForeignKey(
        BusinessProcessCategory, on_delete=models.PROTECT,
        verbose_name="Categoria")

    def __str__(self): return self.name

    class Meta:
        verbose_name = "Proceso de negocio"
        verbose_name_plural = "Procesos de negocio"


# Catalogue
class Catalogue (models.Model):
    title = TITLE
    description = DESCRIPTION
    date = models.DateField(auto_now=True, verbose_name="Fecha de creacion")
    business_process = models.ForeignKey(
        BusinessProcess, on_delete=models.PROTECT, verbose_name="Proceso de negocio")

    def __str__(self): return self.title

    class Meta:
        verbose_name = "Catalogo"
        verbose_name_plural = "Catalogos"


# Patterns
class PatternType(models.Model):
    name = NAME
    def __str__(self): return self.name

    class Meta:
        verbose_name = "Tipo de patrón"
        verbose_name_plural = "Tipos de patrones"
    
    def get_words(self):
        # TODO: Agregar palabras claves 
        return f'{self.name} {self.intent} {self.motivation} {self.applicability} {self.paricipants} {self.consequences} {self.example}'.split()

class Pattern(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    description = DESCRIPTION
    structure = models.TextField(verbose_name="Estructura")
    type = models.ForeignKey(PatternType, on_delete=models.PROTECT, verbose_name="Tipo de Patrón")
    catalogue = models.ForeignKey(Catalogue, on_delete=models.PROTECT, verbose_name="Catálogo")
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
        words = unicodedata.normalize('NFKD', f'{self.name} {self.description} {self.type.name} {self.catalogue.title}'.lower()).encode('ASCII', 'ignore').split()
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
    catalogue = models.ForeignKey(Catalogue, on_delete=models.PROTECT, verbose_name="Catálogo")

    def __str__(self): return self.title

    class Meta:
        verbose_name = "Paper"
        verbose_name_plural = "Papers"

# TODO: add inverted index clases
