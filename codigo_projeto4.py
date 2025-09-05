import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date') 

# Clean data
valores_baixos = df['value'].quantile(0.0250)
valores_altos = df['value'].quantile(0.9750)
condicao = (df['value'] <= valores_baixos ) | (df['value'] >= valores_altos) 
df = df.drop(df[condicao].index)


def draw_line_plot():
    df.index = pd.to_datetime(df.index)
    # Draw line plot
    fig, ax = plt.subplots(figsize=(16, 6))
    sns.lineplot(data=df, x=df.index, y='value', color='red', linewidth=1)

    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    ax.set_ylim(20000, 180000)  
    ax.set_xlim(pd.Timestamp('2016-07-01'), pd.Timestamp('2020-01-01'))

    plt.grid(True)
    plt.tight_layout()
    plt.show()
    # Save image and return fig (don't change this part)
    fig = plt.gcf()
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    #Preparando os dados
    df_bar = df.copy()
    df_bar['year'] = df.index.year
    df_bar['month'] = df.index.month_name()

    #Agrupar e pivotar
    df_grouped = df_bar.groupby(['year', 'month'])['value'].mean().reset_index()
    month_order = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    df_grouped['month'] = pd.Categorical(df_grouped['month'], categories=month_order, ordered=True)
    df_pivot = df_grouped.pivot(index='year', columns='month', values='value')


    #Grafico
    fig, ax = plt.subplots(figsize=(14, 8))

    #Tipo de grafico
    df_pivot.plot(kind='bar', ax=ax)

    
    ax.set_title('Average Page Views per Month')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')

    #
    ax.legend(title='Months')

    #Layout 
    plt.tight_layout()

    # Salva e retorna a figura
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['date'] = pd.to_datetime(df_box['date'])
    df_box = df_box[(df_box['date'].dt.year >= 2016) & (df_box['date'].dt.year <= 2019)]

    df_box['year'] = [d.year for d in df_box.date]


    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    df_box['month'] = pd.Categorical(df_box['month'], categories=month_order, ordered=True)

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(18, 6)) 
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[0].set_ylim(0, 200000)
    axes[0].set_yticks([0, 20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000, 200000])

    
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    axes[1].tick_params(axis='x', rotation=45)
    axes[1].set_ylim(0, 200000)


        # Ajusta layout e salva
    plt.tight_layout()
    fig.savefig('box_plot.png')
    
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
