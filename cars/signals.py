from django.db.models.signals import pre_save
from django.dispatch import receiver
from cars.models import Car
from deepseek.client import client as deepseek_client


@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    """
    Gera a descrição automática (bio) com IA antes de salvar o carro,
    apenas se o campo estiver vazio.
    """
    if not instance.bio:
        try:
            instance.bio = deepseek_client.generate_car_description(
                brand=instance.brand.name,
                model=instance.model,
                year=instance.model_year
            )
        except Exception as e:
            instance.bio = f"Descrição indisponível. Erro: {str(e)}"
