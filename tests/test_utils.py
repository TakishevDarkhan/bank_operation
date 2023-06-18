from src import utils


def test_utils(data, capsys):
    assert utils.get_filtered(data) == data
    assert utils.data_sorted(data)[0] == data[0]
    utils.output_last_operation(data)
    captured = capsys.readouterr()
    '26.08.2019 Перевод организации' in captured.out
    "Maestro 1596 83** **** 5199 -> Счет **9589" in captured.out
    "31957.58 руб." in captured.out
