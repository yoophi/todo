TODO
======

Flask, SQLAlchemy, Flask-Security 를 이용해 만드는 TODO 서비스입니다.

OAuth2 인증을 지원하는 RESTful API 서비스를 제공합니다.

## Install

	git clone https://github.com/yoophi/todo.git
	
## Init

virtualenv 를 사용한다면 초기화하세요.

	virtualenv venv
	. venv/bin/activate
	
그리고 실행합니다.

    pip install requirements.txt    
    
    # DB 설치
    python manage.py db upgrade
    
    # 서버 실행
    python manage.py runserver
    
기본적으로 <http://localhost:5000/> 에서 서비스를 확인할 수 있습니다.