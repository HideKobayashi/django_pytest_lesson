from restapi.views import (add_two_numbers)
import pytest
from pytest import param as pp


class TestAddTwoNumbers:
    """関数 add_two_numbers の単体テスト
    """

    def test_ok(self):
        """正常系
        """
        num1 = 1
        num2 = 2
        expect = 3

        actual = add_two_numbers(num1, num2)

        print("actual:", actual, end="| ")
        assert expect == actual

    def test_ng(self):
        """異常系

        条件: ２つの入力パラメータの型が違う
        期待値: 例外が上がる
        """
        num1 = 1
        num2 = 'a'

        with pytest.raises(Exception) as excinfo:
            _ = add_two_numbers(num1, num2)

        print('str(excinfo):', str(excinfo), end='| ')

    @pytest.mark.parametrize('two_numbers, expect', [
        pp((1, 2), 3, id='integers' ),
        pp(('a', 'b'), 'ab', id='strings'),
        # pp((1.1, 2.2), 3.3, id='float' ),　# 現実装では期待通りにならない
    ])
    def test_ok_multi(self, two_numbers, expect):
        """正常系

        条件: ２つの入力パラメータに整数を与える (1, 2)
        期待値: 合計値 3

        条件: ２つの入力パラメータに文字列を与える ('a', 'b')
        期待値: 文字列が連結される 'ab'

        条件: ２つの入力パラメータに浮動小数点数を与える (1.1, 2.2)
        期待値: 合計値 3.3
        """
        # -- 準備
        num1 = two_numbers[0]
        num2 = two_numbers[1]

        # -- 実行
        actual = add_two_numbers(num1, num2)

        # -- 検証
        print("actual:", actual, end="| ")
        assert expect == actual

