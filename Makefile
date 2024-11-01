API_NAME=OpenAPI-Example
USER=$(shell id -u)
GROUP=$(shell id -g)

GEN_VER=6.2.1

build-server: clean
	java -jar /openapi-generator-cli-${GEN_VER}.jar generate \
                   --additional-properties=apiNameSuffix=controller_impl \
                   -t .openapi-generator-server/ \
                   -i ${API_NAME}.v1.yaml \
                   -g python-flask \
                   -o server/

build-server-local: clean
	docker run --user ${USER}:${GROUP} --rm \
                   -v ${PWD}:/local openapitools/openapi-generator-cli:v${GEN_VER} generate \
				   --additional-properties=apiNameSuffix=controller_impl \
                   -t /local/.templates/${GEN_VER}/.openapi-generator-server/ \
                   -i /local/openapi.yaml \
                   -g python-flask \
                   -o /local/server/

extract-templates:
	docker run --user ${USER}:${GROUP} --rm \
                   -v ${PWD}:/local \
                   openapitools/openapi-generator-cli:v${GEN_VER} author template \
                   -g python-flask \
                   -o /local/.templates/${GEN_VER}/.openapi-generator-server/
clean:
	rm -f -r client python_server dist *.egg-info