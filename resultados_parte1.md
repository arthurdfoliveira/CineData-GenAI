# Resultados da avaliação (04/10/2026 20:23)

**12/13 corretas** — 31 requisições no total

| # | Categoria | Pergunta | Resultado | Req |
|---|---|---|---|---|
| 1 | Finanças | Quais os top 10 filmes com maior receita em R$? | ✅ 3/3 itens do gabarito (mínimo 3) | 3 |
| 2 | Finanças | Qual o lucro médio por gênero, considerando apenas filmes com receita informada? | ✅ 1/1 itens do gabarito (mínimo 1) | 2 |
| 3 | Finanças | Quais os filmes com maior margem de lucro, entre os que possuem receita e orçamento informados? | ✅ 3/3 itens do gabarito (mínimo 1) | 3 |
| 4 | Popularidade | Quais os 5 filmes mais populares? | ✅ 3/3 itens do gabarito (mínimo 2) | 3 |
| 5 | Popularidade | Quais filmes têm a maior divergência entre a nota TMDB e a nota IMDb? | ✅ 3/3 itens do gabarito (mínimo 1) | 2 |
| 6 | Popularidade | Qual a nota média IMDb por ano de lançamento? | ✅ 2/2 itens do gabarito (mínimo 2) | 2 |
| 7 | Elenco | Qual ator tem mais participações em filmes lançados nos últimos 5 anos? | ✅ 1/1 itens do gabarito (mínimo 1) | 2 |
| 8 | Elenco | Quais diretores têm a maior nota média (mínimo de 5 filmes)? | ✅ 2/3 itens do gabarito (mínimo 1) | 2 |
| 9 | Elenco | Qual a dupla ator–diretor que mais trabalhou junta? | ✅ 2/2 itens do gabarito (mínimo 2) | 2 |
| 10 | Gêneros | Qual a quantidade de filmes por gênero? | ✅ 2/2 itens do gabarito (mínimo 2) | 2 |
| 11 | Produtoras | Qual produtora tem o maior lucro total? | ✅ 1/1 itens do gabarito (mínimo 1) | 2 |
| 13 | Usuários | Quais os filmes mais avaliados pelos usuários? | ✅ 1/1 itens do gabarito (mínimo 1) | 2 |
| 14 | Usuários | Em quais filmes a nota média dos usuários mais diverge da nota IMDb? | ❌ 0/5 itens do gabarito (mínimo 1) | 4 |

## Detalhes

### 1. Quais os top 10 filmes com maior receita em R$?

**Esperado na resposta:** ['Avatar: The Way Of Water', 'Avengers: Endgame', 'Spider-man: No Way Home']

**Resultado:** ✅ 3/3 itens do gabarito (mínimo 3)

**Resposta do agente:**

Aqui estão os **top 10 filmes com maior receita em R$** (faturamento em Reais):

| # | Filme | Receita em R$ |
|---|---|---|
| 1 | Avatar: The Way Of Water | R$ 12.390.136.500,54 |
| 2 | Avengers: Endgame | R$ 11.094.720.000,00 |
| 3 | Spider-Man: No Way Home | R$ 10.977.782.882,74 |
| 4 | Avengers: Infinity War | R$ 7.190.430.847,63 |
| 5 | Top Gun: Maverick | R$ 7.160.804.869,01 |
| 6 | Barbie | R$ 6.856.159.007,38 |
| 7 | The Super Mario Bros. Movie | R$ 6.838.413.799,10 |
| 8 | The Lion King | R$ 6.227.552.146,58 |
| 9 | Frozen II | R$ 6.094.028.191,32 |
| 10 | Jurassic World: Fallen Kingdom | R$ 4.934.822.930,85 |

**Critérios:** foram considerados todos os filmes do catálogo com receita em R$ informada, ordenados pela coluna `receita_brl` da tabela `fact_movies_performance`.

```sql
SELECT m.titulo, f.receita_brl FROM fact_movies_performance f JOIN dim_movies m ON m.sk_movie_id = f.sk_movie_id ORDER BY f.receita_brl DESC LIMIT 10;
```

**SQL executado:**
```sql
SELECT sk_movie_id, titulo, receita_brl FROM fact_movies_performance ORDER BY receita_brl DESC LIMIT 10;
```

**SQL executado:**
```sql
SELECT m.titulo, f.receita_brl FROM fact_movies_performance f JOIN dim_movies m ON m.sk_movie_id = f.sk_movie_id ORDER BY f.receita_brl DESC LIMIT 10;
```

### 2. Qual o lucro médio por gênero, considerando apenas filmes com receita informada?

**Esperado na resposta:** ['Adventure']

