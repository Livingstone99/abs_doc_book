from django.contrib import admin
from .models import User, Hospital, Specialist, Doctor, Appointment, Payment, SpecialistType, Company, Wallet

# Register your models here.

#admin.site.register(User)
#admin.site.register(Hospital)
#admin.site.register(Specialist)


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','date_of_birth','gender')
    search_fields = ('first_name',)
    list_filter = ('date_of_birth',)
    list_display_links = ('first_name', 'last_name','date_of_birth',)
    #list_editable = ('date_of_birth', 'first_name','last_name',)
admin.site.register(User, UserAdmin)

class SpecialistAdmin(admin.ModelAdmin):
    list_display = ('user','description')
    #list_filter = ('hospital',)
admin.site.register(Specialist,SpecialistAdmin)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'description','hospital_name')
    #list_filter = ('hospital_name',)
    search_fields = ('user',)
    #list_editable = ('hospital_name',)

    def hospital_name(self, obj):
        return obj.hospital.hospital_name

admin.site.register(Doctor, DoctorAdmin)

class HospitalAdmin(admin.ModelAdmin):
    list_display = ('hospital_name','Address')
    list_filter = ('hospital_name',)
    search_fields = ('hospital_name',)
    list_editable = ('Address',)
admin.site.register(Hospital, HospitalAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('venue','user_name', 'user_doctor','user_specialist','start_time','end_time')
    list_editable = ('start_time','end_time','user_specialist',)
    list_filter = ('venue','start_time','end_time',)
    search_fields = ('venue',)

    #def user_req(self, obj):s
    #    return obj.user.user_type

admin.site.register(Appointment,AppointmentAdmin )

class PaymmentAdmin(admin.ModelAdmin):
    list_display =  ('Account_name','Account_type','Account_number',)
    list_display_links = ('Account_name',)
    list_editable = ('Account_number',)
    search_fields = ('Account_name',)
admin.site.register(Payment, PaymmentAdmin)

class SpecialistTypeAdmin(admin.ModelAdmin):
    list_display = ('specialist_type','specialist_category')
    #list_editable = ('specialist_type',)
admin.site.register(SpecialistType, SpecialistTypeAdmin) 

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name',)
admin.site.register(Company, CompanyAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display = ('balance','user_name')
    

    def user_name(self, obj):
        return obj.user.username

admin.site.register(Wallet, WalletAdmin)