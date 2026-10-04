from pydantic_ai.exceptions import UsageLimitExceeded

from src.agent import LIMITES, agent


def main():
    print("CineData Agent — pergunte sobre o catálogo de filmes.")
    print("Comandos: 'nova' limpa o contexto, 'sair' encerra.\n")
    historico = []

    while True:
        try:
            pergunta = input("Você: ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not pergunta:
            continue
        if pergunta.lower() in {"sair", "exit", "quit"}:
            break
        if pergunta.lower() == "nova":
            historico = []
            print("Contexto limpo.\n")
            continue

        try:
            r = agent.run_sync(pergunta, message_history=historico, usage_limits=LIMITES)
        except UsageLimitExceeded:
            print("\nAgente: essa pergunta precisou de chamadas demais. Tente reformular.\n")
            continue
        except Exception as e:
            print(f"\nErro: {e}\n")
            continue

        historico = r.all_messages()
        print(f"\nAgente: {r.output}")
        print(f"[requisições nesta pergunta: {r.usage.requests}]\n")


if __name__ == "__main__":
    main()