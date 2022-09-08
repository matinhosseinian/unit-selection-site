from django.contrib import admin
from .models import Course, Departemant, Section, Time_Slot, Instructor
import nested_admin

class Time_SlotInline(nested_admin.NestedStackedInline):
    model = Time_Slot
    extra = 1

class SectionInline(nested_admin.NestedStackedInline):
    model = Section
    inlines = [Time_SlotInline]
    extra = 1

class CourseAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        SectionInline,
    ]
    list_display = ("name", "dept_name", "credits", "status")
    list_filter = ("dept_name", "credits", "status")
    search_fields = ["name"]

class InstructorAdmin(admin.ModelAdmin):
    list_display = ("name", "dept_name",)
    list_filter = ("dept_name",)
    search_fields = ["name"]



class SectionAdmin(admin.ModelAdmin):
#     inlines = [
#         Time_SlotInline,
#     ]
    list_display = ("course", "group", "instructor", "gender",)
    list_filter = ("course", "instructor", "gender",)
    search_fields = ["course", "instructor",]

class Time_SlotAdmin(admin.ModelAdmin):
    list_display = ("section", "day", "start", "end",)
    list_filter = ("day",)
    search_fields = ["section", "day",]


admin.site.register(Departemant)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Time_Slot, Time_SlotAdmin)