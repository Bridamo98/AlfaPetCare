from django.db import models

# Create your models here.

class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 200, blank = False, null = False)
    apellidos = models.CharField(max_length = 100 , blank = False, null = False)
    nacionalidad = models.CharField(max_length = 100 , blank = False, null = False)
    descripcion = models.TextField(blank = False, null = False)

    def __str__(self): #To string
        return self.nombre
    #end def

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']
    #end class
#end Class

class Libro(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField(max_length = 200, blank = False, null = False)
    fecha_publicacion = models.DateField('Fecha publicacion', blank = False, null = False)
    autor_id = models.ForeignKey(Autor, on_delete = models.CASCADE)#OneToOneField|ManyToManyField

    def __str__(self):
        return self.titulo
    #end def

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
    #end class
#end class
