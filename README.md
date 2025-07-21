# Hostname e IP Info

Uma aplicação web simples em Flask que mostra o hostname da máquina e o IP do cliente.

## Instalação

1. Clone o repositório
2. Crie um ambiente virtual:
```bash
python -m venv venv
```
3. Ative o ambiente virtual:
   - Windows:
   ```bash
   .\venv\Scripts\activate
   ```
   - Linux/Mac:
   ```bash
   source venv/bin/activate
   ```
4. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Executando o projeto

1. Ative o ambiente virtual (se ainda não estiver ativo)
2. Execute o aplicativo:
```bash
python app.py
```
3. Acesse no navegador: http://127.0.0.1:8080

## Funcionalidades

- Exibe o hostname da máquina onde o servidor está rodando
- Mostra o IP do cliente que está acessando a aplicação
- Retorna os dados em formato JSON 