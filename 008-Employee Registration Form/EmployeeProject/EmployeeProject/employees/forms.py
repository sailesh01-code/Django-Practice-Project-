from django import forms



# class EmployeeForm(forms.Form):
#     name = forms.CharField()
#     department = forms.CharField()
#     salary = forms.IntegerField()
#     email = forms.EmailField()


class DepartmentChoiceField(forms.ChoiceField):
    def valid_value(self, value):
        return any(
            str(value).lower() == str(key).lower()
            for key, _ in self.choices
        )


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    widget = MultipleFileInput

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if not data:
            return []
        if isinstance(data, (list, tuple)):
            return [single_file_clean(file_data, initial) for file_data in data]
        return [single_file_clean(data, initial)]


class EmployeeForm(forms.Form):
    employee_code = forms.RegexField(regex=r'^EMP[0-9]{3}$')
    name = forms.CharField(
        label='Employee Name',
        min_length=3,
        max_length=50,
        widget=forms.TextInput(
            attrs={'class': 'input-box', 'placeholder': 'Enter employee name'}
        ),
    )
    department = DepartmentChoiceField(
        label='Department Name',
        choices=[
            ('development', 'Development'),
            ('testing', 'Testing'),
            ('hr', 'HR'),
            ('finance', 'Finance'),
        ],
    )

    def clean_department(self):
        return self.cleaned_data['department'].lower()

    salary = forms.IntegerField(
        label='Monthly Salary',
        help_text='Enter monthly salary in rupees',
    )
    email = forms.EmailField(label='Email Address', required=False)
    password = forms.CharField(widget=forms.PasswordInput)
    joining_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    joining_datetime = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    joining_time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'})
    )
    address = forms.CharField(
        max_length=200,
        widget=forms.Textarea(
            attrs={'rows': 4, 'cols': 40, 'placeholder': 'Enter employee address'}
        ),
    )
    employment_type = forms.ChoiceField(
        choices=[
            ('full', 'Full Time'),
            ('part', 'Part Time'),
            ('intern', 'Internship'),
        ],
        widget=forms.RadioSelect,
    )
    skills = forms.MultipleChoiceField(
        choices=[
            ('python', 'Python'),
            ('django', 'Django'),
            ('sql', 'SQL'),
            ('javascript', 'JavaScript'),
        ],
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )
    currently_working = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput,
    )
    website = forms.URLField()
    project_slug = forms.SlugField(max_length=50)
    bonus = forms.DecimalField(max_digits=10, decimal_places=2)
    performance_score = forms.FloatField()
    resume = MultipleFileField(required=False)

    def clean_resume(self):
        resumes = self.cleaned_data['resume']
        allowed_extensions = ('.pdf', '.doc', '.docx')
        for resume in resumes:
            if not resume.name.lower().endswith(allowed_extensions):
                raise forms.ValidationError(
                    'Only PDF, DOC and DOCX files are allowed'
                )
        return resumes
    
