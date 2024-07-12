from django.contrib import admin
from .models import Role,Employee,EmployeeProfile,Batch,AssignBatch

# Register your models here.
admin.site.register(Role)
admin.site.register(Employee)
admin.site.register(EmployeeProfile)    
admin.site.register(Batch)
admin.site.register(AssignBatch)

