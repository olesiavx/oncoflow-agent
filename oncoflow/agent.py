#the orchestrator module that calls all other modules in order to run the full oncoflow analysis
from .loaders import load_expression, load_clinical
from .preprocessing import clean_expression, clean_clinical
from .deg import run_deg
from .survival import run_survival
from .report import build_report

class OncoFlowAgent:
    def __init__(self, config):
        self.config = config

    def run(self):
        #this loadd the data
        expr = load_brca_expression(self.config.EXPR_RAW_PATH)
        clin = load_brca_clinical(self.config.CLIN_RAW_PATH)
        surv = load_brca_survival(self.config.SURV_PATH)

        #this preprocesses the data
        expr_clean = clean_expression(expr)
        clin_clean = clean_clinical(clin)

        #this does the differential expression analysis
        deg_results = run_deg(expr_clean, clin_clean)

        #this does the survival analysis
        survival_results = run_survival(expr_clean, clin_clean)

        #this builds the report
        report_text = build_report(deg_results, survival_results)

        return report_text
