from django.db import models
import re
from django.core.validators import RegexValidator

arabic_regex = re.compile(r"^[\u0600-\u06FF\s]+$") # Regular expression to match Arabic characters

validate_arabic = RegexValidator(
    arabic_regex, "Please enter text in Arabic", "invalid" # Error message to display if the input is not in Arabic
)

class arabic_input(models.Model):

    arabic_text = models.CharField(max_length=1000,validators=[validate_arabic])
    prediction = models.CharField(max_length=20,blank=True)

    def __str__(self):
        return self.arabic_text