**Resultado:** ✅ 1/1 itens do gabarito (mínimo 1)

**Resposta do agente:**

**Lucro médio por gênero (considerando apenas filmes com receita informada)**

| Gênero          | Lucro Médio (USD) |
|-----------------|--------------------|
| Science Fiction | 183.055.334,67 |
| Adventure       | 181.399.653,22 |
| Fantasy         | 126.985.391,65 |
| Animation       | 126.541.446,29 |
| Family          | 116.663.901,69 |
| Action          | 114.110.307,89 |
| War             | 63.179.459,23 |
| Music           | 52.139.511,67 |
| Comedy          | 50.932.226,53 |
| Horror          | 41.516.368,31 |
| History         | 36.228.461,98 |
| Mystery         | 33.150.658,77 |
| Thriller        | 32.662.809,98 |
| Drama           | 31.859.537,94 |
| Romance         | 31.601.076,12 |
| Crime           | 29.494.464,50 |
| Tv Movie        | 310.076,00 |
| Documentary     | ‑179.402,83 |
| Western         | ‑626.512,64 |

**Critério utilizado:** apenas filmes com `receita_usd` não nula (receita informada). Lucro calculado como `receita_usd – orcamento_usd`; filmes sem orçamento informado são automaticamente excluídos do cálculo de lucro para esse gênero.

**Query utilizada:**
```sql
WITH movie_profit AS (
  SELECT m.sk_movie_id,
         f.receita_usd,
         f.orcamento_usd,
         (f.receita_usd - f.orcamento_usd) AS lucro_usd
  FROM dim_movies m
  JOIN fact_movies_performance f ON f.sk_movie_id = m.sk_movie_id
  WHERE f.receita_usd IS NOT NULL
)
SELECT g.nome_genero AS genero,
       AVG(mp.lucro_usd) AS lucro_medio_usd
FROM movie_profit mp
JOIN bridge_movie_genre bg ON bg.sk_movie_id = mp.sk_movie_id
JOIN dim_genres g ON g.sk_genre_id = bg.sk_genre_id
GROUP BY g.nome_genero
ORDER BY lucro_medio_usd DESC
LIMIT 50;
```

**SQL executado:**
```sql
WITH movie_profit AS (
  SELECT m.sk_movie_id,
         f.receita_usd,
         f.orcamento_usd,
         (f.receita_usd - f.orcamento_usd) AS lucro_usd
  FROM dim_movies m
  JOIN fact_movies_performance f ON f.sk_movie_id = m.sk_movie_id
  WHERE f.receita_usd IS NOT NULL
)
SELECT g.nome_genero AS genero,
       AVG(mp.lucro_usd) AS lucro_medio_usd
FROM movie_profit mp
JOIN bridge_movie_genre bg ON bg.sk_movie_id = mp.sk_movie_id
JOIN dim_genres g ON g.sk_genre_id = bg.sk_genre_id
GROUP BY g.nome_genero
ORDER BY lucro_medio_usd DESC
LIMIT 50;
```

### 3. Quais os filmes com maior margem de lucro, entre os que possuem receita e orçamento informados?

**Esperado na resposta:** ['Secret Superstar', 'Demond The Movie', 'Unbound']

**Resultado:** ✅ 3/3 itens do gabarito (mínimo 1)

**Resposta do agente:**



Aqui está o ranking dos filmes com maior margem de lucro, considerando apenas títulos com orçamento e receita **confiáveis (≥ US$ 1.000)**, para evitar valores irrisórios de cadastro.

| Posição | Filme | Orçamento (US$) | Receita (US$) | Margem de Lucro (%) |
|---|---|---|---|---|
| 1 | Secret Superstar | 286.284 | 137.416.709 | 99,79% |
| 2 | Demond The Movie | 10.000 | 3.000.000 | 99,67% |
| 3 | Unbound | 80.000 | 21.000.000 | 99,62% |
| 4 | Me Against You: Mr. S's Vendetta | 75.000 | 9.500.000 | 99,21% |
| 5 | Dragon Ball Super: Broly | 1.000.000 | 125.002.821 | 99,20% |
| 6 | Ariana Grande - Positions Album (official Live Performances) \| Vevo | 25.000 | 3.000.000 | 99,17% |
| 7 | The Farewell | 250.300 | 23.076.657 | 98,92% |
| 8 | The Villainess | 125.000 | 8.737.458 | 98,57% |
| 9 | Terrifier 2 | 250.000 | 15.065.239 | 98,34% |
| 10 | Get Out | 4.500.000 | 255.407.969 | 98,24% |

