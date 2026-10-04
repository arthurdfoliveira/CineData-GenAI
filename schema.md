# Schema do banco CineData (camada Gold)

## dim_companies

| coluna | tipo | pk |
|---|---|---|
| sk_company_id | VARCHAR(64) | sim |
| nome_produtora | VARCHAR(255) |  |

Exemplos:
- {'sk_company_id': 'e17419bca33c2819ae6a261f7b854e3e63e827a109bdbe3229da95179d43d9a8', 'nome_produtora': 'Universal Pictures'}
- {'sk_company_id': 'f8e412750a4fd01adb773c05ed12d8c8f4f0c0136f586cfa085f47f29cae3498', 'nome_produtora': 'Enlight Pictures'}
- {'sk_company_id': '6a291db141ec3ec89fa9bd09032c1737b2a4f27a46cb9778b7da12321da38d67', 'nome_produtora': 'Novo Pictures'}

## dim_genres

| coluna | tipo | pk |
|---|---|---|
| sk_genre_id | VARCHAR(64) | sim |
| nome_genero | VARCHAR(50) |  |

Exemplos:
- {'sk_genre_id': '271a22f75d73e13fa558d991442ecde8d75a34a0b9f6216d44b116f8612c82dc', 'nome_genero': 'Horror'}
- {'sk_genre_id': 'd7d2f0ffb02cf5f91acf2010f88656db336d9e293f80d504b1d3dac08aa17502', 'nome_genero': 'Western'}
- {'sk_genre_id': '85f1c8c8e324b6be99b13732edd1770eb0d200d15becbd659cc47ff5e060ac43', 'nome_genero': 'Comedy'}

## dim_movies

| coluna | tipo | pk |
|---|---|---|
| sk_movie_id | VARCHAR(64) | sim |
| id_filme | VARCHAR(50) |  |
| titulo | VARCHAR(500) |  |
| data_lancamento | DATE |  |
| ano_lancamento | INTEGER |  |
| duracao_minutos | INTEGER |  |
| idioma_original | VARCHAR(10) |  |
| status_filme | VARCHAR(50) |  |
| sinopse | VARCHAR(4000) |  |
| url_poster | VARCHAR(2048) |  |
| url_backdrop | VARCHAR(2048) |  |

