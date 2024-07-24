from student.models import StudentPayment
from django import forms


class StudentPaymentForm(forms.ModelForm):
    class Meta:
        model = StudentPayment
        fields = ['student_id','technology_id','total_fees','remaining_fees','paid_fees','status']