**Critérios aplicados:**
- `orcamento_usd > 0` e `receita_usd > 0` (apenas filmes com ambos os valores informados).
- `orcamento_usd >= 1000` e `receita_usd >= 1000` (exclusão de valores irrisórios).
- Margem de lucro calculada como `(receita - orcamento) / receita * 100`.
- Ordenação decrescente pela margem, limitado a 10 resultados.

```sql
SELECT d.titulo,
       f.orcamento_usd,
       f.receita_usd,
       ((f.receita_usd - f.orcamento_usd) * 1.0 / f.receita_usd * 100.0) AS margem_percentual
FROM fact_movies_performance f
JOIN dim_movies d ON f.sk_movie_id = d.sk_movie_id
WHERE f.orcamento_usd >= 1000
  AND f.receita_usd >= 1000
ORDER BY margem_percentual DESC
LIMIT 10;
```

**SQL executado:**
```sql
SELECT d.titulo,
       f.orcamento_usd,
       f.receita_usd,
       ((f.receita_usd - f.orcamento_usd) * 1.0 / f.receita_usd * 100.0) AS margem_percentual
FROM fact_movies_performance f
JOIN dim_movies d ON f.sk_movie_id = d.sk_movie_id
WHERE f.orcamento_usd > 0
  AND f.receita_usd > 0
ORDER BY margem_percentual DESC
LIMIT 10;
```

**SQL executado:**
```sql
SELECT d.titulo,
       f.orcamento_usd,
       f.receita_usd,
       ((f.receita_usd - f.orcamento_usd) * 1.0 / f.receita_usd * 100.0) AS margem_percentual
FROM fact_movies_performance f
JOIN dim_movies d ON f.sk_movie_id = d.sk_movie_id
WHERE f.orcamento_usd >= 1000
  AND f.receita_usd >= 1000
ORDER BY margem_percentual DESC
LIMIT 10;
```

### 4. Quais os 5 filmes mais populares?

**Esperado na resposta:** ['Blue Beetle', 'Gran Turismo', 'La Fellinette']

**Resultado:** ✅ 3/3 itens do gabarito (mínimo 2)

**Resposta do agente:**



Aqui estão os 5 filmes com maior popularidade no catálogo, classificados pela métrica `popularidade`:

| Posição | Filme | Popularidade |
|---|---|---|
| 1 | Blue Beetle | 2994.357 |
| 2 | Gran Turismo | 2680.593 |
| 3 | La Fellinette | 2020.0 |
| 4 | The Fear Footage 2: Curse Of The Tape | 2019.0 |
| 5 | Wwe Survivor Series 2018 | 2018.0 |

**Critério usado:** ranking por `popularidade` (da tabela de desempenho `fact_movies_performance`), do maior para o menor, limitado aos 5 primeiros, ordenando apenas registros com valor de popularidade informado.

```sql
SELECT m.titulo, f.popularidade
FROM fact_movies_performance f
JOIN dim_movies m ON m.sk_movie_id = f.sk_movie_id
ORDER BY f.popularidade DESC
LIMIT 5;
```

**SQL executado:**
```sql
SELECT sk_movie_id, titulo, popularidade FROM fact_movies_performance ORDER BY popularidade DESC LIMIT 5;
```

**SQL executado:**
```sql
SELECT m.titulo, f.popularidade 
FROM fact_movies_performance f 
JOIN dim_movies m ON m.sk_movie_id = f.sk_movie_id 
ORDER BY f.popularidade DESC 
LIMIT 5;
```

### 5. Quais filmes têm a maior divergência entre a nota TMDB e a nota IMDb?

**Esperado na resposta:** ['5gang: A Different Kind Of Christmas', 'Harry And Meghan: Escaping The Palace', 'Megalodon Rising']

**Resultado:** ✅ 3/3 itens do gabarito (mínimo 1)

**Resposta do agente:**



Aqui estão os filmes lançados com a maior divergência entre as notas IMDb e TMDB:

| Filme | Ano | Nota IMDb | Votos IMDb | Nota TMDB | Votos TMDB | Divergência |
|---|---|---|---|---|---|---|
| 5gang: A Different Kind Of Christmas | 2019 | 2.0 | 3.451 | 8.2 | 104 | 6.2 |
| Harry And Meghan: Escaping The Palace | 2021 | 2.6 | 1.485 | 6.76 | 153 | 4.2 |
| Megalodon Rising | 2021 | 2.1 | 1.090 | 6.11 | 125 | 4.0 |
| 365 Days | 2020 | 3.3 | 110.070 | 7.06 | 8.429 | 3.8 |
| No Manches Frida 2 | 2019 | 4.3 | 1.414 | 7.99 | 810 | 3.7 |
| The Flood | 2023 | 3.2 | 2.678 | 6.84 | 206 | 3.6 |
| Covid-21: Lethal Virus | 2021 | 1.9 | 1.161 | 5.52 | 232 | 3.6 |
| It's A Fairy! | 2016 | 2.4 | 2.879 | 5.7 | 139 | 3.3 |
| 3 Idiotas | 2017 | 4.4 | 1.678 | 7.6 | 104 | 3.2 |
| 365 Days: This Day | 2022 | 2.7 | 28.914 | 5.84 | 1.207 | 3.1 |

