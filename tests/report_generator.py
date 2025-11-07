import os
import io
import sys
from datetime import datetime
import pytest
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_pdf_report(test_results, output_file='test_report.pdf'):
    """Gera um relatório em PDF com os resultados dos testes"""
    doc = SimpleDocTemplate(
        output_file,
        pagesize=letter,
        rightMargin=72, leftMargin=72,
        topMargin=72, bottomMargin=72
    )
    
    styles = getSampleStyleSheet()
    elements = []
    
    # Verifica se os estilos já existem antes de adicioná-los
    if 'ReportTitle' not in styles:
        styles.add(ParagraphStyle(
            name='ReportTitle',
            parent=styles['Heading1'],
            fontSize=18,
            spaceAfter=20,
            alignment=1  # 0=Left, 1=Center, 2=Right
        ))
    
    if 'ReportHeader' not in styles:
        styles.add(ParagraphStyle(
            name='ReportHeader',
            parent=styles['Heading2'],
            fontSize=14,
            spaceAfter=10,
            textColor=colors.HexColor('#2c3e50')
        ))
    
    # Título
    elements.append(Paragraph('Relatório de Testes - Calorie Tracker', styles['ReportTitle']))
    elements.append(Spacer(1, 12))
    
    # Data do relatório
    elements.append(Paragraph(
        f"<b>Data do Relatório:</b> {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}",
        styles['Normal']
    ))
    elements.append(Spacer(1, 20))
    
    # Resumo
    elements.append(Paragraph('Resumo dos Testes', styles['ReportHeader']))
    
    # Tabela de resumo
    summary_data = [
        ['Total de Testes', test_results['total']],
        ['Sucessos', test_results['passed']],
        ['Falhas', test_results['failed']],
        ['Erros', test_results['errors']],
        ['Pulados', test_results['skipped']]
    ]
    
    summary_table = Table(summary_data, colWidths=[200, 100])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c3e50')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f8f9fa')),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.HexColor('#2c3e50')),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#dee2e6')),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#dee2e6')),
    ]))
    
    elements.append(summary_table)
    elements.append(Spacer(1, 20))
    
    # Detalhes dos testes com falha
    if test_results['failed_tests']:
        elements.append(Paragraph('Testes com Falha', styles['ReportHeader']))
        
        for i, test in enumerate(test_results['failed_tests'], 1):
            elements.append(Paragraph(
                f'<b>{i}. {test["name"]}</b>',
                styles['Heading3']
            ))
            
            # Tabela de detalhes do teste
            test_data = [
                ['Arquivo', test['file']],
                ['Erro', test['error'][:500] + '...' if len(test['error']) > 500 else test['error']]
            ]
            
            test_table = Table(test_data, colWidths=[100, 400])
            test_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f8f9fa')),
                ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#6c757d')),
                ('ALIGN', (0, 0), (0, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 9),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                ('TOPPADDING', (0, 0), (-1, -1), 6),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#dee2e6')),
            ]))
            
            elements.append(test_table)
            elements.append(Spacer(1, 12))
    
    # Gera o PDF
    doc.build(elements)
    return output_file

def pytest_sessionfinish(session, exitstatus):
    """Gera o relatório em PDF após a execução dos testes"""
    report = {
        'total': session.testscollected,
        'passed': 0,
        'failed': 0,
        'errors': 0,
        'skipped': 0,
        'failed_tests': []
    }
    
    # Conta os resultados dos testes
    for item in session.items:
        if hasattr(item, 'rep_call'):
            rep = item.rep_call
            if rep.passed:
                report['passed'] += 1
            elif rep.failed:
                report['failed'] += 1
                report['failed_tests'].append({
                    'name': item.name,
                    'file': item.location[0],
                    'error': str(rep.longrepr)
                })
            elif rep.skipped:
                report['skipped'] += 1
            elif rep.outcome == 'error':
                report['errors'] += 1
    
    # Gera o relatório em PDF
    os.makedirs('tests/reports', exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = f'tests/reports/test_report_{timestamp}.pdf'
    generate_pdf_report(report, output_file)
    print(f"\nRelatório de testes gerado em: {os.path.abspath(output_file)}")