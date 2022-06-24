# ddd-karen-arcoverde
DDD - Backend - Karen Arcoverde

Link: https://silver-motors-karen.herokuapp.com/
***
## Índice

- [Modelo Entidade Relacionamento](#mer)
- [Rotas](#rotas)
- [Exemplos](#exemplos)

***
## MER

![diagrama silver motors novo](https://user-images.githubusercontent.com/59583521/154323914-9eb4e9cf-ee8a-46e8-8bbf-74b820d04d83.png)

### Usuário
|Campo|Tipo|Argumentos|Descrição|
|-----|-----|-----|-----|
|nome|string(30)|nullable(False)|Nome do usuário|
|cpf|string(15)|nullable(False)|cpf do usuário|
|email|string(50)|nullable(False) unique(True)|E-mail do usuário|
|telefone|string(15)|nullable(False)|Telefone do usuário|
|endereco|string(150)|nullable(False)|Endereço do usuário|
|senha_hash|largebinary(128)|nullable(False)|Senha hashed do usuário|
|avatar|string(100)|default(foto_base)|Foto de identificação do usuário relacionado ao digital ocean|
|carrinho|relationship|||
|cupons|relationship|||


### Carros
|Campo|Tipo|Argumentos|Descrição|
|-----|-----|-----|-----|
|cor|String(10)|nullable(False)|cor do carro: vermelho, branco, preto etc.|
|descricao|String(50)|nullable(False)|uma breve descricao sobre o carro, história do carro etc.|
|modelo|String(20)|nullable(False)|por exemplo Fiat Uno, modelo: Uno|
|marca|String(20)|nullable(False)|por exemplo Fiat uno, marca: Fiat|
|ano_fabricacao|string(150)|nullable(False)|ano em que foi fabricado o carro|
|motor|Integer|nullable(False)|motor 1.0, 2.0 etc.|
|estoque|Integer|quantidade de um determinado carro que tem em estoque|
|preco|Integer|nullable(False)|preço do carro|
|nacional|Boolean|nullable(False)|se o carro é nacional (true) ou não (false)|
|importada|Boolean|nullable(False)|se o carro é importado (true) ou não (false)|
|carros_carrinho|relationship|||

### Motos
|Campo|Tipo|Argumentos|Descrição|
|-----|-----|-----|-----|
|cor|String(10)|nullable(False)|cor da moto: vermelho, branco, preto etc.|
|descricao|String(50)|nullable(False)|uma breve descricao sobre a moto, história da moto etc.|
|modelo|String(20)|nullable(False)|por exemplo Fiat Uno, modelo: Uno|
|marca|String(20)|nullable(False)|por exemplo Fiat uno, marca: Fiat|
|ano_fabricacao|string(150)|nullable(False)|ano em que foi fabricado a moto|
|motor|Integer|nullable(False)|motor 1.0, 2.0 etc.|
|estoque|Integer|quantidade de um determinada moto que tem em estoque|
|preco|Integer|nullable(False)|preço da moto|
|nacional|Boolean|nullable(False)|se a moto é nacional (true) ou não (false)|
|importada|Boolean|nullable(False)|se a moto é importada (true) ou não (false)|
|motos_carrinho|relationship|||

### Carrinho
|Campo|Tipo|Argumentos|Descrição|
|-----|-----|-----|-----|
|forma_pagamento|String(40)|nullable(False)|pode ser PIX, boleto bancario, cartao de crédito etc.|
|preco_frete|Integer|nullable(False)|preço diferente para cada regiao e para cada transporte|
|quantidade|Integer|nullable(False)|quantidade de itens no carrinho|
|preco_total|Integer|nullable(False)|preço total, incluindo tudo que foi colocado no carrinho|
|cupons_id|relationship|||
|CarrosCarrinho_id|relationship|||
|MotosCarrinho_id|relationship|||
|usuario_id|relationship|||

### Cupons
|Campo|Tipo|Argumentos|Descrição|
|-----|-----|-----|-----|
|codigo_cupom|Integer|nullable(False)|os cupons possuem codigos para poder inserir no carrinho de compras|
|valor_desconto|Integer|nullable(False)|se o desconto é de 5%, 10% etc.|
|quantidade|Integer|nullable(False)|quantidade de cupons disponíveis|
|categoria|String(20)|nullable(False)|se o cupom só é disponível em datas comemorativas, por exemplo, natal etc.|
|usuario_id|relationship|||
|carrinho|relationship|||

### Carros Carrinho
|Campo|Tipo|Argumentos|Descrição|
|-----|-----|-----|-----|
|modelo|String(20)|nullable(False)|por exemplo Fiat Uno, modelo: Uno|
|marca|String(20)|nullable(False)|por exemplo Fiat uno, marca: Fiat|
|quantidade|Integer|nullable(False)|quantidade de carros colocados no carrinho|
|preco_unitario|Integer|nullable(False)|preço de somente um carro colocado no carrinho|
|preco_total|Integer|nullable(False)|preço total de todas os carros colocados no carrinho|
|carrinho|relationship|||
|carros_id|relationship|||

### Motos Carrinho
|Campo|Tipo|Argumentos|Descrição|
|-----|-----|-----|-----|
|modelo|String(20)|nullable(False)|por exemplo Fiat Uno, modelo: Uno|
|marca|String(20)|nullable(False)|por exemplo Fiat uno, marca: Fiat|
|quantidade|Integer|nullable(False)|quantidade de motos colocadas no carrinho|
|preco_unitario|Integer|nullable(False)|preço de somente uma moto|
|preco_total|Integer|nullable(False)|preço total de todos as motos colocadas|
|carrinho|relationship|||
|motos_id|relationship|||

***
## Rotas
|Endpoint|Método|Descrição|
|-----|-----|-----|
|/login|POST|Usuario qualquer envia email e senha para fazer login e recebe seu token|
|/send_mail/reset|POST| caso tenha esquecido a senha, token enviado por email|
|/reset/<string:token>|PATCH|Usuario registrado envia nova senha|
|/files/put_url/formato|GET|para pegar o caminho do digital ocean|
|/usuarios|GET|visualização de todos os usuários|
|/usuarios|POST|cadastro de novo usuário|
|/usuarios/<int:id>|GET|usuario logado pode ver suas informações, usando seu token|
|/usuarios/<int:id>?fields=<atributo_1>, <atributo_2>|GET|visualização dos atributos escolhidos separados por vírgula de um determinado usuário, usando seu token|
|/usuarios/<int:id>|PUT|Usuario logado pode alterar todas suas informações, usando seu token|
|/usuarios/<int:id>|PATCH|Usuario logado pode alterar alguma de suas informações, usando seu token|
|/usuarios/<int:id>|DELETE|Usuario logado pode deletar seu perfil, usando seu token|
|/carros|GET|visualização de todos os carros|
|/carros|POST|cadastro de novo carro|
|/carros/<int:id>|GET|carro logado pode ver suas informações|
|/carros/<int:id>|PUT|carro logado pode alterar todas suas informações|
|/carros/<int:id>|PATCH|carro logado pode alterar alguma de suas informações|
|/carros/<int:id>|DELETE|carro logado pode deletar seu perfil|
|/motos|GET|visualização de todas as motos|
|/motos|POST|cadastro de nova moto|
|/motos/<int:id>|GET|moto logada pode ver suas informações|
|/motos/<int:id>|PUT|moto logada pode alterar todas suas informações|
|/motos/<int:id>|PATCH|moto logada pode alterar alguma de suas informações|
|/motos/<int:id>|DELETE|moto logada pode deletar seu perfil|
|/cupons|GET|visualização de todos os cupons|
|/cupons|POST|cadastro de novo cupom|
|/cupons/<int:id>|GET|cupom logado pode ver suas informações|
|/cupons/<int:id>|PUT|cupom logado pode alterar todas suas informações|
|/cupons/<int:id>|PATCH|cupom logado pode alterar alguma de suas informações|
|/cupons/<int:id>|DELETE|cupom logado pode deletar seu perfil|
|/carroscarrinho|GET|visualização de todos os carros carrinho|
|/carroscarrinho|POST|cadastro de novo carro carrinho|
|/carroscarrinho/<int:id>|GET|carro carrinho logado pode ver suas informações|
|/carroscarrinho/<int:id>|PUT|carro carrinho logado pode alterar todas suas informações|
|/carroscarrinho/<int:id>|PATCH|carro carrinho logado pode alterar alguma de suas informações|
|/carroscarrinho/<int:id>|DELETE|carro carrinho logado pode deletar seu perfil|
|/motoscarrinho|GET|visualização de todos as motos carrinho|
|/motoscarrinho|POST|cadastro de nova moto carrinho|
|/motoscarrinho/<int:id>|GET|moto carrinho logado pode ver suas informações|
|/motoscarrinho/<int:id>|PUT|moto carrinho logado pode alterar todas suas informações|
|/motoscarrinho/<int:id>|PATCH|moto carrinho logado pode alterar alguma de suas informações|
|/motoscarrinho/<int:id>|DELETE|moto carrinho logado pode deletar seu perfil|
|/carrinhos|GET|visualização de todos os carrinhos|
|/carrinhos|POST|cadastro de novo carrinho|
|/carrinhos/<int:id>|GET|carrinho logado pode ver suas informações|
|/carrinhos/<int:id>|PUT|carrinho logado pode alterar todas suas informações|
|/carrinhos/<int:id>|PATCH|carrinho logado pode alterar alguma de suas informações|
|/carrinhos/<int:id>|DELETE|carrinho logado pode deletar seu perfil|


***
## Exemplos

### POST /login
```
{
    "email": "karenarcoverde@poli.ufrj.br",
    "senha": "12345"
}
```
```
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0NzQ2NDYxMiwianRpIjoiNzk2NWJlM2ItMDc4YS00Njc5LTkxYmEtZTJiMjhjOTc1YjAyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjQ3NDY0NjEyLCJleHAiOjE2NDc0NjU1MTJ9.21ppfPpcGyu1nQegt7PwkL19Ro-26R3blEVG_lGC-nk"
}
```

### POST /usuarios
```
{
	"nome":"karen",
	"cpf":"23993232",
	"email":"karenarcoverde@poli.ufrj.br",
	"telefone":"23352",
	"endereco":"rua mena barreto",
	"senha":"12345"
}
```
```
{
	"id": 1,
	"nome": "karen",
	"cpf": "23993232",
	"email": "karenarcoverde@poli.ufrj.br",
	"telefone": 23352,
	"endereco": "rua mena barreto"
}
```

### GET /files/put_url/png
```

```
```
{
	"media_url": "https://nyc3.digitaloceanspaces.com/storage-fluxo/ddd-karen/557a23c0d3ed4837b6d05f2d2765277a.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=GTT4PXUAPEWSTC5OIHPO%2F20220311%2Fnyc3%2Fs3%2Faws4_request&X-Amz-Date=20220311T011808Z&X-Amz-Expires=300&X-Amz-SignedHeaders=host&X-Amz-Signature=f02937e2e9ad4e51fcbbf8879e738274b77207a2c12933adf66a7fe75667e70b",
	"file_name": "557a23c0d3ed4837b6d05f2d2765277a.png"
}
```

### POST /send_mail/reset
```
{
    "email": "karenarcoverde@poli.ufrj.br",
}
```
```
{
	"Resultado": "envio feito"
}
```

### PATCH /reset/*colocar token enviado por email aqui*
```
{
	"senha":"123456"
}
```
```
{}
```

### GET /usuarios/1?fields=email,telefone
*OBS: Colocar no "Bearer" o token*
```
{
	"email":"karenarcoverde@poli.ufrj.br",
	"senha":"12345"
}
```
```
{
	"email": "karenarcoverde@poli.ufrj.br",
	"telefone": 23352
}
```