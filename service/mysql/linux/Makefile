DB=control
DOCKER=db-control
FILE=dump
USER=root
PASSWORD=toor
CRED=-u${USER} -p${PASSWORD}
PARAMS=${CRED} --databases ${DB} --routines --single-transaction --add-drop-database


dump:
	docker exec ${DOCKER} sh -c 'exec mysqldump ${PARAMS}  --no-data' > ../${FILE}.sql

dump_data:
	docker exec ${DOCKER} sh -c 'exec mysqldump ${PARAMS}' > ../${FILE}.sql

dump_remote:
	ssh prod "docker exec ${DOCKER} sh -c 'exec mysqldump ${PARAMS} --no-data'" > ../${FILE}.sql

dump_remote_data:
	ssh prod "docker exec ${DOCKER} sh -c 'exec mysqldump ${PARAMS}'" > ../${FILE}.sql


restore:
	docker exec -i ${DOCKER} sh -c 'exec mysql -v ${CRED}' < ../${FILE}.sql

restore_remote:
	ssh prod "docker exec -i  ${DOCKER} sh -c 'exec mysql -v ${DB} ${CRED}'" < ../${FILE}.sql
