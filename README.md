# get-full-address-microservice
Microsserviço para consultar endereços a partir do CEP desenvolvida em Flask.

## Route

```https://get-full-address-microservice.herokuapp.com/api/get-full-address/<CEP>```
  - Requisição: GET

Route chamada pelo serviço para a consulta de detalhes do endereço passando como argumento de URL o cep desejado.

Exemplo de requisição

`/api/get-full-address/09781250`
- Resposta: (content-type application/json)
```
{
    "address": "Rua Papa Paulo VI (Jd Yrajá)",
    "city": "São Bernardo do Campo",
    "neighborhood": "Santa Terezinha",
    "postal_code": "09781250",
    "state": "SP"
}
```

## Iniciando app local

O app é escrito em python3 e configurado para ambiente virtual:
```
virtualenv venv -p python3
. venv/bin/activate
pip install -r requirements.txt
```

Uma vez dentro da venv, basta iniciar a aplicação, ela estará disponível na porta 5000:
```
python main.py
```


## Scripts

A versão do repositório utiliza um banco de dados sqlite já alimentado com dados de endereços disponibilizados pelos correios `ceps_raw.txt`, o script abaixo foi usado para a inicialização do banco de dados e pode ser utilizado para qualquer banco relacional suportado pela biblioteca SQLAlchemy para python. 
```python script_seed_db.py```

Por questões de simplicidade na demonstração, o app feito no deploy está com a opção de autorização por token desabilitada, porém o app está estruturado para isso, para habilitar a função apenas desmarcamos o decorator na route da api em `get-full-address-microservice/app/views/api.py` na linha 12:
``` 
@jwt_required
```
Para gerar um novo token, colocamos a secret_key como variável de ambiente e rodamos um script para criação de um novo token:
```
export JWT_SECRET_KEY = "DA879DN8ADA8DNA8AS78DNAYND8ASYD87A"
python script_generate_token.py
```
