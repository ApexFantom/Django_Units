class FormFromSomeModel(forms.ModelForm):
    class Meta:
        model = SomeModel
        widgets = {
            'foo': SummernoteWidget(),
            'bar': SummernoteInplaceWidget(),
        }