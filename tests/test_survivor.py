from src.survivor import Survivor


def test_survivor_has_name():
    survivor = Survivor("Shawna")
    assert survivor.get_name() == "Shawna"