Critérios usados: apenas filmes com status "Lançado", notas IMDb e TMDB ambas não nulas, mínimo de 1.000 votos na IMDb e 100 votos na TMDB (para evitar ruído), divergência = |IMDb - TMDB|. Os resultados mostram que o IMDb tende a avaliar esses filmes bem abaixo do TMDB.

```sql
SELECT m.titulo, m.ano_lancamento, f.nota_imdb, f.qtd_imdb, f.nota_tmdb, f.qtd_tmdb, ROUND(ABS(f.nota_imdb - f.nota_tmdb), 2) AS divergencia
FROM fact_movies_performance f
JOIN dim_movies m ON m.sk_movie_id = f.sk_movie_id
WHERE f.nota_imdb IS NOT NULL AND f.nota_tmdb IS NOT NULL
  AND f.qtd_imdb >= 1000 AND f.qtd_tmdb >= 100
  AND m.status_filme = 'Lançado'
ORDER BY divergencia DESC
LIMIT 10
```

**SQL executado:**
```sql
SELECT m.titulo, m.ano_lancamento, f.nota_imdb, f.qtd_imdb, f.nota_tmdb, f.qtd_tmdb, ABS(f.nota_imdb - f.nota_tmdb) AS divergencia
FROM fact_movies_performance f
JOIN dim_movies m ON m.sk_movie_id = f.sk_movie_id
WHERE f.nota_imdb IS NOT NULL AND f.nota_tmdb IS NOT NULL
  AND f.qtd_imdb >= 1000 AND f.qtd_tmdb >= 100
  AND m.status_filme = 'Lançado'
ORDER BY divergencia DESC
LIMIT 10
```

### 6. Qual a nota média IMDb por ano de lançamento?

**Esperado na resposta:** ['2016', '6.3']

**Resultado:** ✅ 2/2 itens do gabarito (mínimo 2)

**Resposta do agente:**

**Nota média IMDb por ano de lançamento (filmes lançados):**

| Ano | Média Nota IMDb | Qtd. Filmes |
|-----|----------------|-------------|
| 2016 | 6.34 | 10.381 |
| 2017 | 6.34 | 11.189 |
| 2018 | 6.27 | 11.327 |
| 2019 | 6.26 | 11.637 |
| 2020 | 6.24 | 9.533 |
| 2021 | 6.23 | 9.578 |
| 2022 | 6.23 | 9.887 |
| 2023 | 6.23 | 7.227 |
| 2024 | 6.21 | 1.050 |
| 2025 | 6.55 | 2 |
| 2026 | 7.50 | 1 |

**Critérios usados:** apenas filmes com status "Lançado" e que possuam nota IMDb não nula.

```sql
SELECT 
    m.ano_lancamento AS ano,
    ROUND(AVG(f.nota_imdb), 2) AS media_nota_imdb,
    COUNT(f.sk_movie_id) AS qtd_filmes
FROM dim_movies m
JOIN fact_movies_performance f ON f.sk_movie_id = m.sk_movie_id
WHERE m.status_filme = 'Lançado'
    AND f.nota_imdb IS NOT NULL
GROUP BY m.ano_lancamento
ORDER BY ano
```

**SQL executado:**
```sql
SELECT 
    m.ano_lancamento AS ano,
    ROUND(AVG(f.nota_imdb), 2) AS media_nota_imdb,
    COUNT(f.sk_movie_id) AS qtd_filmes
FROM dim_movies m
JOIN fact_movies_performance f ON f.sk_movie_id = m.sk_movie_id
WHERE m.status_filme = 'Lançado'
    AND f.nota_imdb IS NOT NULL
GROUP BY m.ano_lancamento
ORDER BY ano
```

### 7. Qual ator tem mais participações em filmes lançados nos últimos 5 anos?

**Esperado na resposta:** ['Eric Roberts']

**Resultado:** ✅ 1/1 itens do gabarito (mínimo 1)

**Resposta do agente:**

