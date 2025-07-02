import pandas as pd 
import seaborn as sns

dinosaurs = pd.read_csv('../data/raw/data.csv')

dinosaurs[['period name', 'period start (million years ago)', 'period end (million years ago)']] = dinosaurs['period'].str.extract(r'^(.*?)\s+(\d+)[–-](\d+)\s+million years ago$')

dinosaurs = dinosaurs.drop(['period'], axis=1)

taxonomy_splt = dinosaurs['taxonomy'].str.split()
max_clades = taxonomy_splt.apply(len).max()

taxonomy_df = pd.DataFrame(
    taxonomy_splt.tolist(),
    columns=[f'Clade_{i+1}' for i in range(max_clades)])

dinosaurs = pd.concat([dinosaurs, taxonomy_df], axis=1)

dinosaurs = dinosaurs.drop(['Clade_8', 'Clade_9', 'Clade_10', 'Clade_11', 'Clade_12', 'Clade_13', 'Clade_14', 'Clade_15', 'Clade_16', 'Clade_17'], axis=1).head(3)

dinosaurs = dinosaurs.rename(columns={
    'Clade_1': 'Kingdom',
    'Clade_2': 'Phylum',
    'Clade_3': 'Class',
    'Clade_4': 'Order',
    'Clade_5': 'Suborder',
    'Clade_6': 'Infraorder',
    'Clade_7': 'Family'
})

