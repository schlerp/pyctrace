from pyctraceapi.db.engine import PCTEngine
from pyctraceapi import config


engine = PCTEngine(config.NEO4J_URL, config.NEO4J_USER, config.NEO4J_PASSWORD)