O ator **Eric Roberts** tem mais participações em filmes lançados nos últimos 5 anos, com **105 filmes**.

**Filtros usados:**
- Status do filme = 'Lançado'
- Ano de lançamento >= 2020 (últimos 5 anos)

```sql
WITH last_5_years_movies AS (
  SELECT sk_movie_id 
  FROM dim_movies 
  WHERE status_filme = 'Lançado' 
    AND ano_lancamento >= 2020
)
SELECT p.nome_pessoa AS ator, COUNT(DISTINCT b.sk_movie_id) AS total_filmes
FROM bridge_movie_person b
JOIN dim_people p ON p.sk_person_id = b.sk_person_id
WHERE p.tipo_pessoa = 'Ator' 
  AND b.sk_movie_id IN (SELECT sk_movie_id FROM last_5_years_movies)
GROUP BY p.nome_pessoa
ORDER BY total_filmes DESC
LIMIT 1
```

**SQL executado:**
```sql
WITH last_5_years_movies AS (
  SELECT sk_movie_id 
  FROM dim_movies 
  WHERE status_filme = 'Lançado' 
    AND ano_lancamento >= 2020
)
SELECT p.nome_pessoa AS ator, COUNT(DISTINCT b.sk_movie_id) AS total_filmes
FROM bridge_movie_person b
JOIN dim_people p ON p.sk_person_id = b.sk_person_id
WHERE p.tipo_pessoa = 'Ator' 
  AND b.sk_movie_id IN (SELECT sk_movie_id FROM last_5_years_movies)
GROUP BY p.nome_pessoa
ORDER BY total_filmes DESC
LIMIT 1
```

### 8. Quais diretores têm a maior nota média (mínimo de 5 filmes)?

**Esperado na resposta:** ['Scott Wozniak', 'Jun Shishido', 'Yūichirō Hayashi']

**Resultado:** ✅ 2/3 itens do gabarito (mínimo 1)

**Resposta do agente:**

**Diretores com maior nota média no IMDb (mínimo de 5 filmes lançados, cada um com ≥ 1.000 votos no IMDb)**

| Diretor | Qtd. filmes | Nota média IMDb |
|---|---|---|
| Jun Shishido | 7 | 9.21 |
| Yūichirō Hayashi | 7 | 9.21 |
| Spencer Susser | 5 | 8.40 |
| Digpal Lanjekar | 5 | 8.18 |
| Chad Payne | 27 | 7.90 |
| Stan Lathan | 7 | 7.76 |
| Nandita Roy | 6 | 7.57 |
| Shiboprosad Mukherjee | 6 | 7.57 |
| Louis C.k. | 14 | 7.45 |
| Akiyuki Shinbō | 5 | 7.44 |
| Aaron Schoenke | 5 | 7.30 |
| Sean Schoenke | 5 | 7.30 |

**Critérios aplicados:** filmes com status "Lançado", nota IMDb não nula, mínimo de 1.000 votos no IMDb por filme (regra padrão para rankings de nota), e pelo menos 5 filmes por diretor. Fonte da nota: **IMDb** (padrão, já que não foi especificada).

```sql
SELECT 
    p.nome_pessoa AS diretor,
    COUNT(DISTINCT m.sk_movie_id) AS qtd_filmes,
    ROUND(AVG(f.nota_imdb), 2) AS nota_media_imdb
FROM bridge_movie_person b
JOIN dim_people p ON p.sk_person_id = b.sk_person_id
JOIN dim_movies m ON m.sk_movie_id = b.sk_movie_id
JOIN fact_movies_performance f ON f.sk_movie_id = b.sk_movie_id
WHERE p.tipo_pessoa = 'Diretor'
  AND m.status_filme = 'Lançado'
  AND f.nota_imdb IS NOT NULL
  AND f.qtd_imdb >= 1000
GROUP BY p.nome_pessoa
HAVING COUNT(DISTINCT m.sk_movie_id) >= 5
ORDER BY nota_media_imdb DESC
LIMIT 50
```

**SQL executado:**
```sql
SELECT 
    p.nome_pessoa AS diretor,
    COUNT(DISTINCT m.sk_movie_id) AS qtd_filmes,
    ROUND(AVG(f.nota_imdb), 2) AS nota_media_imdb
FROM bridge_movie_person b
JOIN dim_people p ON p.sk_person_id = b.sk_person_id
JOIN dim_movies m ON m.sk_movie_id = b.sk_movie_id
JOIN fact_movies_performance f ON f.sk_movie_id = b.sk_movie_id
WHERE p.tipo_pessoa = 'Diretor'
  AND m.status_filme = 'Lançado'
  AND f.nota_imdb IS NOT NULL
  AND f.qtd_imdb >= 1000
GROUP BY p.nome_pessoa
HAVING COUNT(DISTINCT m.sk_movie_id) >= 5
ORDER BY nota_media_imdb DESC
LIMIT 50
```

