# 📦 Barcode Generator API

Uma API desenvolvida em **Python** para gerar códigos de barras em formato de imagem com base em códigos de produtos fornecidos. Utiliza o **Flask** para gerenciamento das rotas HTTP e a biblioteca `python-barcode` para criação dos códigos.

---

## 🚀 Funcionalidades

- **Criação de códigos de barras**: Gera uma imagem de código de barras a partir de um código de produto enviado via HTTP.
- **Validação de entrada**: Garante que o código do produto seja uma string válida.
- **Tratamento de erros**: Retorna respostas HTTP apropriadas em caso de entradas inválidas ou falhas internas.

---

## 📁 Estrutura do Projeto

```plaintext
src/
├── controllers/     # Lógica de negócios
├── drivers/         # Integração com bibliotecas externas
├── errors/          # Tratamento e tipos de erros
├── main/            # Configuração do servidor e rotas
├── validators/      # Validação de dados de entrada
├── views/           # Camada de interação com HTTP
```

---

## 📦 Requisitos

- Python **3.11** ou superior
- Dependências listadas no `requirements.txt`

---

## ⚙️ Instalação

```bash
# 1. Clone o repositório
git clone <URL_DO_REPOSITORIO>
cd codigo_barras

# 2. Crie e ative um ambiente virtual
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
# No Windows:
.venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt
```

---

## ▶️ Uso

### 1. Inicie o servidor

```bash
python run.py
```

### 2. Faça uma requisição POST para a rota `/create_tag` com um corpo JSON contendo o código do produto:

```json
{
  "product_code": "12345"
}
```

### 3. A resposta será um JSON com o caminho da imagem gerada:

```json
{
  "data": {
    "type": "Tag Image",
    "count": 1,
    "path": "12345.png"
  }
}
```

---

## ✅ Testes

Para executar os testes, utilize:

```bash
pytest
```

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## ✨ Contribuições

Contribuições são bem-vindas! Sinta-se livre para abrir issues ou pull requests.
