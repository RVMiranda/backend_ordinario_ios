from django.contrib import admin
from .models import Tarea, Materia, Institution

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'materia', 'institucion', 'estado')
    search_fields = ('titulo', 'materia__nombre', 'institucion__nombre')
    list_filter = ('institucion', 'estado')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "materia":
            # Filtrar las materias por la institución seleccionada
            if 'institucion' in request.GET:
                institution_id = request.GET.get('institucion')
                kwargs['queryset'] = Materia.objects.filter(institucion__id=institution_id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

#admin.site.register(Tarea, TareaAdmin)