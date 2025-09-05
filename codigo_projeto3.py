import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')


# 2 


df['overweight'] = np.where( (df['weight'] /( (df['height'] / 100) ** 2) ) > 25, 1, 0)


# 3 Normalizando 

df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)
df['gluc'] = np.where(df['gluc'] == 1, 0, 1)

# 4
grafico_sexo_colesterol = pd.crosstab(df['sex'], df['smoke']).plot( kind='bar', color=['blue', 'red'], figsize=(8, 5))
plt.title('Smokers by gender')
plt.xlabel('Gender')
plt.ylabel('Number of smokers')
plt.legend(['Non-smoker', 'Smoker'])

def draw_cat_plot():
    
    
    # 5
    df_cat = pd.melt(df, 
                    id_vars=['cardio'], 
                    value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'],
                    var_name='variable', 
                    value_name='value')

    # 6
    df_grouped = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    df_grouped = df_grouped.rename(columns={'value': 'response'})

    # 7

    # 8
    fig = sns.catplot(
        data=df_grouped,
        kind='bar',
        x='variable',
        y='total',
        hue='response',
        col='cardio' 
    )


    # 9
    fig.savefig('catplot.png')
    return fig.figure
draw_cat_plot()


# 10
def draw_heat_map():
    # Limpeza dos dados
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Matriz de correlação
    corr = df_heat.corr()

    # Máscara para esconder a metade superior
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Gráfico
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", center=0, square=True, linewidths=.5, cbar_kws={"shrink": 0.5})
    return fig
