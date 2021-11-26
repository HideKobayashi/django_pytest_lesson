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
python 3.6.11
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

以下の説明では、先頭のプロンプトは $ と記述しますが、全て仮想環境を有効にした状態で実施してください。

## Django のプロジェクトを作成する

下記のページを参考にして、Djangoプロジェクトを作成する。

はじめての Django アプリ作成、その 1
https://docs.djangoproject.com/ja/3.2/intro/tutorial01/

下記のようなファイルが自動作成されます。

```
$ tree mysite
mysite
├── manage.py
└── mysite
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

開発用Webサーバをローカル環境で起動します

```
$ cd mysite
$ python manage.py runserver 8080
```

Webブラウザを立ち上げて、下記のURLを指定します。
```
http://localhost:8080/
```
ロケットのアニメーションが表示されればOKです。

ターミナルには下記のようなメッセージが表示されます。
```
$ python manage.py runserver 8080
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
November 26, 2021 - 16:56:30
Django version 3.2.9, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8080/
Quit the server with CONTROL-C.
[26/Nov/2021 16:57:02] "GET / HTTP/1.1" 200 10697
[26/Nov/2021 16:57:02] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
[26/Nov/2021 16:57:02] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 85876
[26/Nov/2021 16:57:02] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 85692
[26/Nov/2021 16:57:02] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 86184
Not Found: /favicon.ico
[26/Nov/2021 16:57:03] "GET /favicon.ico HTTP/1.1" 404 2110
```

開発用サーバを停止するには、Ctrl-c を押します。


## モデルのマイグレーション

初期状態で、管理画面用のモデルや設定ファイルが用意されています。モデルとは、モデルとは、データベース設計をPythonのコードで実装したものです。Django ではモデルをデータベースのテーブルに自動でマッピングする機能が用意されています。モデルをデータベースのテーブルにマッピングすることをマイグレーションと呼びます。マイグレーションを実施するには下記のコマンドを実施します。

```
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```
このとき、新しく sqlite3 形式のデータベースファイル `db.sqlite3` が作成されています。

```
$ ls
db.sqlite3      manage.py*      mysite/
```

Webブラウザで管理画面を開いてみます。Webブラウザを立ち上げて、下記のURLにアクセスしてください。

```
http://localhost:8080/admin/
```
ログイン画面が表示されればOKです。

ターミナルには、下記の表示が現れます。
```
$ python manage.py runserver 8080
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 26, 2021 - 17:11:52
Django version 3.2.9, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8080/
Quit the server with CONTROL-C.
[26/Nov/2021 17:12:44] "GET /admin/ HTTP/1.1" 302 0
[26/Nov/2021 17:12:45] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 2214
[26/Nov/2021 17:12:45] "GET /static/admin/css/base.css HTTP/1.1" 200 19513
[26/Nov/2021 17:12:45] "GET /static/admin/css/fonts.css HTTP/1.1" 304 0
[26/Nov/2021 17:12:45] "GET /static/admin/css/login.css HTTP/1.1" 200 939
[26/Nov/2021 17:12:45] "GET /static/admin/css/nav_sidebar.css HTTP/1.1" 200 2271
[26/Nov/2021 17:12:45] "GET /static/admin/js/nav_sidebar.js HTTP/1.1" 200 1360
[26/Nov/2021 17:12:45] "GET /static/admin/css/responsive.css HTTP/1.1" 200 18545
[26/Nov/2021 17:12:45] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 304 0
[26/Nov/2021 17:12:45] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 304 0
```

## アプリを作成する

ここでは、チュートリアルにしたがって、polls というアプリをつくります。

下記のコマンドを入力してください。

```
$ python manage.py startapp polls
```
`manage.py` があるディレクトリの配下に `polls` というディレクトリが新しく作成されます。その下にはさらにいくつかのファイルが作られています。

```
$ tree polls
polls
├── __init__.py
├── admin.py
├── apps.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py

1 directory, 7 files
```

### ビューを作る

`polls/views.py`

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

### URLconfを作る

`polls/urls.py`

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

### ルートのURLconfにpolls.urlsモジュールの記述を反映させる

`mysite/urls.py`

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

ここまで終わったら、開発用サーバーを起動します。

```
$ python manage.py runserver 8080
```

ブラウザで確認します。

```
http://localhost:8080/polls/
```

ブラウザの画面の左上に　"Hello, world. You're at the polls index." が表示されればOKです。
