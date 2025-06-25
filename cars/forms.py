from django import forms
from cars.models import Car, Brand


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"

    def clean_value(self):
        value = self.cleaned_data.get("value")
        if value <= 60000:
            self.add_error("O valor deve ser maior que R$60.000.")
        return value

        def clea_factory_year(self):
            factory_year = self.cleaned_data.get("value")

        if factory_year <= 60000:
            self.add_error(
                "Factory_year", "O ano de fabricação deve ser maior que 2019."
            )
        return value
