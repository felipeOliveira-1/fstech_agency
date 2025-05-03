import pytest
from FSTech_Consulting_Agency.Analista_ROI.analista_roi import run_analista_roi_task

def test_run_analista_roi_task_with_transcricao():
    contexto = {
        "reuniao_transcricao": (
            "O cliente deseja automatizar processos e reduzir custos em 30%. "
            "A solução deve integrar com sistemas legados e gerar relatórios mensais."
        )
    }
    resultado, _ = run_analista_roi_task("Projeção de ROI baseada na reunião", contexto)
    # Verificações básicas
    assert resultado is not None
    # Se a função retornar um dict, deve conter summary ou ROI
    if isinstance(resultado, dict):
        assert "analysis_summary" in resultado or "ROI" in str(resultado)
    else:
        assert "ROI" in str(resultado) or "projeção" in str(resultado).lower()
