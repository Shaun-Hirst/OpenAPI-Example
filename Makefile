API_NAME=OpenAPI-Example
USER=$(shell id -u)
GROUP=$(shell id -g)

GEN_VER=6.2.1

build-server:
	java -jar /openapi-generator-cli-${GEN_VER}.jar generate \
                   --additional-properties=apiNameSuffix=controller_impl \
                   -t .templates/${GEN_VER}/python_flask/.openapi-generator-server/ \
                   -i openapi.yaml \
                   -g python-flask \
                   -o python_flask/

build-server-local-flask:
	docker run --user ${USER}:${GROUP} --rm \
                   -v ${PWD}:/local openapitools/openapi-generator-cli:v${GEN_VER} generate \
				   --additional-properties=apiNameSuffix=controller_impl \
                   -t /local/.templates/${GEN_VER}/python_flask/.openapi-generator-server/ \
                   -i /local/openapi.yaml \
                   -g python-flask \
                   -o /local/python_flask/

build-server-local-fastapi:
	docker run --user ${USER}:${GROUP} --rm \
                   -v ${PWD}:/local openapitools/openapi-generator-cli:v${GEN_VER} generate \
				   --additional-properties=apiNameSuffix=controller_impl \
                   -t /local/.templates/${GEN_VER}/python_fastapi/.openapi-generator-server/ \
                   -i /local/openapi.yaml \
                   -g python-fastapi \
                   -o /local/python_fastapi/

extract-templates-flask:
	docker run --user ${USER}:${GROUP} --rm \
                   -v ${PWD}:/local \
                   openapitools/openapi-generator-cli:v${GEN_VER} author template \
                   -g python-flask \
                   -o /local/.templates/${GEN_VER}/python_flask/.openapi-generator-server/

extract-templates-fastapi:
	docker run --user ${USER}:${GROUP} --rm \
                   -v ${PWD}:/local \
                   openapitools/openapi-generator-cli:v${GEN_VER} author template \
                   -g python-fastapi \
                   -o /local/.templates/${GEN_VER}/python_fastapi/.openapi-generator-server/

clean:
	git clean -fd