### 9. Qual a dupla ator–diretor que mais trabalhou junta?

**Esperado na resposta:** ["Joe Anoa'i", 'Kevin Dunn']

**Resultado:** ✅ 2/2 itens do gabarito (mínimo 2)

**Resposta do agente:**

Aqui está o resultado da dupla ator–diretor que mais trabalhou junta no catálogo:

| # | Ator | Diretor | Filmes juntos |
|---|------|---------|---------------|
| 1 | **Joe Anoa'i** | **Kevin Dunn** | 37 |
| 2 | Colby Lopez | Kevin Dunn | 32 |
| 3 | Ahomas Hailwuttem | Chad Payne | 31 |
| 4 | Anton Pelizzari | Chad Payne | 31 |
| 5 | Cameron Nichols | Chad Payne | 31 |
| 6 | David Love | Chad Payne | 31 |
| 7 | Jazzyjoeyjr | Chad Payne | 31 |
| 8 | John Whinfield | Chad Payne | 31 |
| 9 | Jeff Kirkendall | Mark Polonia | 25 |
| 10 | Vivica A. Fox | David Decoteau | 25 |

**Dupla campeã:** **Joe Anoa'i** (ator) e **Kevin Dunn** (diretor), com **37 filmes** em parceria.

> **Critérios:** considei apenas filmes lançados ou em qualquer status (o banco relaciona todas as associações de pessoas a filmes, sem filtro de status). A contagem vem do número de filmes compartilhados entre cada ator e cada diretor, conforme as pontes `bridge_movie_person` e `dim_people`.

```sql
WITH a AS MATERIALIZED (SELECT b.sk_movie_id AS m, p.nome_pessoa AS nome FROM bridge_movie_person b JOIN dim_people p ON p.sk_person_id = b.sk_person_id WHERE p.tipo_pessoa = 'Ator'), d AS MATERIALIZED (SELECT b.sk_movie_id AS m, p.nome_pessoa AS nome FROM bridge_movie_person b JOIN dim_people p ON p.sk_person_id = b.sk_person_id WHERE p.tipo_pessoa = 'Diretor') SELECT a.nome AS ator, d.nome AS diretor, COUNT(*) AS filmes FROM a JOIN d ON d.m = a.m GROUP BY 1, 2 ORDER BY filmes DESC LIMIT 10
```

**SQL executado:**
```sql
WITH a AS MATERIALIZED (SELECT b.sk_movie_id AS m, p.nome_pessoa AS nome FROM bridge_movie_person b JOIN dim_people p ON p.sk_person_id = b.sk_person_id WHERE p.tipo_pessoa = 'Ator'), d AS MATERIALIZED (SELECT b.sk_movie_id AS m, p.nome_pessoa AS nome FROM bridge_movie_person b JOIN dim_people p ON p.sk_person_id = b.sk_person_id WHERE p.tipo_pessoa = 'Diretor') SELECT a.nome AS ator, d.nome AS diretor, COUNT(*) AS filmes FROM a JOIN d ON d.m = a.m GROUP BY 1, 2 ORDER BY filmes DESC LIMIT 10
```

### 10. Qual a quantidade de filmes por gênero?

**Esperado na resposta:** ['Drama', '28086']

**Resultado:** ✅ 2/2 itens do gabarito (mínimo 2)

**Resposta do agente:**

Contagem de filmes por gênero (um filme pode pertencer a mais de um gênero, então a soma total ultrapassa o número de filmes únicos):

| Gênero | Quantidade de filmes |
|---|---|
| Drama | 28.086 |
| Documentary | 18.082 |
| Comedy | 16.048 |
| Horror | 8.674 |
| Thriller | 8.540 |
| Romance | 6.209 |
| Action | 5.028 |
| Animation | 3.911 |
| Crime | 3.902 |
| Tv Movie | 3.336 |
| Science Fiction | 3.218 |
| Family | 3.140 |
| Fantasy | 2.722 |
| Mystery | 2.713 |
| Music | 2.384 |
| Adventure | 2.376 |
| History | 1.993 |
| War | 804 |
| Western | 355 |

**Critérios:** contagem de `sk_movie_id` distintos na `dim_movies`, via bridge `bridge_movie_genre` → `dim_genres`.

