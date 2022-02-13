docker build -t gcr.io/samet-sandbox/yolo:v2 .

docker run -it -p 8000: 8000 gcr.io/samet-sandbox/yolo:v2

docker push gcr.io/samet-sandbox/yolo:v2
