try:
    import agno
    print(f"Agno instalado em: {agno.__file__}")
    from agno.playground import Playground
    print("Playground encontrado!")
except ImportError as e:
    print(f"Erro de importação: {e}")
except Exception as e:
    print(f"Outro erro: {e}")