# ecs-ecr-hello
Flask 기반의 API(Application Programming Interface) 예제.
도커 이미지로 빌드 → Amazon ECR(Elastic Container Registry) 푸시 → Amazon ECS(Elastic Container Service) Fargate에서 실행

## 1) 로컬 실행(선택)
pip install -r requirements.txt
python app.py
# 브라우저: http://localhost:8001/api/hello  또는  /api/health