Exemplos:
- {'sk_movie_id': 'b5c312c4d8cee94972412b9ea785976f9dbb2c26dd11480d9f2b9b4691df1571', 'id_filme': '14564', 'titulo': 'Rings', 'data_lancamento': '2017-02-01', 'ano_lancamento': 2017, 'duracao_minutos': 102, 'idioma_original': None, 'status_filme': 'Lançado', 'sinopse': '"Julia becomes worried about her boyfriend Holt when he explores the dark urban legend of a mysterious videotape said to kill the w
- {'sk_movie_id': 'd286f479f6764d7a09951df2c51cc95b7615c4f021fedc31773b69fa3e4da5f1', 'id_filme': '32471', 'titulo': 'Mixtape', 'data_lancamento': '2021-12-03', 'ano_lancamento': 2021, 'duracao_minutos': 94, 'idioma_original': None, 'status_filme': 'Lançado', 'sinopse': 'On the eve of Y2K, orphaned 12-year-old Beverly discovers a broken mixtape crafted by her teen parents. Raised by her grandmother 
- {'sk_movie_id': '54ecb594e9ce04d4b5ba09215e8d130683c7fe6d8ef5f0d469691ae1dfe6df62', 'id_filme': '38258', 'titulo': 'Grizzly Ii: Revenge', 'data_lancamento': '2020-02-17', 'ano_lancamento': 2020, 'duracao_minutos': 74, 'idioma_original': None, 'status_filme': 'Lançado', 'sinopse': '"All hell breaks loose when a giant grizzly, reacting to the slaughter of her cubs by poachers, attacks a massive rock

## dim_people

| coluna | tipo | pk |
|---|---|---|
| sk_person_id | VARCHAR(64) | sim |
| nome_pessoa | VARCHAR(255) |  |
| tipo_pessoa | VARCHAR(20) |  |

Exemplos:
- {'sk_person_id': 'bf5e0ac295b6fb1fa19ceb03263420e75b793f0a060116e05269db88dd0aa269', 'nome_pessoa': 'Billy Dee Williams', 'tipo_pessoa': 'Ator'}
- {'sk_person_id': '49cddf9c90c501b73744c7c5f42839d103363370128a0693cdf1a7f6f2a2d558', 'nome_pessoa': 'Esther Zynn', 'tipo_pessoa': 'Ator'}
- {'sk_person_id': '4f80c66265e7497ecef27241a12979cf48e25dfd2edea335fb558a625c83b55c', 'nome_pessoa': 'Camila Selser', 'tipo_pessoa': 'Ator'}

## bridge_movie_company

| coluna | tipo | pk |
|---|---|---|
| sk_movie_id | VARCHAR(64) | sim |
| sk_company_id | VARCHAR(64) | sim |

Chaves estrangeiras:
- sk_company_id -> dim_companies.sk_company_id
- sk_movie_id -> dim_movies.sk_movie_id

Exemplos:
- {'sk_movie_id': '8a85beff7b0f64692b227466b2c9c4abb274cf1225da4d5ce495da2180ba89c8', 'sk_company_id': 'a93d6d918018600b5fba9d39dbb7898430ece8d5fb29e42a2f8db59a37f5faf7'}
- {'sk_movie_id': 'c1e53d82aeac91f16040913257678ba690813daa7a5c5d3e182866a339553ce0', 'sk_company_id': 'f0ed91f80406391e38f2e7cc647c452f8f5919e770d7d1247969c27f14bc0980'}
- {'sk_movie_id': 'ceeda10da2fb7789a0c63741e562f050cec19f48ab727861678a10e51f9fc1f9', 'sk_company_id': 'e8170686c11431164d3ad11ef91043bfb5a67a6a4af9f7e9f6e3ea51476398bd'}

## bridge_movie_genre

| coluna | tipo | pk |
|---|---|---|
| sk_movie_id | VARCHAR(64) | sim |
| sk_genre_id | VARCHAR(64) | sim |

Chaves estrangeiras:
- sk_genre_id -> dim_genres.sk_genre_id
- sk_movie_id -> dim_movies.sk_movie_id

Exemplos:
- {'sk_movie_id': 'b5c312c4d8cee94972412b9ea785976f9dbb2c26dd11480d9f2b9b4691df1571', 'sk_genre_id': '271a22f75d73e13fa558d991442ecde8d75a34a0b9f6216d44b116f8612c82dc'}
- {'sk_movie_id': 'd286f479f6764d7a09951df2c51cc95b7615c4f021fedc31773b69fa3e4da5f1', 'sk_genre_id': '85f1c8c8e324b6be99b13732edd1770eb0d200d15becbd659cc47ff5e060ac43'}
- {'sk_movie_id': 'd286f479f6764d7a09951df2c51cc95b7615c4f021fedc31773b69fa3e4da5f1', 'sk_genre_id': 'bd2d677b2ed4381b48bb1d0841052c6d076e7d634d5052e85dcbe0b8a0dedd80'}

## bridge_movie_person

| coluna | tipo | pk |
|---|---|---|
| sk_movie_id | VARCHAR(64) | sim |
| sk_person_id | VARCHAR(64) | sim |

Chaves estrangeiras:
- sk_person_id -> dim_people.sk_person_id
- sk_movie_id -> dim_movies.sk_movie_id

Exemplos:
- {'sk_movie_id': 'aeaa39e5a5aaf5ed549d66015e79f5ab0ec8597ce5992ba2dfd994889ee62fa8', 'sk_person_id': '34804511568de2626dc0316016c59db9686690e9b5ec60d229d2f9be16c6d76a'}
- {'sk_movie_id': 'af3850ad62f1372fca11335a346805439cca808ecf06f294f2efe02d2443a33d', 'sk_person_id': '8cc7024d5ffdf994a8106f161493a83b5025278cd0ac50efd3f8c31db9721ba8'}
- {'sk_movie_id': '4762d8543e630ec5e6d542ca11cd750e5f08e6cf8e18423745f8187c4dc7520e', 'sk_person_id': 'cbe46f077649e1de6aa5e3a3d101007882afc361ecf95ec3678c316a8bfa13bf'}

## dim_reviews

| coluna | tipo | pk |
|---|---|---|
| sk_review_id | VARCHAR(64) | sim |
| sk_movie_id | VARCHAR(64) |  |
| qtd_avaliacoes_usuarios | INTEGER |  |
| nota_media_usuarios | DOUBLE |  |

Chaves estrangeiras:
- sk_movie_id -> dim_movies.sk_movie_id

Exemplos:
- {'sk_review_id': 'b5c312c4d8cee94972412b9ea785976f9dbb2c26dd11480d9f2b9b4691df1571', 'sk_movie_id': 'b5c312c4d8cee94972412b9ea785976f9dbb2c26dd11480d9f2b9b4691df1571', 'qtd_avaliacoes_usuarios': 1, 'nota_media_usuarios': 0.9}
- {'sk_review_id': '828b13d31d443e6fd9cc899ddf64e71d074ab2ac59953a1db89dafd9254409df', 'sk_movie_id': '828b13d31d443e6fd9cc899ddf64e71d074ab2ac59953a1db89dafd9254409df', 'qtd_avaliacoes_usuarios': 1, 'nota_media_usuarios': 0.2}
- {'sk_review_id': '7a96c98767c6a30941381b087dfe60e457a20a0666990988cf5fd123aef7a6df', 'sk_movie_id': '7a96c98767c6a30941381b087dfe60e457a20a0666990988cf5fd123aef7a6df', 'qtd_avaliacoes_usuarios': 1, 'nota_media_usuarios': 5.9}

## fact_movies_performance

| coluna | tipo | pk |
|---|---|---|
| sk_movie_id | VARCHAR(64) | sim |
| orcamento_usd | NUMERIC(18, 2) |  |
| receita_usd | NUMERIC(18, 2) |  |
| lucro_usd | NUMERIC(18, 2) |  |
| orcamento_brl | NUMERIC(18, 2) |  |
| receita_brl | NUMERIC(18, 2) |  |
| lucro_brl | NUMERIC(18, 2) |  |
| popularidade | DOUBLE |  |
| nota_tmdb | DOUBLE |  |
| qtd_tmdb | INTEGER |  |
| nota_imdb | DOUBLE |  |
| qtd_imdb | INTEGER |  |

Chaves estrangeiras:
- sk_movie_id -> dim_movies.sk_movie_id

Exemplos:
- {'sk_movie_id': 'b5c312c4d8cee94972412b9ea785976f9dbb2c26dd11480d9f2b9b4691df1571', 'orcamento_usd': 25000000, 'receita_usd': 83080890, 'lucro_usd': 58080890, 'orcamento_brl': 78682500, 'receita_brl': 261480485.1, 'lucro_brl': 182797985.1, 'popularidade': 24.584, 'nota_tmdb': 4.966, 'qtd_tmdb': 2375, 'nota_imdb': 4.5, 'qtd_imdb': 46286}
- {'sk_movie_id': 'd286f479f6764d7a09951df2c51cc95b7615c4f021fedc31773b69fa3e4da5f1', 'orcamento_usd': None, 'receita_usd': None, 'lucro_usd': 0, 'orcamento_brl': None, 'receita_brl': None, 'lucro_brl': 0, 'popularidade': 8.929, 'nota_tmdb': 7.064, 'qtd_tmdb': 118, 'nota_imdb': 6.6, 'qtd_imdb': 4617}
- {'sk_movie_id': '54ecb594e9ce04d4b5ba09215e8d130683c7fe6d8ef5f0d469691ae1dfe6df62', 'orcamento_usd': 7500000, 'receita_usd': None, 'lucro_usd': -7500000, 'orcamento_brl': 32363250, 'receita_brl': None, 'lucro_brl': -32363250, 'popularidade': None, 'nota_tmdb': 3.161, 'qtd_tmdb': 28, 'nota_imdb': None, 'qtd_imdb': None}

## movie_reviews

| coluna | tipo | pk |
|---|---|---|
| id | INTEGER | sim |
| sk_movie_review_id | VARCHAR(64) |  |
| sk_movie_id | VARCHAR(64) |  |
| name | VARCHAR(120) |  |
| rating | DOUBLE |  |
| text | VARCHAR(4000) |  |
| created_at | DATETIME |  |

Chaves estrangeiras:
- sk_movie_id -> dim_movies.sk_movie_id

Exemplos:
- {'id': 1, 'sk_movie_review_id': 'a9605da4b01e5f61d0623ddf0ff189de61e1ddd9dbddd30213ed609c2bbaf54e', 'sk_movie_id': '48767763d50f8bdac4e2c2af298a83562e4f0031de6d2446ccb10bac86d8eacc', 'name': 'Henrique Carvalho', 'rating': 9.8, 'text': 'Adorei cada minuto, uma experiência inesquecível.', 'created_at': '2026-09-28 15:49:34'}
- {'id': 2, 'sk_movie_review_id': 'a8e08425791b3b5d7be3c73842e2ccf747d274baf2819ace31081e2853c5ebda', 'sk_movie_id': 'f74334b36599b97ff4eb7fd0bb76d946b9df5e711062b73885f742fec7c1c9f7', 'name': 'Lucas Silva', 'rating': 2.4, 'text': 'Horrível! Perda de tempo.', 'created_at': '2026-09-28 15:49:34'}
- {'id': 3, 'sk_movie_review_id': '4bf79b3c90409e763565e1dc8eb28462ba895bfaf1bbe2acd2403f194fab1701', 'sk_movie_id': '7f81b30a8987982c36276f599aec2e07bceecd2c7bfd68b2136fe6bfbfa500c5', 'name': 'Gabriela Cardoso', 'rating': 7.7, 'text': 'Ótimo entretenimento, não decepciona.', 'created_at': '2026-09-28 15:49:34'}
