# 🔧 Correção de Problema: NumPy 2.x e opencv-python

## Problema

Se você está vendo este erro:

```
A module that was compiled using NumPy 1.x cannot be run in
NumPy 2.3.4 as it may crash.
AttributeError: _ARRAY_API not found
```

Isso acontece porque `opencv-python` ainda não é totalmente compatível com NumPy 2.x.

## Solução

### Opção 1: Downgrade do NumPy (Recomendado)

```bash
pip install 'numpy<2'
```

### Opção 2: Reinstalar opencv-python

```bash
pip install --upgrade --force-reinstall opencv-python
```

### Opção 3: Usar versão específica

```bash
pip install numpy==1.26.4 opencv-python==4.9.0.80
```

## Verificar Instalação

```bash
python -c "import cv2; import numpy; print(f'OpenCV: {cv2.__version__}, NumPy: {numpy.__version__}')"
```

Deve mostrar NumPy < 2.0.0

## Após Correção

Execute novamente:

```bash
python scripts/generate_all_evidences.py
```

