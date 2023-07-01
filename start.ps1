docker build --tag telematon .

docker service rm telematon
docker container rm telematon

docker service create --name telematon `
    --secret source=app_api_id,target=app_api_id `
    --secret source=app_api_hash,target=app_api_hash `
    --secret source=session_string,target=session_string `
    --publish 8080:8080 `
    telematon