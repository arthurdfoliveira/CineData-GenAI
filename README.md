# CineData Agent: Text-to-SQL com PydanticAI e OpenRouter

Agente de IA que responde perguntas em português sobre o catálogo de filmes da **CineData Analytics**. Ele transforma a pergunta em SQL, executa na camada Gold (SQLite) e devolve a resposta interpretada, junto com a query usada. Assim, quem não sabe SQL consegue analisar bilheteria, notas, elenco, gêneros e avaliações direto pelo terminal.

```
Você: quais os 5 filmes de terror mais lucrativos?

Agente: Considerando apenas filmes com orçamento e receita informados:

| # | Filme          | Lucro (USD) |
|---|----------------|------------:|
| 1 | It             | 661.800.000 |
| 2 | It Chapter Two | 394.122.525 |
| 3 | The Meg        | 380.517.320 |
...
[requisições nesta pergunta: 2]
```

## Stack

| Item | Escolha |
|---|---|
| Linguagem | Python 3.10+ |
| Framework de agentes | [PydanticAI](https://ai.pydantic.dev/) |
| Modelos | Modelos gratuitos (`:free`) do [OpenRouter](https://openrouter.ai/), com fallback |
| Banco de dados | SQLite (`cinerocket.db`, camada Gold em modelo estrela) |
| Interface | Linha de comando (CLI) |

## Estrutura do Projeto

```
CineData-GenAI/
├── data/cinerocket.db       # Banco SQLite (não versionado)
├── src/
│   ├── db.py                # Conexão somente leitura, validação e execução do SQL
│   ├── agent.py             # Prompt, regras de negócio, modelos e a tool run_sql
│   ├── main.py              # Loop de perguntas no terminal
│   └── export_schema.py     # Gera o schema.md a partir do banco
├── schema.md                # Schema das 10 tabelas, usado no prompt
├── avaliacao.py             # Avaliação automática com as perguntas da atividade
├── resultados_parte1.md     # Relatório da 1ª rodada de avaliação
├── resultados_parte2.md     # Relatório da 2ª rodada de avaliação
├── .env.example
└── requirements.txt
```

## Tabelas

`dim_movies` é o centro do modelo estrela. As tabelas `bridge_*` ligam filmes a gêneros, pessoas e produtoras, e `fact_movies_performance` guarda as métricas.

| Tabela | Conteúdo |
|---|---|
| `dim_movies` | 95.645 filmes, de 2016 a 2029 (título, ano, duração, status, sinopse) |
| `fact_movies_performance` | Orçamento, receita e lucro (USD e BRL), popularidade, notas e votos TMDB e IMDb |
| `dim_genres`, `dim_people`, `dim_companies` | Gêneros (em inglês), pessoas (`Ator`, `Diretor`, `Roteirista`) e produtoras |
| `dim_reviews` | Quantidade e nota média das avaliações dos usuários, 1 linha por filme |
| `movie_reviews` | Avaliações individuais dos usuários, com texto |
| `bridge_movie_genre`, `bridge_movie_person`, `bridge_movie_company` | Relações muitos-para-muitos |

O schema completo está em [`schema.md`](schema.md).

## Como Executar

**Pré-requisitos:** Python 3.10+, uma chave gratuita do OpenRouter ([openrouter.ai/keys](https://openrouter.ai/keys)) e o arquivo `cinerocket.db` da pasta do Drive da atividade.

```bash
# 1. Clonar o repositório
git clone https://github.com/arthurdfoliveira/CineData-GenAI.git
cd CineData-GenAI

# 2. Criar e ativar o ambiente virtual
python3 -m venv .venv
source .venv/bin/activate        # Linux / Mac / WSL
# .venv\Scripts\activate         # Windows

# 3. Instalar as dependências
pip install -r requirements.txt

# 4. Colocar o banco em data/
mkdir -p data
# copie o cinerocket.db para data/cinerocket.db

# 5. Configurar a chave
cp .env.example .env
# edite o .env e preencha OPENROUTER_API_KEY

# 6. Rodar o agente
python -m src.main
```

| Variável do `.env` | Obrigatória | Para que serve |
|---|---|---|
| `OPENROUTER_API_KEY` | Sim | Chave do OpenRouter |
| `DB_PATH` | Não | Caminho do banco (padrão: `data/cinerocket.db`) |
| `MODELS` | Não | Modelos separados por vírgula, em ordem de prioridade |

No chat, `nova` limpa o histórico e `sair` encerra. O agente lembra da conversa, então dá para perguntar "e as de terror?" depois de uma pergunta sobre comédias.

## Exemplos de Perguntas

- **Finanças:** Quais os top 10 filmes com maior receita em R$? / Qual o lucro médio por gênero, considerando apenas filmes com receita informada?
- **Popularidade:** Quais os 5 filmes mais populares? / Qual a nota média IMDb por ano de lançamento?
- **Elenco:** Quais diretores têm a maior nota média (mínimo de 5 filmes)? / Qual a dupla ator–diretor que mais trabalhou junta?
- **Gêneros e produtoras:** Qual a quantidade de filmes por gênero? / Qual produtora tem o maior lucro total?
- **Usuários:** Quais os filmes mais avaliados pelos usuários? / Em quais filmes a nota dos usuários mais diverge da nota IMDb?

## Arquitetura

```
Usuário → main.py → agent.py (PydanticAI + OpenRouter) → run_sql → db.py → cinerocket.db
```

O prompt de sistema já traz o `schema.md`, as regras de negócio e alguns valores reais do banco (gêneros, tipos de pessoa, status e intervalo de anos). O modelo escreve o SQL e chama a ferramenta `run_sql`, que valida e executa a consulta. Se der erro, o modelo corrige e tenta de novo. No fim, ele responde em português, explica os critérios usados e mostra a query. A maioria das perguntas custa **2 requisições**.

## Regras de Negócio

Essas regras estão no prompt e saíram de consultas feitas direto no banco antes de testar o agente.

| Regra | Por quê |
|---|---|
| Receita = faturamento = bilheteria. Dólar por padrão, real quando a pergunta fala em R$ | Os três termos aparecem nas perguntas da atividade |
| Lucro e margem só com `orcamento > 0` e `receita > 0` | Quando falta um dos dois, o lucro vem 0 ou como prejuízo falso |
| Se o usuário define o filtro, vale o dele | Ex.: "considerando apenas filmes com receita informada" |
| Margem = (receita − orçamento) ÷ receita. Rankings de margem ignoram valores abaixo de US$ 1.000 | O banco tem 71 receitas e 63 orçamentos irrisórios, que são erro de cadastro |
| Margem média de um grupo = margem agregada (soma do lucro ÷ soma da receita) | A média simples por filme dá negativa para todos os gêneros; a agregada aponta Horror com 75,9% |
| Rankings de nota exigem mínimo de votos (IMDb ≥ 1.000 ou TMDB ≥ 100) | Sem isso, um filme com um único voto 10 fica em primeiro |
| Comparações com a nota dos usuários exigem pelo menos 3 avaliações | 37.575 de 40.267 filmes têm só uma avaliação de usuário |
| Gêneros e títulos estão em inglês | "terror" vira `Horror`, "comédia" vira `Comedy` |
| Bilheteria, notas e "últimos N anos" só contam filmes `Lançado` | O catálogo vai até 2029 e inclui filmes planejados |
| Filmes duplicados aparecem uma vez nos rankings | 1.518 títulos estão cadastrados mais de uma vez ("Emesis Blue" tem 36 cópias) |

## Guardrails

| Guardrail | O que faz |
|---|---|
| Banco somente leitura | A conexão abre com `mode=ro`, então qualquer escrita é recusada pelo SQLite |
| Validador de SQL | Aceita só uma instrução `SELECT` ou `WITH` e barra `DELETE`, `DROP`, `INSERT` etc. |
| Limites de execução | Timeout de 30 s, no máximo 50 linhas por resultado e textos cortados em 200 caracteres |
| Limite de requisições | No máximo 6 chamadas ao modelo por pergunta, para proteger a cota |
| Escopo | Recusa perguntas fora do catálogo e pedidos para revelar ou mudar as instruções |

## Decisões de Projeto

- **PydanticAI:** tool calling simples, compatível com o OpenRouter e com fallback (`FallbackModel`) e limite de requisições (`UsageLimits`) prontos.
- **Fallback entre modelos gratuitos:** a lista é `openrouter/free`, `z-ai/glm-5.2:free`, `nvidia/nemotron-3.5-lightning:free` e `google/gemma-4-26b-a4b-it:free`. Se um modelo dá erro ou rate limit, o próximo assume.
- **Schema no prompt, e não como ferramenta:** consultar o schema por ferramenta custaria uma requisição a mais por pergunta. Com o schema no prompt, a maioria das perguntas sai em 2.
- **Uma ferramenta só (`run_sql`):** deixa o fluxo previsível e concentra toda a segurança no `db.py`.
- **Query modelo para a dupla ator–diretor:** a versão com join direto passava de 15 s. Com CTEs `MATERIALIZED` ela roda em poucos segundos, e esse modelo vai pronto no prompt.
- **Testes planejados por causa da cota de 50 requisições por dia:** as suposições do prompt foram conferidas primeiro com consultas diretas no banco, que não gastam cota.

## Avaliação

O `avaliacao.py` roda as 14 perguntas da atividade e 2 testes de guardrail. O gabarito de cada pergunta é calculado direto no banco, e o script confere se a resposta do agente traz os itens certos.

```bash
python avaliacao.py --gabarito    # mostra os gabaritos (não gasta cota)
python avaliacao.py --ids 9,14    # roda só essas perguntas
python avaliacao.py               # roda as 16 (~35 requisições)
```

| Rodada | Resultado | O que mudou |
|---|---|---|
| [1ª](resultados_parte1.md) | 12/13 | A pergunta sobre nota dos usuários falhou porque o agente escolhia um mínimo de avaliações diferente a cada vez. O relatório também revelou os filmes duplicados |
| [2ª](resultados_parte2.md) | 16/16 | Com as regras de duplicados, mínimo de avaliações e margem agregada, todas passaram, com média de 2,25 requisições por pergunta |

## Limitações

- A conta gratuita do OpenRouter permite 50 requisições por dia.
- O `openrouter/free` escolhe o modelo na hora, então as respostas podem variar um pouco entre execuções.
- O agente responde o que está no banco e não corrige problemas de dados, como os duplicados.
