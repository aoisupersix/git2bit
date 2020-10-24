import json
import os


def writeTmpFile(fileName: str, data: object) -> None:
    """
    引数に与えられたobjectを./tmpフォルダに書き出します
    """
    # 特に使い道はないけど後で確認したいとき用に取得したデータを保存しておく
    os.makedirs('./tmp', exist_ok=True)
    f = open(f'./tmp/{fileName}', 'w')
    json.dump(data, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
    f.close()
