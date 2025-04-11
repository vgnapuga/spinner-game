from logic.game_engine import GameEngine


def main() -> None:
    engine = GameEngine()
    print(f"Score: {engine.score}")
    print(engine._game_field.field)

if (__name__ == "__main__"):
    main()