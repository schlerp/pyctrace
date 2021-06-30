import os

# -----------------------------------------------------------------------------
# neo4j connection config
# -----------------------------------------------------------------------------

#   defaults
_default_neo4j_url = "neo4j://localhost:7687"
_default_neo4j_user = "test_user"
_default_neo4j_password = "password123"

#   exported
NEO4J_URL = os.environ.get("NEO4J_URL", _default_neo4j_url)
NEO4J_USER = os.environ.get("NEO4J_USER", _default_neo4j_user)
NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD", _default_neo4j_password)

# -----------------------------------------------------------------------------
