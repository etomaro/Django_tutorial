# Django_tutorial
https://docs.djangoproject.com/en/4.2/intro/tutorial01/

# sqliteへの入り方
$ sqlite3 db.sqlite3 

# DBスキーマ操作
1. モデルの作成・修正(APP_NAME.models.py)
2. モデルを基にマイグレーションファイルを作成($python manage.py makemigrations APP_NAME)
3. マイグレーションファイルを内容をDBに適用($python manage.py migrate)

# django内で設定されているモデル操作をシェルで操作する
$ python manage.py shell(辞めるときは, $quit)

# 管理ユーザー(管理サイトにアクセスできる)を作成する
$ python manage.py createsuperuser

Username: admin
Email address: admin@example.com
password: pass

# 管理画面へのアクセス
https://XXX/admin/
上記のURLで管理画面にアクセスできる
ここからアプリのDBの値の編集をGUIで行える

# viewsの役割
1. HttpsResponseを返すこと。django内(views内)でHttpsResponse関数を使ってもいいし、外部(例えばreact)からHttpResponseを取得してviews内で返してもいい
2. Http404のような例外を返すこと。これもHttpResponseと同様で内部でも外部で取得して物でもいい。




# ---------------------- tutorial ----------------------
1. 初期プロジェクト作成
2. DB設定、管理画面
3. view, urlの設定
4. 投票システムの作成。下記のような典型的な処理をDjangoのショートカットを使用して拘束に作成する
    """
    1. Urlに指定されたパラメータを基にDBから値を取得
    2. テンプレートを用意する
    3. テンプレートにDBの値をセットしてViewを返す
    """
5. 自動テスト



