from django.http import HttpRequest, HttpResponse, JsonResponse

ESSENTIAL_PARAMS = ("num1", "num2")

def restapi_main(request: HttpRequest) -> JsonResponse:
    """メイン関数 HTTPリクエストを受け付けて処理結果を返す

    HTTP GET メソッドでリクエストに含まれるパラメータを取得する。
    処理を行い、結果を JSON 形式に変換して HTTP レスポンスとして返す

    Args:
        request (HttpRequest): パラメータを含むHTTPリクエスト

    Returns:
        JsonResponse: JSON形式の内容をもつHTTPレスポンス
    """
    rdict = {
        "num1": "",
        "num2": "",
        "result": None,
        "statusCode": None,
        "message": "",
    }
    msg = ""
    try:
        # リクエストパラメータをすべて取得する
        for key in request.GET:
            rdict[key] = request.GET.get(key)

        # パラメータの妥当性を確認する
        param_check(rdict)

        # 処理を行う
        rdict["result"] = add_two_numbers(rdict["num1"], rdict["num2"])

        # 正常系のレスポンスステータスを設定
        rdict.update({'statusCode': 200, 'message': 'OK'})

    except:
        # 異常系のレスポンスステータスを設定
        rdict.update({'statusCode': 500, 'message': msg})

    return JsonResponse(rdict)


def param_check(
        rdict: dict, 
        essential_params: tuple = ESSENTIAL_PARAMS):
    """パラメータの妥当性を確認する

    整数の文字を数値に変換する

    Args:
        rdict (dict): 全リクエストパラメータを含む辞書

    Raises:
        Exception: パラメータの必須項目がない
        Exception: パラメータの値がない
        Exception: パラメータの値の文字列を整数に変換できない

    Returns:
        None: [description]
    """
    for key in essential_params:
        if not key in rdict:
            msg = f"No key: {key}"
            raise Exception()
        if not rdict[key]:
            msg = f"No value of key: {key}"
            raise Exception()
        try:
            rdict[key] = int(rdict[key])
        except:
            msg = f"Cannot convert to integer. {key}={rdict[key]}"
            raise Exception()


def add_two_numbers(num1: str, num2: str) -> int:
    """２つの数の合計を計算する

    Args:
        num1 (int): [description]
        num2 (int): [description]

    Returns:
        int: [description]
    """
    return num1 + num2
