# Dicas de Python em VSCode

Este repositório possui dicas e exemplos para programar python dentro do VSCode.

## Estrutura do código do repositório

Este repositório segue um exemplo básico de backend com Flask, seguindo os padrões do [Cosmic Python](https://www.cosmicpython.com/).

No arquivo `src/app.py` você encontra a aplicação Flask básica.

Na pasta `src/schemas` estão alguns modelos do Pydantic para a validação de tipos.

Na pasta `src/services` estão implementados alguns serviços onde são organizdas as regras de negócio.

Como a aplicação é bastante simples, a forma como este repositório está estruturado é um overkill! Mas a ideia é mostrar a extensão de VSCode para Python funcionando em um ambiente semelhante aos encontrados no dia-a-dia de um dev Python.

## Subindo a apicação

Vá para a pasta `app/` e suba o servidor com o comando:

```sh
python -m flask --debug run --host=0.0.0.0 --port=8080
```

Assim que a aplicação subir, você pode usar os comandos abaixo para testar as rotas:

### Teste das rotas

#### `/soma`

```sh
curl localhost:8080/soma -d '{"x":1,"y":2}'  -H 'Content-Type: application/json'
```

#### `/health_check`

```sh
curl localhost:8080/health_check
```
