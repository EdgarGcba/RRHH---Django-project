# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from tabnanny import verbose
from django.db import models


class Barrio(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50, blank=True, null=True, verbose_name="Nombre")  # Field name made lowercase.
    idciudad = models.ForeignKey('Ciudad', models.DO_NOTHING, db_column='IDciudad', blank=True, null=True)  # Field name made lowercase.
    codigo_postal = models.CharField(db_column='Codigo Postal', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'barrio'


class BusquedaTecnologia(models.Model):
    idbusqueda = models.ForeignKey('Busquedalaboral', models.DO_NOTHING, db_column='IDbusqueda')  # Field name made lowercase.
    idtecnologia = models.ForeignKey('Tecnologia', models.DO_NOTHING, db_column='IDtecnologia')  # Field name made lowercase.
    idestado = models.ForeignKey('Estado', models.DO_NOTHING, db_column='IDestado', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'busqueda_tecnologia'


class Busquedalaboral(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    idorganizacion = models.ForeignKey('Organizacion', models.DO_NOTHING, db_column='IDorganizacion', blank=True, null=True)  # Field name made lowercase.
    idrol = models.ForeignKey('Rol', models.DO_NOTHING, db_column='IDrol', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField(blank=True, null=True)
    descripcion = models.CharField(db_column='Descripcion', max_length=250, blank=True, null=True)  # Field name made lowercase.
    ididioma = models.ForeignKey('Idioma', models.DO_NOTHING, db_column='IDidioma', blank=True, null=True)  # Field name made lowercase.

    
    class Meta:
        managed = False
        db_table = 'busquedalaboral'


class Ciudad(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idprovincia = models.ForeignKey('Provincia', models.DO_NOTHING, db_column='IDprovincia', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        fila = "ID - " + str(self.id) + " - " + "Nombre: " + self.nombre
        return fila

    class Meta:
        managed = False
        db_table = 'ciudad'


class Documento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=20, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        fila = "ID - " + str(self.id) +" - "+ self.descripcion
        return fila

    class Meta:
        managed = False
        db_table = 'documento'


class Estado(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estado'


class Genero(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=10, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        fila = "ID - " + str(self.id) +" - "+ self.descripcion
        return fila

    class Meta:
        managed = False
        db_table = 'genero'


class Idioma(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=10, blank=True, null=True)  # Field name made lowercase.

    
    def __str__(self):
        fila = "ID - " + str(self.id) +" - "+ self.descripcion
        return fila

    class Meta:
        managed = False
        db_table = 'idioma'


class Organizacion(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    razon_social = models.CharField(db_column='Razon Social', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    idbarrio = models.ForeignKey(Barrio, models.DO_NOTHING, db_column='IDbarrio', blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(max_length=50, blank=True, null=True)
    cuit = models.CharField(db_column='CUIT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=20, blank=True, null=True)  # Field name made lowercase.
    celular = models.CharField(db_column='Celular', max_length=20, blank=True, null=True)  # Field name made lowercase.
    idtipo = models.ForeignKey('Tipoorganizacion', models.DO_NOTHING, db_column='IDtipo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'organizacion'


class Pais(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pais'


class Postulante(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=25)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=25)  # Field name made lowercase.
    iddocumento = models.ForeignKey(Documento, models.DO_NOTHING, db_column='IDdocumento', blank=True, null=True)  # Field name made lowercase.
    numdocumento = models.CharField(db_column='NumDocumento', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fechadenacimiento = models.DateField(db_column='FechaDeNacimiento', blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idbarrio = models.ForeignKey(Barrio, models.DO_NOTHING, db_column='IDbarrio', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=20, blank=True, null=True)
    celular = models.CharField(max_length=20, blank=True, null=True)
    idestado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='IDestado', blank=True, null=True)  # Field name made lowercase.
    idgenero = models.ForeignKey(Genero, models.DO_NOTHING, db_column='IDgenero', blank=True, null=True)  # Field name made lowercase.

    def __str__(self) -> str:
        fila = "ID - " + str(self.id) + " - " + self.nombre + "  " + self.apellido
        return fila
    
    class Meta:
        managed = False
        db_table = 'postulante'


class PostulanteBusqueda(models.Model):
    idpostulante = models.ForeignKey(Postulante, models.DO_NOTHING, db_column='IDpostulante')  # Field name made lowercase.
    idbusqueda = models.ForeignKey(Busquedalaboral, models.DO_NOTHING, db_column='IDbusqueda')  # Field name made lowercase.
    idestado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='IDestado', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'postulante_busqueda'


class PostulanteIdioma(models.Model):
    idpostulante = models.ForeignKey(Postulante, models.DO_NOTHING, db_column='IDpostulante')  # Field name made lowercase.
    ididioma = models.ForeignKey(Idioma, models.DO_NOTHING, db_column='IDidioma')  # Field name made lowercase.
    idestado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='IDestado', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'postulante_idioma'


class PostulanteRol(models.Model):
    idpostulante = models.ForeignKey(Postulante, models.DO_NOTHING, db_column='IDpostulante')  # Field name made lowercase.
    idrol = models.ForeignKey('Rol', models.DO_NOTHING, db_column='IDrol')  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    idestado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='IDestado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'postulante_rol'


class PostulanteTecnologia(models.Model):
    idpostulante = models.ForeignKey(Postulante, models.DO_NOTHING, db_column='IDpostulante')  # Field name made lowercase.
    idtecnologia = models.ForeignKey('Tecnologia', models.DO_NOTHING, db_column='IDtecnologia')  # Field name made lowercase.
    idestado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='IDestado', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'postulante_tecnologia'


class Provincia(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idpais = models.ForeignKey(Pais, models.DO_NOTHING, db_column='IDpais', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'provincia'


class Rol(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rol'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=160)
    principal_id = models.IntegerField()
    diagram_id = models.IntegerField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class Tecnologia(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tecnologia'

    def __str__(self):
        fila = "ID - " + str(self.id) +" - "+ self.descripcion
        return fila


class Tipoorganizacion(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipoorganizacion'