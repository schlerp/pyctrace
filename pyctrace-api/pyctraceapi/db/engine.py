from datetime import datetime

from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable
from neo4j.work.transaction import Transaction

from pyctraceapi.log import logger


class PCTEngine(object):
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_visit(self, person_id: str, location_id: str, visit_dt: datetime):
        with self.driver.session() as session:
            result = session.write_transaction(
                self._create_and_return_visit, person_id, location_id, visit_dt
            )
            for row in result:
                logger.info(
                    f"Created visit: {row['p1']} visited {row['l1']} at {row['dt']}"
                )

    @staticmethod
    def _create_and_return_visit(
        tx: Transaction, person_id: str, location_id: str, visit_dt: datetime
    ):
        query = (
            "CREATE (p1:Person { id: $person_id, infected: false }) "
            "CREATE (l1:Location { id: $location_id }) "
            "CREATE (p1)-[v:VISITED { dt: $visit_dt }]->(l1) "
            "RETURN p1, l1, dt1"
        )
        result = tx.run(
            query, person_id=person_id, location_id=location_id, visit_dt=visit_dt
        )
        try:
            return [
                {"p1": row["p1"]["id"], "p2": row["p2"]["id"], "dt": row["v"]["dt"]}
                for row in result
            ]
        except ServiceUnavailable as exception:
            logger.error(f"{query} raised an error: \n {exception}")
            raise

    def find_person(self, person_id: str):
        with self.driver.session() as session:
            result = session.read_transaction(self._find_and_return_person, person_id)
            for row in result:
                print("Found person: {row}".format(row=row))

    @staticmethod
    def _find_and_return_person(tx, person_name):
        query = (
            "MATCH (p:Person) " "WHERE p.name = $person_name " "RETURN p.name AS name"
        )
        result = tx.run(query, person_name=person_name)
        return [row["name"] for row in result]