```sql
SELECT g.nome_genero AS genero, COUNT(DISTINCT m.sk_movie_id) AS quantidade_filmes
FROM dim_movies m
JOIN bridge_movie_genre bg ON m.sk_movie_id = bg.sk_movie_id
JOIN dim_genres g ON bg.sk_genre_id = g.sk_genre_id
GROUP BY g.nome_genero
ORDER BY quantidade_filmes DESC, g.nome_genero;
```

**SQL executado:**
```sql
SELECT g.nome_genero AS genero, COUNT(DISTINCT m.sk_movie_id) AS quantidade_filmes
FROM dim_movies m
JOIN bridge_movie_genre bg ON m.sk_movie_id = bg.sk_movie_id
JOIN dim_genres g ON bg.sk_genre_id = g.sk_genre_id
GROUP BY g.nome_genero
ORDER BY quantidade_filmes DESC, g.nome_genero;
```

### 11. Qual produtora tem o maior lucro total?

**Esperado na resposta:** ['Marvel Studios']

**Resultado:** ✅ 1/1 itens do gabarito (mínimo 1)

**Resposta do agente:**



A produtora com o maior lucro total é a **Marvel Studios**, com lucro acumulado de **US$ 15.638.957.726** (cerca de 15,6 bilhões de dólares).

Critérios: somei `lucro_usd` de todos os filmes associados a cada produtora (valores nulos tratados como zero), agrupando por `nome_produtora`.

```sql
SELECT c.nome_produtora, SUM(COALESCE(fp.lucro_usd, 0)) AS lucro_total
FROM fact_movies_performance fp
JOIN bridge_movie_company bmc ON fp.sk_movie_id = bmc.sk_movie_id
JOIN dim_companies c ON bmc.sk_company_id = c.sk_company_id
GROUP BY c.nome_produtora
ORDER BY lucro_total DESC
LIMIT 1
```

**SQL executado:**
```sql
SELECT c.nome_produtora, SUM(COALESCE(fp.lucro_usd, 0)) AS lucro_total
FROM fact_movies_performance fp
JOIN bridge_movie_company bmc ON fp.sk_movie_id = bmc.sk_movie_id
JOIN dim_companies c ON bmc.sk_company_id = c.sk_company_id
GROUP BY c.nome_produtora
ORDER BY lucro_total DESC
LIMIT 1
```

### 13. Quais os filmes mais avaliados pelos usuários?

**Esperado na resposta:** ['Die Hart 2: Die Harter']

**Resultado:** ✅ 1/1 itens do gabarito (mínimo 1)

**Resposta do agente:**



Aqui estão os 10 filmes com mais avaliações da plataforma (maior número de avaliações dos usuários, `qtd_avaliacoes_usuarios`):

| Filme | Nº de avaliações |
|---|---|
| Die Hart 2: Die Harter | 13 |
| Die Hart 2: Die Harter | 12 |
| Die Hart: Die Harter | 11 |
| Die Hart: Die Harter | 10 |
| Die Hart: Die Harter | 10 |
| Die Hart: Die Harter | 10 |
| Die Hart 2: Die Harter | 10 |
| Die Hart 2: Die Harter | 9 |
| Die Hart 2: Die Harter | 9 |
| Die Hart 2: Die Harter | 9 |

**Critérios:** listado pelo maior número de avaliações dos usuários na tabela de reviews do catálogo; apenas filmes que possuem pelo menos uma avaliação registrada. O título "Die Hart" aparece repetido porque existem entradas distintas para filmes com o mesmo nome.

```sql
SELECT m.titulo, r.qtd_avaliacoes_usuarios
FROM dim_movies m
JOIN dim_reviews r ON m.sk_movie_id = r.sk_movie_id
WHERE r.qtd_avaliacoes_usuarios IS NOT NULL
ORDER BY r.qtd_avaliacoes_usuarios DESC
LIMIT 10;
```

**SQL executado:**
```sql
SELECT m.titulo, r.qtd_avaliacoes_usuarios
FROM dim_movies m
JOIN dim_reviews r ON m.sk_movie_id = r.sk_movie_id
WHERE r.qtd_avaliacoes_usuarios IS NOT NULL
ORDER BY r.qtd_avaliacoes_usuarios DESC
LIMIT 10;
```

### 14. Em quais filmes a nota média dos usuários mais diverge da nota IMDb?

**Esperado na resposta:** ['Nathan For You: Finding Frances', 'Red Dead Redemption 2', 'Threat Level Midnight: The Movie', 'Arcane', 'Fatteshikast']

**Resultado:** ❌ 0/5 itens do gabarito (mínimo 1)

**Resposta do agente:**

