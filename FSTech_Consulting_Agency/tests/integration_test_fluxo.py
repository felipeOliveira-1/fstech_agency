import pytest
from FSTech_Consulting_Agency.Arquiteto_de_Software.arquiteto_de_software import run_arquiteto_task
from FSTech_Consulting_Agency.Analista_ROI.analista_roi import run_analista_roi_task

def test_fluxo_completo_com_transcricao():
    transcricao = (
        "O cliente deseja um sistema web integrado com login, dashboard e relatórios. "
        "Busca automatizar processos e reduzir custos em 30%. Necessário integração com ERP e geração de relatórios mensais."
    )
    contexto = {"reuniao_transcricao": transcricao}

    # Arquiteto de Software
    resultado_arquiteto, _ = run_arquiteto_task("Análise de arquitetura baseada na reunião", contexto)
    assert resultado_arquiteto is not None
    assert any(palavra in str(resultado_arquiteto).lower() for palavra in ["arquitetura", "sistema", "proposta", "solução"])

    # Analista de ROI
    resultado_roi, _ = run_analista_roi_task("Projeção de ROI baseada na reunião", contexto)
    assert resultado_roi is not None
    assert any(palavra in str(resultado_roi).lower() for palavra in ["roi", "retorno", "projeção", "benefício"])

    # Simula integração: ambos outputs disponíveis
    assert resultado_arquiteto and resultado_roi

# Teste para transcrição vazia

def test_fluxo_com_transcricao_vazia():
    contexto = {"reuniao_transcricao": ""}
    resultado_arquiteto, _ = run_arquiteto_task("Análise de arquitetura baseada na reunião", contexto)
    resultado_roi, _ = run_analista_roi_task("Projeção de ROI baseada na reunião", contexto)
    assert resultado_arquiteto is not None
    assert resultado_roi is not None
