# API para Gestão de Usuários

Esta API foi criada para a disciplina **Banco de Dados I** e permite o cadastro e consulta de usuários.

## Execução

### Passos para execução em uma máquina local

1. **Clonar o repositório**:
   - Abra o terminal e clone o repositório:
     ```bash
     git clone https://github.com/seu-usuario/BancoDeDadosAPI.git
     cd BancoDeDadosAPI
     ```

2. **Criar e ativar um ambiente virtual**:
   - Certifique-se de ter o Python 3.8+ instalado em sua máquina.
   - Crie um ambiente virtual:
     ```bash
     python3 -m venv myenv
     ```
   - Ative o ambiente virtual:
     - **Linux/macOS**:
       ```bash
       source myenv/bin/activate
       ```
     - **Windows**:
       ```bash
       .\myenv\Scripts\activate
       ```

3. **Instalar as dependências**:
   - Instale as bibliotecas necessárias que estão no arquivo `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

4. **Executar a API**:
   - No ambiente virtual ativado, rode o servidor FastAPI usando o **uvicorn**:
     ```bash
     uvicorn main:app --host 127.0.0.1 --port 8000
     ```

5. **Acessar a API**:
   - A API estará disponível em [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Endpoints

### 1. **Documentação Interativa (Swagger UI)**
- Caminho: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- A documentação interativa permite testar os endpoints da API e visualizar detalhes das requisições e respostas.

### 2. **Consultar Usuários**
- **GET**: `/users?cpf={cpf}`
  - **Descrição**: Retorna uma lista de usuários. Se o parâmetro `cpf` for informado, retorna apenas o usuário correspondente ao CPF fornecido.
  - **Parâmetros**:
    - `cpf` (opcional): Número do CPF do usuário a ser consultado.
  - **Exemplo de uso**:
    - Retornar todos os usuários: [http://127.0.0.1:8000/users](http://127.0.0.1:8000/users)
    - Retornar usuário com CPF "12345678901": [http://127.0.0.1:8000/users?cpf=12345678901](http://127.0.0.1:8000/users?cpf=12345678901)

### 3. **Cadastrar Usuário**
- **POST**: `/user`
  - **Descrição**: Adiciona um novo usuário ao sistema.
  - **Corpo da requisição** (JSON):
    ```json
    {
      "cpf": 12345678901,
      "nome": "alguem",
      "data_nascimento": "2010-02-25"
    }
    ```
