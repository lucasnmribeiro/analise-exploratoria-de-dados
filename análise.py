import pandas as pd

file_path = 'C:/Users/lcasn/OneDrive/Área de Trabalho/VExpenses/netflix_titles.csv' # Para testar, substituam pelo seu caminho.
netflix_data = pd.read_csv(file_path)

# Quais colunas estão presentes no dataset?
colunas = netflix_data.columns.tolist()
print("\nColunas presentes no dataset:\n", ', '.join(colunas))

# Quantos filmes estão disponíveis na Netflix?
total_movies = netflix_data[netflix_data['type'] == 'Movie'].shape[0]
print(f"\nTotal de filmes disponíveis na Netflix: {total_movies}")

# Quem são os 5 diretores com mais filmes e séries na plataforma?
top_directors = netflix_data['director'].dropna().value_counts().head(5)
print("\nTop 5 diretores com mais produções:")
for diretor, count in top_directors.items():
    print(f"- {diretor}: {count} produções")

# Quais diretores também atuaram como atores em suas próprias produções?
directors_in_cast = netflix_data.dropna(subset=['director', 'cast'])

# O script abaixo corrige um erro que eu estava enfrentando. O código estava considerando a coluna 'director'
# como uma única string, mesmo quando havendo diretores separados por vírgulas, assim duplicando nomes.
# Ele limpa, separa, corrige e itera e maneira apropriada. 
def director_in_cast(row):
    directors = [d.strip() for d in row['director'].split(',')]
    cast_members = [c.strip() for c in row['cast'].split(',')]
    return any(director in cast_members for director in directors)

directors_as_actors = directors_in_cast[directors_in_cast.apply(director_in_cast, axis=1)]

unique_directors_actors = set()
for _, row in directors_as_actors.iterrows():
    directors = [d.strip() for d in row['director'].split(',')]
    cast_members = [c.strip() for c in row['cast'].split(',')]
    for director in directors:
        if director in cast_members:
            unique_directors_actors.add(director)

print("\nDiretores que atuaram em suas próprias produções:")
for diretor in sorted(unique_directors_actors):
    print(f"- {diretor}")

# Insights adicionais

# Qual a quantidade de produções por país (top 5)?
productions_by_country = netflix_data['country'].value_counts().head(5)
print("\nTop 5 países com mais produções na Netflix:")
for country, count in productions_by_country.items():
    print(f"- {country}: {count} produções")

# Qual a distribuição das classificações indicativas (top 5)?
ratings_distribution = netflix_data['rating'].value_counts().head(5)
print("\nDistribuição das classificações indicativas mais comuns:")
for rating, count in ratings_distribution.items():
    print(f"- {rating}: {count} produções")