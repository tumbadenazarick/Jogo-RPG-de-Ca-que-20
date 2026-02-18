# Documentação Técnica: Galaxia Aurora Final (v3.0)

## 1. Arquitetura do Multiverso
O sistema foi projetado para ser modular e resistente a falhas (Blindagem Cardinal).

### Core (Núcleo)
- `entidades.py`: Gerenciamento de classes base (Protagonista, Aliado, Inimigo).
- `economia.py`: Lógica de produção e pesquisa tecnológica.
- `militar.py`: Gestão de bases e batalhões.
- `romance.py`: Sistema de afinidade e interações.

### Sistemas Avançados
- `ia_adaptativa.py`: Ajuste dinâmico de dificuldade.
- `opostos.py`: Implementação dos sistemas Abyss e Paradox (Antítese).
- `retina.py`: Interface visual e monitoramento online.

## 2. Prevenção de Falhas e Pontes
Para resolver o problema de nomes idênticos e intenções diferentes:
1.  **Máscara OP_**: Aplicada via `utils/ponte.py` em códigos detectados como redundantes.
2.  **Quarentena**: Códigos com falhas são movidos para `/quarentena/` sem serem apagados.
3.  **Ponte Nexus**: Conecta o motor Rust `operacao_fronteira` ao ecossistema Python.

## 3. Comandos de Comportamento
- `ALERTA_MAXIMO`: "O céu escurece, a lâmina Nexus brilha!"
- `STATUS_QUO`: "Vigilância eterna nas fronteiras do Abismo."

---
*Assinado: Lord Eclipse - Sistema Nexus Integrado*
