# PyCTrace

A python tool for contact tracing and managing active infections with in a city. This tool intends to hold relationships between people and locations. People can have their infected status updated, and queries can be ran against the graph (network) to see all people who possibly came in contact form visiting those locations during the exposure windows. This tool assumes there is data collected about individuals visits to locations, and that each individual can be uniquely identified in some way.

In addition, from reporting, once someone tests positive new relationships can be made between that person and direct contacts or infections with persons. These relationships can then be used to enrich queries and build better pictures of potentially infected populations.

## Nodes

### Person (NODE)

A person is (as the name suggests) an individual which is part of the community. Care will need to be taken when selecting the "person ID" it is suggested that unique government identifiers are to be used (assuming they are a part of your cities contact tracing recording application). Something like a concatenation of name and DOB would be a good fall back.

#### Attributes

- Unique ID
- first name
- Last name
- DOB

### Location (NODE)

A location is as the name implies a locationt that has some way of recording people who have entered the premesis and at what time. These locations are linked to the Person nodes via "VISIT" relationships.

#### Attributes

_No attributes currently_

## Edges/Relationships

### Visit (EDGE/Relationship)

A Visit is a type of relationship from a person to a location. It represents that the person attended this location during a given period of time. These are used as the primary form of contact tracing between people.

#### Attributes

- Start time
- End time

### Household (EDGE/Relationship)

A household relationship is a Person to Person relationship. This represents the fact that two given persons live together. This can be used to enrich queries.

#### Attributes

- Start time
- End time

### Infection Vector (EDGE/Relationship)

An Infection Vector relationship is a person to person relationship. This represents a confirmed infection vector from one person to another. These are identified when a given person was infected, and have passed their infection onto another person. These are identified from other types of relationship and are generally not required in actual contect tracing but serve as a very useful relationship when reporting on vectors of infection through the community.

### Attributes

- Start time
- End time
