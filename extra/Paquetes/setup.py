from setuptools import setup

setup(
	name="paquete",
	version="0.1",
	description="Este es un paquete de ejemplo",
	author="Luis Fernando Chavez",
	author_email="yo@email.com",
	url="http://hcosta.info",
	scripts=[],
	packages=["paquete", "paquete.adios", "paquete.hola"]
)