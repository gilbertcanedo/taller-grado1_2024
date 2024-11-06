from django.contrib import admin
from .models import (
    Genero, GrupoSanguineo, Paciente, UnidadTratamiento,
    Medico, MedicoTratante, TipoHemocomponente,
    SolicitudTransfusion, Hemocomponente, ReaccionTransfusional
)

# Registrar modelos básicos sin personalización
admin.site.register(Genero)
admin.site.register(GrupoSanguineo)
admin.site.register(UnidadTratamiento)
admin.site.register(Medico)
admin.site.register(MedicoTratante)
admin.site.register(TipoHemocomponente)
admin.site.register(Hemocomponente)
admin.site.register(ReaccionTransfusional)

# Personalización del modelo Paciente
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido_paterno', 'apellido_materno', 'edad', 'seguro', 'grupo_sanguineo')
    search_fields = ('nombre', 'apellido_paterno', 'apellido_materno')
    list_filter = ('genero', 'grupo_sanguineo')

# Registrar el modelo Paciente con personalización
admin.site.register(Paciente, PacienteAdmin)

# Personalización del modelo SolicitudTransfusion
class SolicitudTransfusionAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'paciente', 'unidad_tratamiento', 'urgencia', 'medico', 'medico_tratante')
    list_filter = ('urgencia', 'unidad_tratamiento')
    search_fields = ('paciente__nombre', 'diagnostico')

# Registrar el modelo SolicitudTransfusion con personalización
admin.site.register(SolicitudTransfusion, SolicitudTransfusionAdmin)

