from django.contrib import admin
from django.contrib.auth.models import Group
from modeltranslation.admin import TranslationAdmin

from .models import (
    Program,
    Course,
    CourseAllocation,
    Upload,
    UploadVideo,
    TrainingCalendar,
    Certificate,
    FeedbackQuestion,
    FeedbackResponse,
    Testimonial,
)


class ProgramAdmin(TranslationAdmin):
    pass


class CourseAdmin(TranslationAdmin):
    pass


class UploadAdmin(TranslationAdmin):
    pass


admin.site.register(Program, ProgramAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseAllocation)
admin.site.register(Upload, UploadAdmin)

admin.site.register(UploadVideo)
admin.site.register(TrainingCalendar)
admin.site.register(Certificate)
admin.site.register(Testimonial)
admin.site.register(FeedbackQuestion)
admin.site.register(FeedbackResponse)