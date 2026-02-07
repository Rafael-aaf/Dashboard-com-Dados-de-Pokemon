# Dashboard com Dados de Pokemon

## Sumário
- [Introdução](#introdução)
- [Exportação dos Dados](#exportação-dos-dados)
- [Organização dos Dados](#organização-dos-dados)
- [Análise dos Dados](#análise-dos-dados)

## Introdução
Para este projeto meu objetivo era aprender mais sobre Ciência de Dados e criar um Dashboard online. Nele, eu realizei a exportação, organização e análise com dados de Pokemon,
e utilizei várias ferramentas, como:

- Python
- Jupyter
- Pandas
- Matplotlib
- Seaborn
- Plotly
- Streamlit

O site para o dashboard é: https://dashboard-com-dados-de-pokemon-rafaelaaf.streamlit.app/


## Exportação dos Dados
Eu utilizei um arquivo ```.csv``` do site Kaggle e armazenei ele na variável ```df_pokemon```.

Esse é o dataframe inicial:

| ID | Name       | Base Exp | Height | Weight | Types          | Abilities                    | Moves                                               | Stats                                                   |
|----|------------|----------|--------|--------|----------------|------------------------------|-----------------------------------------------------|---------------------------------------------------------|
| 1  | Bulbasaur  | 64       | 7      | 69     | Grass, Poison  | Overgrow, Chlorophyll        | razor-wind, swords-dance, cut, bind, vine-whip      | HP=45, Attack=49, Defense=49, Sp.Atk=65, Sp.Def=65, Speed=45 |
| 2  | Ivysaur    | 142      | 10     | 130    | Grass, Poison  | Overgrow, Chlorophyll        | swords-dance, cut, bind, vine-whip, headbutt        | HP=60, Attack=62, Defense=63, Sp.Atk=80, Sp.Def=80, Speed=60 |
| 3  | Venusaur   | 236      | 20     | 1000   | Grass, Poison  | Overgrow, Chlorophyll        | swords-dance, cut, bind, vine-whip, headbutt        | HP=80, Attack=82, Defense=83, Sp.Atk=100, Sp.Def=100, Speed=80 |
| 4  | Charmander | 62       | 6      | 85     | Fire           | Blaze, Solar Power           | mega-punch, fire-punch, thunder-punch, scratch...   | HP=39, Attack=52, Defense=43, Sp.Atk=60, Sp.Def=50, Speed=65  |
| 5  | Charmeleon | 142      | 11     | 190    | Fire           | Blaze, Solar Power           | mega-punch, fire-punch, thunder-punch, scratch...   | HP=58, Attack=64, Defense=58, Sp.Atk=80, Sp.Def=65, Speed=80  |

 
## Organização dos Dados

Nesta etapa, eu utilizei o Jupyter e o Pandas

O que mudou:
- Colunas em minúsculo.
- Separei os tipos em 2 colunas.
- Separei os stats em 6 colunas: 'hp', 'attack', 'defense', 'specialattack', 'specialdefense', 'speed'.
- Separei as habilidades em 3 colunas.
- Arrumei os dados de peso e altura, pois estavam 10 vezes maior do que deveriam ser.

Esse é o dataframe final:
| pokemon | type_1 | type_2 | base_experience | height_m | weight_kg | hp | attack | defense | specialattack | specialdefense | speed | ability_1 | ability_2 | ability_3 |
|--------|--------|--------|-----------------|----------|-----------|----|--------|---------|---------------|----------------|-------|-----------|-----------|-----------|
| bulbasaur | grass | poison | 64  | 0.7 | 6.9  | 45 | 49 | 49 | 65 | 65 | 45 | overgrow | chlorophyll | NaN |
| ivysaur   | grass | poison | 142 | 1.0 | 13.0 | 60 | 62 | 63 | 80 | 80 | 60 | overgrow | chlorophyll | NaN |
| venusaur  | grass | poison | 236 | 2.0 | 100.0 | 80 | 82 | 83 | 100 | 100 | 80 | overgrow | chlorophyll | NaN |
| charmander| fire  | NaN    | 62  | 0.6 | 8.5  | 39 | 52 | 43 | 60 | 50 | 65 | blaze | solar-power | NaN |
| charmeleon| fire  | NaN    | 142 | 1.1 | 19.0 | 58 | 64 | 58 | 80 | 65 | 80 | blaze | solar-power | NaN |


## Análise dos Dados

Por último, usei algumas bibliotecas para construção de gráficos, como Matplotlib, Seaborn, Plotly e Streamlit. Os gráficos podem ser vistos neste [arquivo](https://github.com/Rafael-aaf/Dashboard-com-Dados-de-Pokemon/blob/main/An%C3%A1lise%20de%20Dados%20de%20Pok%C3%A9mon.ipynb).



