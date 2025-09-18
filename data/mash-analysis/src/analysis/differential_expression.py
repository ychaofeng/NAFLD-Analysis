def perform_differential_expression_analysis(expression_data, sample_groups):
    import pandas as pd
    from scipy import stats
    import statsmodels.stats.multitest as multi

    results = []

    for gene in expression_data.index:
        try:
            nafl_expr = expression_data.loc[gene, sample_groups == 'NAFL'].astype(float).values
            nash_expr = expression_data.loc[gene, sample_groups == 'NASH'].astype(float).values
            
            if len(nafl_expr) == 0 or len(nash_expr) == 0:
                continue
            
            t_stat, p_val = stats.ttest_ind(nash_expr, nafl_expr, equal_var=False)
            mean_nafl = nafl_expr.mean()
            mean_nash = nash_expr.mean()
            log2_fold_change = np.log2((mean_nash + 1) / (mean_nafl + 1))
            
            results.append({
                'gene': gene,
                'log2FoldChange': log2_fold_change,
                'pvalue': p_val,
                'mean_NAFL': mean_nafl,
                'mean_NASH': mean_nash,
                't_statistic': t_stat
            })
        except Exception as e:
            print(f"Error processing gene {gene}: {str(e)}")
            continue

    results_df = pd.DataFrame(results)

    if len(results_df) > 0:
        results_df['padj'] = multi.multipletests(results_df['pvalue'], method='fdr_bh')[1]

    return results_df