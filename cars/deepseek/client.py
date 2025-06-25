import os
from openai import OpenAI
from dotenv import load_dotenv
from django.core.exceptions import ValidationError
from django.core.cache import cache

load_dotenv()

class DeepSeekClient:
    def __init__(self):
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY"),
        )
    
    def generate_car_description(self, brand: str, model: str, year: str, max_tokens: int = 250) -> str:
        """
        Gera descrição de veículo usando a API DeepSeek via OpenRouter
        
        Args:
            brand: Marca do veículo
            model: Modelo do veículo
            year: Ano do veículo
            max_tokens: Tamanho máximo da resposta
            
        Returns:
            str: Descrição formatada
            
        Raises:
            ValidationError: Se ocorrer erro na API
        """
        cache_key = f"deepseek_car_desc_{brand}_{model}_{year}_{max_tokens}"
        
        if cached := cache.get(cache_key):
            return cached
            
        try:
            prompt = self._build_prompt(brand, model, year)
            
            response = self.client.chat.completions.create(
                model="deepseek/deepseek-chat",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=0.7,
                timeout=10,
                headers={
                    "HTTP-Referer": os.getenv("SITE_URL", "https://github.com/seu-usuario/seu-projeto"),
                    "X-Title": os.getenv("APP_NAME", "Meu Projeto Django"),
                }
            )
            
            description = response.choices[0].message.content.strip()
            cache.set(cache_key, description, timeout=60*60*24)  # Cache por 24h
            return description
            
        except Exception as e:
            raise ValidationError(f"Falha ao gerar descrição: {str(e)}")
    
    def _build_prompt(self, brand: str, model: str, year: str) -> str:
        """Constroi o prompt para a API"""
        return f"""
        Gere uma descrição de venda atraente para o {brand} {model} {year}.
        A descrição deve incluir:
        - Principais características técnicas
        - Itens de conforto e segurança
        - Vantagens competitivas
        - Linguagem persuasiva para venda
        Seja conciso e direto ao ponto.
        """

# Instância singleton para uso no projeto
client = DeepSeekClient()