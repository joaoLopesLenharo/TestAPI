#!/usr/bin/env python3
"""
Sistema Autônomo de Geração de Evidências
Captura automaticamente screenshots e vídeos durante a execução dos testes.
"""

import os
import sys
import time
import json
import io
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, List
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
import cv2
import numpy as np
from PIL import Image

# Adiciona o diretório raiz ao path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class EvidenceGenerator:
    """Gerador autônomo de evidências para testes."""
    
    def __init__(self, base_dir: str = "evidencias"):
        """
        Inicializa o gerador de evidências.
        
        Args:
            base_dir: Diretório base para salvar evidências
        """
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(exist_ok=True)
        
        # Mapeamento de nomes de testes para IDs de evidências
        self.test_mapping = self._load_test_mapping()
        
        # Contadores para múltiplas evidências do mesmo teste
        self.evidence_counters: Dict[str, int] = {}
        
        # Para gravação de vídeo
        self.video_writers: Dict[str, cv2.VideoWriter] = {}
        self.video_frames: Dict[str, List] = {}
        self.recording_tests: Dict[str, bool] = {}
        
    def _load_test_mapping(self) -> Dict[str, str]:
        """Carrega mapeamento de testes para IDs de evidências."""
        mapping_file = Path("planilhas/Casos_de_Teste.csv")
        
        if not mapping_file.exists():
            # Mapeamento padrão baseado nos testes existentes
            return {
                "test_user_registration_and_login": "CT-003",
                "test_add_food_entry": "CT-008",
                "test_dark_mode_toggle": "CT-040",
                "test_login_route": "CT-001",
                "test_invalid_login": "CT-002",
                "test_register_route": "CT-003",
            }
        
        # Lê o CSV e cria mapeamento
        mapping = {}
        try:
            with open(mapping_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                # Pula o cabeçalho
                for line in lines[1:]:
                    parts = line.strip().split(',')
                    if len(parts) >= 1:
                        ct_id = parts[0].strip()
                        # Mapeia por padrão baseado no ID
                        mapping[f"test_case_{ct_id.lower()}"] = ct_id
        except Exception as e:
            print(f"⚠️  Erro ao carregar mapeamento: {e}")
        
        return mapping
    
    def get_evidence_id(self, test_name: str, test_id: Optional[str] = None) -> str:
        """
        Obtém o ID da evidência para um teste.
        
        Args:
            test_name: Nome do teste
            test_id: ID do caso de teste (opcional)
            
        Returns:
            ID da evidência (ex: CT-001)
        """
        if test_id:
            return test_id
        
        # Tenta encontrar no mapeamento
        for key, value in self.test_mapping.items():
            if key.lower() in test_name.lower():
                return value
        
        # Extrai ID do nome do teste se possível
        if "CT-" in test_name or "ct-" in test_name:
            import re
            match = re.search(r'[Cc][Tt]-(\d+)', test_name)
            if match:
                return f"CT-{match.group(1).zfill(3)}"
        
        # Gera ID baseado no nome do teste
        return f"CT-{test_name[:10].upper().replace('_', '-')}"
    
    def capture_screenshot(self, driver: WebDriver, test_name: str, 
                          test_id: Optional[str] = None, 
                          suffix: str = "") -> str:
        """
        Captura um screenshot do navegador.
        
        Args:
            driver: Instância do WebDriver
            test_name: Nome do teste
            test_id: ID do caso de teste (opcional)
            suffix: Sufixo para o arquivo (ex: "-F" para falha, "-R" para regressão)
            
        Returns:
            Caminho do arquivo salvo
        """
        evidence_id = self.get_evidence_id(test_name, test_id)
        
        # Incrementa contador se já existe evidência com mesmo ID
        key = f"{evidence_id}{suffix}"
        if key in self.evidence_counters:
            self.evidence_counters[key] += 1
            filename = f"IMG-{evidence_id}{suffix}-{self.evidence_counters[key]}.png"
        else:
            self.evidence_counters[key] = 0
            filename = f"IMG-{evidence_id}{suffix}.png"
        
        filepath = self.base_dir / filename
        
        try:
            # Captura screenshot
            driver.save_screenshot(str(filepath))
            print(f"Screenshot capturado: {filename}")
            return str(filepath)
        except Exception as e:
            print(f"ERRO: Erro ao capturar screenshot: {e}")
            return ""
    
    def start_video_recording(self, driver: WebDriver, test_name: str,
                             test_id: Optional[str] = None) -> bool:
        """
        Inicia gravação de vídeo para um teste.
        
        Args:
            driver: Instância do WebDriver
            test_name: Nome do teste
            test_id: ID do caso de teste (opcional)
            
        Returns:
            True se iniciou com sucesso
        """
        evidence_id = self.get_evidence_id(test_name, test_id)
        key = f"VID-{evidence_id}"
        
        if key in self.recording_tests and self.recording_tests[key]:
            return False  # Já está gravando
        
        self.recording_tests[key] = True
        self.video_frames[key] = []
        
        print(f"Iniciando gravacao de video: {evidence_id}")
        return True
    
    def capture_video_frame(self, driver: WebDriver, test_name: str,
                            test_id: Optional[str] = None):
        """
        Captura um frame para o vídeo.
        
        Args:
            driver: Instância do WebDriver
            test_name: Nome do teste
            test_id: ID do caso de teste (opcional)
        """
        evidence_id = self.get_evidence_id(test_name, test_id)
        key = f"VID-{evidence_id}"
        
        if key not in self.recording_tests or not self.recording_tests[key]:
            return
        
        try:
            # Captura screenshot como frame
            screenshot = driver.get_screenshot_as_png()
            img = Image.open(io.BytesIO(screenshot))
            frame = np.array(img)
            self.video_frames[key].append(frame)
        except Exception as e:
            print(f"AVISO: Erro ao capturar frame: {e}")
    
    def stop_video_recording(self, test_name: str, test_id: Optional[str] = None,
                            suffix: str = "") -> str:
        """
        Para a gravação de vídeo e salva o arquivo.
        
        Args:
            test_name: Nome do teste
            test_id: ID do caso de teste (opcional)
            suffix: Sufixo para o arquivo
            
        Returns:
            Caminho do arquivo salvo
        """
        evidence_id = self.get_evidence_id(test_name, test_id)
        key = f"VID-{evidence_id}"
        
        if key not in self.recording_tests or not self.recording_tests[key]:
            return ""
        
        self.recording_tests[key] = False
        
        if key not in self.video_frames or len(self.video_frames[key]) == 0:
            print(f"AVISO: Nenhum frame capturado para {evidence_id}")
            return ""
        
        filename = f"VID-{evidence_id}{suffix}.mp4"
        filepath = self.base_dir / filename
        
        try:
            frames = self.video_frames[key]
            if len(frames) == 0:
                return ""
            
            # Obtém dimensões do primeiro frame
            height, width = frames[0].shape[:2]
            
            # Cria VideoWriter
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            fps = 2  # 2 frames por segundo (ajustável)
            
            out = cv2.VideoWriter(str(filepath), fourcc, fps, (width, height))
            
            # Escreve frames
            for frame in frames:
                # Converte RGB para BGR se necessário
                if len(frame.shape) == 3 and frame.shape[2] == 3:
                    frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                else:
                    frame_bgr = frame
                out.write(frame_bgr)
            
            out.release()
            
            print(f"Video salvo: {filename} ({len(frames)} frames)")
            
            # Limpa frames da memória
            del self.video_frames[key]
            
            return str(filepath)
        except Exception as e:
            print(f"ERRO: Erro ao salvar video: {e}")
            return ""
    
    def generate_evidence_report(self) -> str:
        """
        Gera relatório de evidências capturadas.
        
        Returns:
            Caminho do arquivo de relatório
        """
        report_file = self.base_dir / "evidence_report.json"
        
        evidence_list = []
        for file in sorted(self.base_dir.glob("*.png")):
            evidence_list.append({
                "filename": file.name,
                "type": "screenshot",
                "size": file.stat().st_size,
                "created": datetime.fromtimestamp(file.stat().st_mtime).isoformat()
            })
        
        for file in sorted(self.base_dir.glob("*.mp4")):
            evidence_list.append({
                "filename": file.name,
                "type": "video",
                "size": file.stat().st_size,
                "created": datetime.fromtimestamp(file.stat().st_mtime).isoformat()
            })
        
        report = {
            "generated_at": datetime.now().isoformat(),
            "total_evidences": len(evidence_list),
            "evidences": evidence_list
        }
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"Relatorio de evidencias gerado: {report_file}")
        return str(report_file)


# Instância global do gerador
_evidence_generator: Optional[EvidenceGenerator] = None

def get_evidence_generator() -> EvidenceGenerator:
    """Obtém instância global do gerador de evidências."""
    global _evidence_generator
    if _evidence_generator is None:
        _evidence_generator = EvidenceGenerator()
    return _evidence_generator


if __name__ == "__main__":
    # Teste básico do gerador
    import sys
    if "--check" in sys.argv:
        print("✅ EvidenceGenerator carregado com sucesso")
        gen = EvidenceGenerator()
        print(f"📁 Diretório de evidências: {gen.base_dir.absolute()}")
        print(f"📊 Testes mapeados: {len(gen.test_mapping)}")
        sys.exit(0)
    else:
        print("Usage: python evidence_generator.py --check")
        sys.exit(1)

