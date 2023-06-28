API_NAME=OpenAPI-Example
API_VERSION=$(shell yq -r .info.version OpenAPI-Example.yaml)
SERVER_VERSION=1
USER=$(shell id -u)
GROUP=$(shell id -g)

GEN_VER=6.6.0

test:
	@echo $(API_VERSION)

build-server: clean
	java -jar /openapi-generator-cli-${GEN_VER}.jar generate \
                   --additional-properties=apiNameSuffix=controller_impl \
                   -t .openapi-generator-server/ \
                   -i ${API_NAME}.v1.yaml \
                   -g python-flask \
                   -o server/

build-server-local: clean
	docker run --user ${USER}\:${GROUP} --rm \
                   -v ${PWD}:/local openapitools/openapi-generator-cli:v${GEN_VER} generate \
				   --additional-properties=apiNameSuffix=controller_impl \
                   -t /local/.openapi-generator-server/ \
                   -i /local/${API_NAME}.yaml \
                   -g python-flask \
                   -o /local/server/
	docker run --rm --user ${USER} -u\:${GROUP} \
                   -v ${PWD}:/local openapitools/openapi-generator-cli:v${GEN_VER} generate \
                   --package-name ${API_NAME} \
                   --additional-properties=pythonPackageName=${API_NAME} \
                   -i /local/${API_NAME}.yaml \
                   -g html2 \
                   -o /local/server/openapi_server/docs

clean:
	rm -f -r client dist *.egg-info