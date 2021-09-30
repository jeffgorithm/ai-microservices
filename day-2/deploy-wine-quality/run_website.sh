docker run -p 127.0.0.1:8080:8080/tcp \
–network wine_quality_app \
-e WINE_QUALITY_HOST=wine_quality website