from logic.game_engine import GameEngine


def main() -> None:
    engine = GameEngine()

    field_b = engine.game_field.listed_field
    print(engine.match_indexes)
    print(engine.score)

    engine.game_field.update_field(engine.match_indexes)
    engine.update_match_indexes()
    engine.update_score()
    engine.game_field.update_field(engine.match_indexes)
    print(engine.match_indexes)
    print(engine.score)
    field_a = engine.game_field.listed_field

    print(field_a == field_b)


if (__name__ == "__main__"):
    main()