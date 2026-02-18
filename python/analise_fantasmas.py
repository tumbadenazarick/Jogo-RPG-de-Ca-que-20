import ast
import os

def analisar_fantasmas(diretorio):
    definidas = set()
    chamadas = set()

    for root, _, files in os.walk(diretorio):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                with open(path, "r", errors="ignore") as f:
                    try:
                        tree = ast.parse(f.read())
                        for node in ast.walk(tree):
                            if isinstance(node, ast.FunctionDef):
                                definidas.add(node.name)
                            if isinstance(node, ast.Call):
                                if isinstance(node.func, ast.Name):
                                    chamadas.add(node.func.id)
                                elif isinstance(node.func, ast.Attribute):
                                    chamadas.add(node.func.attr)
                    except:
                        pass

    fantasmas = chamadas - definidas
    # Ignorar nomes comuns de built-ins e libs
    comuns = {'print', 'input', 'len', 'range', 'set', 'list', 'dict', 'int', 'str', 'float', 'type', 'super', 'append', 'split', 'strip', 'lower', 'join', 'isinstance', 'getattr', 'hasattr', 'info', 'get', 'items', 'values', 'last', 'add', 'setup_logger', 'iniciar_jogo', 'executar_turno', 'disparar_evento', 'processar_producao', 'executar_ciclo_militar', 'ajustar_dificuldade', 'salvar_jogo', 'carregar_jogo', 'finalizar_jogo'}
    fantasmas = fantasmas - comuns
    return fantasmas

if __name__ == "__main__":
    fantasmas = analisar_fantasmas("Galaxia_aurora_final")
    print("--- RELATÓRIO DE FUNÇÕES FANTASMA ---")
    if not fantasmas:
        print("Nenhuma função fantasma detectada (excluindo built-ins).")
    for f in fantasmas:
        print(f"👻 {f}")
