#creates a markdown report compiling all results and plots
def build_report(deg_results, survival_results):
    md = "# OncoFlow Cancer Informatics Report\n\n"

    md += "## Top Differential Genes\n"
    md += deg_results.head().to_markdown() + "\n\n"

    md += "## Survival Summary\n"
    md += survival_results.to_markdown() + "\n\n"

    return md
