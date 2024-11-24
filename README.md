# ecosysAuto_Gamification_Plates

### Descrição

O projeto ecosysAuto_Gamification_Plates se concentra em identificar placas de veículos a partir de imagens, coletar informações adicionais sobre os veículos e recuperar faixas de preços usando endpoints internos da ecosy AUTO. O objetivo final é alimentar um projeto de gamificação para eventos da ecosy AUTO.

### Requisitos

- Python (versão 3.8 ou superior)
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/jeffexavier/ecosysauto_gamification_plates.git
   ```

2. Acesse o diretório do projeto:

   ```bash
   cd ecosysauto_gamification_plates
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

### Configuração

#### Arquivo `.env`

Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis de ambiente:

```
AUTH_TOKEN="Bearer token"  # Seu token de autenticação
VEHICLE_DETECT_ENDPOINT="endpoint utilizado na detecção da placa com imagem base64"
VEHICLE_CHECK_ALL_ENDPOINT="endpoint de verificação dos dados com base na placa"
VEHICLE_GET_PRICE_ENDPOINT="endpoint de verificação das faixas de preço"
```

### Execução

Após configurar o `.env`, execute o seguinte comando para iniciar o processamento de imagens:

```bash
python process_images_and_save.py
```

Se tudo estiver configurado corretamente, você verá mensagens como estas no terminal:

```
Placa 'AAA9A99' já analisada com base na imagem F:\ecosys\placas\images\image1.jpg
Erro: Resposta não contém a chave ''vehicle_version_id'' para a imagem image2.jpg.
Erro: Resposta não contém a chave ''data'' para a imagem image3.jpg.
```

### Licença

Este projeto está licenciado sob os termos da [Licença MIT](https://opensource.org/licenses/MIT).