# API para Gestão de Usuários

Esta API foi criada para a disciplina **Banco de Dados I** e permite o cadastro e consulta de usuários.

URL: http://34.235.170.120:8080

## Endpoints

### 1. **Documentação Interativa (Swagger UI)**
- Caminho: `http://34.235.170.120:8080/docs`
- A documentação interativa permite testar os endpoints da API e visualizar detalhes das requisições e respostas.

### 2. **Consultar Usuários**
- **GET**: `/users?cpf={cpf}`
  - **Descrição**: Retorna uma lista de usuários. Se o parâmetro `cpf` for informado, retorna apenas o usuário correspondente ao CPF fornecido.
  - **Parâmetros**:
    - `cpf` (opcional): Número do CPF do usuário a ser consultado.
  - **Exemplo de uso**:
    - Retornar todos os usuários: `http://34.235.170.120:8080/users`
    - Retornar usuário com CPF específico: `http://34.235.170.120:8080/users?cpf=12345678901`

### 3. **Cadastrar Usuário**
- **POST**: `http://34.235.170.120:8080/user`
  - **Descrição**: Adiciona um novo usuário ao sistema.
  - **Corpo da requisição** (JSON):
    ```json
    {
      "cpf": 12345678901,
      "nome": "alguem",
      "data_nascimento": "2010-02-25"
    }
    ```