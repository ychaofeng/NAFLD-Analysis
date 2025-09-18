def create_volcano_plot(de_results):
    import matplotlib.pyplot as plt
    import numpy as np

    plt.figure(figsize=(10, 8))
    plt.scatter(de_results['log2FoldChange'], 
                -np.log10(de_results['pvalue']),
                alpha=0.5,
                s=5,
                color='gray')

    significant = de_results['padj'] < 0.05
    plt.scatter(de_results.loc[significant, 'log2FoldChange'],
                -np.log10(de_results.loc[significant, 'pvalue']),
                alpha=0.7,
                s=5,
                color='red',
                label='FDR < 0.05')

    plt.xlabel('log2 Fold Change')
    plt.ylabel('-log10(p-value)')
    plt.title('Volcano Plot')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def create_heatmap(expression_data, sample_groups):
    import seaborn as sns
    import matplotlib.pyplot as plt

    plt.figure(figsize=(12, 8))
    sns.heatmap(expression_data, cmap='RdBu_r', center=0, xticklabels=sample_groups)
    plt.title('Heatmap of Gene Expression')
    plt.xlabel('Samples')
    plt.ylabel('Genes')
    plt.tight_layout()
    plt.show()

def create_bar_plot(enrichment_results):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(12, 6))
    enrichment_results.sort_values('Adjusted P-value').plot(kind='barh', x='Term', y='Adjusted P-value')
    plt.title('Enrichment Analysis Results')
    plt.xlabel('-log10(Adjusted P-value)')
    plt.ylabel('Pathways')
    plt.tight_layout()
    plt.show()