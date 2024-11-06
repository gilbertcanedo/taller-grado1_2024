from django.db import models

# Create your models here.

# Modelo para Género
class Genero(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

# Modelo para Grupo Sanguíneo
class GrupoSanguineo(models.Model):
    tipo_sangre = models.CharField(max_length=2)  # e.g., 'A', 'B', 'O', 'AB'
    factor_rh = models.CharField(max_length=10)  # e.g., 'Positivo', 'Negativo'

    def __str__(self):
        return f"{self.tipo_sangre} {self.factor_rh}"

# Modelo para Paciente
class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    edad = models.IntegerField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    seguro = models.CharField(max_length=50)
    grupo_sanguineo = models.ForeignKey(GrupoSanguineo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno}"

# Modelo para Unidad de Tratamiento
class UnidadTratamiento(models.Model):
    nombre_unidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_unidad

# Modelo para Medico
class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    registro_medico = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} - {self.especialidad}"

# Modelo para Médico Tratante
class MedicoTratante(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    registro_medico = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} - {self.especialidad}"

# Modelo para Tipo Hemocomponente
class TipoHemocomponente(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

# Modelo para Solicitud de Transfusión
class SolicitudTransfusion(models.Model):
    fecha = models.DateField()
    unidad_tratamiento = models.ForeignKey(UnidadTratamiento, on_delete=models.CASCADE)
    urgencia = models.IntegerField(choices=[(1, 'Baja'), (2, 'Media'), (3, 'Alta')])
    diagnostico = models.CharField(max_length=200)
    observaciones = models.TextField()
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='medico_autoriza')
    medico_tratante = models.ForeignKey(MedicoTratante, on_delete=models.CASCADE)

    def __str__(self):
        return f"Solicitud {self.id} - Paciente: {self.paciente}"

# Modelo para Hemocomponente
class Hemocomponente(models.Model):
    tipo_hemocomponente = models.ForeignKey(TipoHemocomponente, on_delete=models.CASCADE)
    num_unidades_solicitadas = models.IntegerField()
    solicitud_transfusion = models.ForeignKey(SolicitudTransfusion, on_delete=models.CASCADE, related_name='hemocomponentes')

    def __str__(self):
        return f"{self.tipo_hemocomponente} - {self.num_unidades_solicitadas} unidades"

# Modelo para Reacción Transfusional
class ReaccionTransfusional(models.Model):
    descripcion = models.CharField(max_length=200)
    fecha_reaccion = models.DateField()
    tipo_reaccion = models.CharField(max_length=100)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='reacciones')

    def __str__(self):
        return f"Reacción {self.tipo_reaccion} - Paciente: {self.paciente}"

