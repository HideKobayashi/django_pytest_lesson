# django_pytest_lesson
Django pytest lesson

## 環境構築

MacOS の場合の設定方法

Homebrew と pyenv をインストールしていない場合はインストールする。
インストール方法は、下記ページなどを参考にする。

Pythonの開発環境を用意しよう！（Mac）
https://prog-8.com/docs/python-env

Python 環境設定 (Windows10, MacOS)
https://midsatoh.github.io/python/install/

ここでは pyenv を使って、python 3.6.11 をインストールしたものとして以下進めます。詳しい手順は割愛します。

python のバージョンを確認します。

```
$ python -V
ython 3.6.11
```

## Python 仮想環境を使う

仮想環境を作成する
```
$ python -m venv ~/.venvs/venv_py36
```

仮想環境を有効化
```
$ source ~/.venvs/venv_py36/bin/activate
(venv_py36) $
```
仮想環境が有効になると、プロンプトの先頭に仮想環境名が丸括弧で示されます。

仮想環境を無効化
```
(venv_py36) $ deactivate
$
```
仮想環境が向こうになると、プロンプトの先頭の仮想環境名が消えてもとにもどります。

## Django, pytest, pytest-django のインストール

Django, pytest, pytest-django をインストールします。

インストール前のパッケージの確認

```
$ pip list
Package    Version
---------- -------
pip        21.3.1
setuptools 40.6.2
```

パッケージのインストール
```
(venv_py36) $ pip install django pytest pytest-django
```

インストールしたあとのパッケージの確認
```
(venv_py36) $ pip list
Package            Version
------------------ -------
asgiref            3.4.1
attrs              21.2.0
Django             3.2.9
importlib-metadata 4.8.2
iniconfig          1.1.1
packaging          21.3
pip                21.3.1
pluggy             1.0.0
py                 1.11.0
pyparsing          3.0.6
pytest             6.2.5
pytest-django      4.4.0
pytz               2021.3
setuptools         40.6.2
sqlparse           0.4.2
toml               0.10.2
typing_extensions  4.0.0
zipp               3.6.0
```

パッケージのバージョンを含めて環境を再現できるよう、パッケージのバージョン付きリストを作成します。

```
(venv_py36) $ pip freeze > requirements.lock
```