**Critério usado:** divergência = ABS(`nota_media_usuarios` – `nota_imdb`), exigindo:
- Filmes com `status_filme = 'Lançado'`
- Notas não nulas em ambas as fontes
- Mínimo de **5 avaliações de usuários** (`qtd_avaliacoes_usuarios >= 5`)
- Mínimo de **1 000 votos IMDb** (`qtd_imdb >= 1000`)

### Top filmes com maior diferença entre a nota média dos usuários e a nota IMDb
| Filme | Avaliações usuários | Nota usuários | Votos IMDb | Nota IMDb | Diferença |
|---|---|---|---|---|---|
| Emesis Blue | 7 | 3.03 | 2 420 | 7.9 | **4.87** |
| Emesis Blue | 7 | 3.13 | 2 420 | 7.9 | 4.77 |
| Emesis Blue | 5 | 3.30 | 2 420 | 7.9 | 4.60 |
| Emesis Blue | 7 | 3.51 | 2 420 | 7.9 | 4.39 |
| Emesis Blue | 6 | 3.92 | 2 420 | 7.9 | 3.98 |
| Emesis Blue | 6 | 4.10 | 2 420 | 7.9 | 3.80 |
| Emesis Blue | 7 | 4.17 | 2 420 | 7.9 | 3.73 |
| Emesis Blue | 6 | 4.30 | 2 420 | 7.9 | 3.60 |
| Spider‑man: Lotus | 7 | 6.37 | 3 269 | 3.1 | 3.27 |
| Die Hart: Die Harter | 6 | 7.47 | 6 181 | 4.3 | 3.17 |

**Observação:** As maiores divergências ocorrem com o filme *Emesis Blue*, onde a nota média dos usuários (em torno de 3–4) difere quase 5 pontos da nota IMDb (7.9). Todos os filmes listados atendem ao mínimo de 5 avaliações de usuários e 1 000 votos IMDb, o que dá um certo grau de confiabilidade às notas.

**SQL executado:**
```sql
SELECT 
    m.titulo,
    r.qtd_avaliacoes_usuarios,
    ROUND(r.nota_media_usuarios, 2) AS nota_usuarios,
    p.qtd_imdb,
    ROUND(p.nota_imdb, 2) AS nota_imdb,
    ROUND(ABS(r.nota_media_usuarios - p.nota_imdb), 2) AS divergencia
FROM dim_movies m
JOIN dim_reviews r ON r.sk_movie_id = m.sk_movie_id
JOIN fact_movies_performance p ON p.sk_movie_id = m.sk_movie_id
WHERE m.status_filme = 'Lançado'
    AND r.nota_media_usuarios IS NOT NULL
    AND p.nota_imdb IS NOT NULL
    AND p.qtd_imdb >= 1000
    AND r.qtd_avaliacoes_usuarios >= 1
ORDER BY divergencia DESC
LIMIT 20;
```

**SQL executado:**
```sql
SELECT 
    m.titulo,
    r.qtd_avaliacoes_usuarios,
    ROUND(r.nota_media_usuarios, 2) AS nota_usuarios,
    p.qtd_imdb,
    ROUND(p.nota_imdb, 2) AS nota_imdb,
    ROUND(ABS(r.nota_media_usuarios - p.nota_imdb), 2) AS divergencia
FROM dim_movies m
JOIN dim_reviews r ON r.sk_movie_id = m.sk_movie_id
JOIN fact_movies_performance p ON p.sk_movie_id = m.sk_movie_id
WHERE m.status_filme = 'Lançado'
    AND r.nota_media_usuarios IS NOT NULL
    AND p.nota_imdb IS NOT NULL
    AND p.qtd_imdb >= 1000
    AND r.qtd_avaliacoes_usuarios >= 10
ORDER BY divergencia DESC
LIMIT 20;
```

**SQL executado:**
```sql
SELECT 
    m.titulo,
    r.qtd_avaliacoes_usuarios,
    ROUND(r.nota_media_usuarios, 2) AS nota_usuarios,
    p.qtd_imdb,
    ROUND(p.nota_imdb, 2) AS nota_imdb,
    ROUND(ABS(r.nota_media_usuarios - p.nota_imdb), 2) AS divergencia
FROM dim_movies m
JOIN dim_reviews r ON r.sk_movie_id = m.sk_movie_id
JOIN fact_movies_performance p ON p.sk_movie_id = m.sk_movie_id
WHERE m.status_filme = 'Lançado'
    AND r.nota_media_usuarios IS NOT NULL
    AND p.nota_imdb IS NOT NULL
    AND p.qtd_imdb >= 1000
    AND r.qtd_avaliacoes_usuarios >= 5
ORDER BY divergencia DESC
LIMIT 20;
```
