from django.urls import path
from . import views

urlpatterns = [
    path('notes/',views.globaleNotesList,name="globaleNotesList"),
    path('note/<int:note_id>/',views.globaleNotesDetails,name="globaleNotesDetails"),
    path('student/<str:student_id>/',views.studentGlobaleNote,name="studentGlobaleNote"),
]
