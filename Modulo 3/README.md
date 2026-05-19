# 📊 Análise de Dados Musicais - Spotify & YouTube

## 🎯 Contexto do Projeto

**Você foi contratado pela Mateus Music** como Cientista de Dados para analisar o catálogo musical da empresa. Sua missão é explorar a base de dados contendo **mais de 20.000 músicas** e extrair insights valiosos sobre o desempenho dos artistas nas plataformas Spotify e YouTube.

A empresa precisa entender:
- Quem são os artistas mais relevantes
- Quais músicas performam melhor
- Como otimizar investimentos em marketing digital

## 📁 Sobre a Base de Dados

### Características Principais:
- **+20.000 músicas** no catálogo completo
- Dados de **Streams no Spotify** 
- Dados de **Views no YouTube**
- **Links dos vídeos** do YouTube para cada música
- **Metadados completos** de artistas e faixas

### Estrutura do DataFrame:
```csv
Artist,Track,Stream,Views,Url_youtube
Artist Name,Song Title,150000000,50000000,https://youtube.com/...
```

## 🎵 Perguntas para Análise

### **1. Importe o Pandas e mostre as informações gerais do dataframe**
**Objetivo:** Familiarizar-se com a estrutura dos dados

**Tarefas:**
- Importar a biblioteca pandas
- Carregar o arquivo CSV
- Exibir informações gerais (número de linhas, colunas, tipos de dados)
- Identificar valores nulos

**Saída esperada:**
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 20000 entries, 0 to 19999
Data columns (total 5 columns):
 #   Column       Non-Null Count  Dtype 
---  ------       --------------  ----- 
 0   Artist       20000 non-null  object
 1   Track        20000 non-null  object
 2   Stream       20000 non-null  int64 
 3   Views        20000 non-null  int64 
 4   Url_youtube  20000 non-null  object
```

### **2. Mostre as cinco primeiras linhas do dataframe**
**Objetivo:** Visualizar amostra dos dados

**Tarefas:**
- Usar método para exibir primeiras linhas
- Entender formato dos dados
- Identificar padrões iniciais

**Saída esperada:**
Tabela com 5 linhas mostrando todas as colunas

### **3. Vamos ver quais os artistas temos em nosso df e contar quantos artistas diferentes temos no nosso dataset**
**Objetivo:** Entender a diversidade artística do catálogo

**Tarefas:**
- Listar artistas únicos
- Contar quantidade total de artistas distintos
- Analisar distribuição

**Código sugerido:**
```python
artistas_unicos = df['Artist'].unique()
quantidade_artistas = df['Artist'].nunique()
```

### **4. Quais os 10 artistas com mais músicas em nosso dataset?**
**Objetivo:** Identificar artistas mais produtivos

**Tarefas:**
- Agrupar por artista
- Contar número de músicas
- Ordenar decrescentemente
- Selecionar top 10

**Saída esperada:**
DataFrame ou série com artista e quantidade de músicas

### **5. Quais as 5 músicas com mais views no YouTube?**
**Objetivo:** Identificar os vídeos mais populares

**Tarefas:**
- Ordenar por views (decrescente)
- Selecionar top 5
- Exibir informações relevantes

**Saída esperada:**
Lista com nome da música, artista e número de views

### **6. Quais os 5 artistas com mais streams no Spotify?**
**Objetivo:** Identificar artistas com maior engajamento no Spotify

**Tarefas:**
- Agrupar por artista
- Somar streams totais
- Ordenar decrescentemente
- Selecionar top 5

**Código sugerido:**
```python
top_artistas_streams = df.groupby('Artist')['Stream'].sum().sort_values(ascending=False).head(5)
```

## 💻 Tecnologias Utilizadas

- **Python 3.x**
- **Pandas** - Manipulação de dados
- **Jupyter Notebook** - Ambiente de análise

## 📊 Métodos do Pandas que você vai precisar:

- `pd.read_csv()` - Carregar dados
- `.info()` - Informações do DataFrame
- `.head()` - Primeiras linhas
- `.unique()` - Valores únicos
- `.nunique()` - Contagem de valores únicos
- `.groupby()` - Agrupamento
- `.sum()` - Soma
- `.count()` - Contagem
- `.sort_values()` - Ordenação
- `.reset_index()` - Resetar índice

## 🎯 Critérios de Avaliação

### **Obrigatórios:**
1. ✅ Código funcional e sem erros
2. ✅ Respostas corretas para todas as perguntas
3. ✅ Uso adequado dos métodos do pandas
4. ✅ Comentários explicativos no código
5. ✅ Organização do notebook

### **Diferenciais:**
1. 🎨 Visualizações extras (gráficos)
2. 📈 Análises complementares
3. 🔍 Insights adicionais
4. 📊 Formatação profissional dos dados
5. 💡 Comentários sobre os resultados

## 💡 Dicas Importantes

### **Para a pergunta 6 (Top 5 artistas com mais streams):**
```python
# Método completo para criar DataFrame organizado
top_artistas_df = (df.groupby('Artist')['Stream']
                   .sum()
                   .sort_values(ascending=False)
                   .head(5)
                   .reset_index())

top_artistas_df.columns = ['Artista', 'Total_Streams']
```

### **Boas práticas:**
- Sempre nomeie suas colunas de forma clara
- Formate números grandes (1.000.000)
- Comente insights interessantes
- Mantenha o notebook organizado

## 📈 Entregáveis Esperados

1. **Código completo** em Jupyter Notebook (.ipynb)
2. **Respostas claras** para todas as 6 perguntas
3. **DataFrames bem formatados**
4. **Comentários explicativos**

---

**🚀 Mãos à obra!** A Mateus Music conta com sua expertise para desvendar os segredos dos dados musicais! 🎧✨

**Boa análise!** Que os dados estejam com você! 📊🎶
