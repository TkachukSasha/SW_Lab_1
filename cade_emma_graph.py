from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import FOAF, RDF, XSD

# Створення графу
g = Graph()

# Простір імен (Namespace)
EX = Namespace("http://example.org/")
g.bind("ex", EX)

# Кейд
cade = URIRef("http://example.org/cade")
g.add((cade, RDF.type, FOAF.Person))
g.add((cade, FOAF.name, Literal("Cade")))
g.add((cade, EX.address, Literal("1516 Henry Street, Berkeley, California 94709, USA")))
g.add((cade, EX.degree, Literal("Bachelor of Biology", datatype=XSD.string)))
g.add((cade, EX.degreeYear, Literal(2011, datatype=XSD.gYear)))
g.add((cade, EX.interests, Literal("birds, ecology, environment, photography, travel", datatype=XSD.string)))
g.add((cade, EX.visited, Literal("Canada", datatype=XSD.string)))
g.add((cade, EX.visited, Literal("France", datatype=XSD.string)))

# Емма
emma = URIRef("http://example.org/emma")
g.add((emma, RDF.type, FOAF.Person))
g.add((emma, FOAF.name, Literal("Emma")))
g.add((emma, EX.address, Literal("Carrer de la Guardia Civil 20, 46020 Valencia, Spain")))
g.add((emma, EX.degree, Literal("Master of Chemistry", datatype=XSD.string)))
g.add((emma, EX.degreeYear, Literal(2015, datatype=XSD.gYear)))
g.add((emma, EX.knowledge, Literal("waste management, toxic waste, air pollution", datatype=XSD.string)))
g.add((emma, EX.interests, Literal("cycling, music, travel", datatype=XSD.string)))
g.add((emma, EX.visited, Literal("Portugal", datatype=XSD.string)))
g.add((emma, EX.visited, Literal("Italy", datatype=XSD.string)))
g.add((emma, EX.visited, Literal("France", datatype=XSD.string)))
g.add((emma, EX.visited, Literal("Germany", datatype=XSD.string)))
g.add((emma, EX.visited, Literal("Denmark", datatype=XSD.string)))
g.add((emma, EX.visited, Literal("Sweden", datatype=XSD.string)))

# Зв'язок між Кейдом та Еммою
g.add((cade, FOAF.knows, emma))
g.add((emma, FOAF.knows, cade))
g.add((cade, EX.metIn, Literal("Paris", datatype=XSD.string)))
g.add((cade, EX.metInDate, Literal("2014-08", datatype=XSD.gYearMonth)))

# Серіалізація графу у формат Turtle та запис у файл
with open("cade_emma_graph.ttl", "w") as f:
    f.write(g.serialize(format='turtle').decode('utf-8'))

# Виведення трійок графу на консоль (всі трійки)
print("Усі трійки графу:")
for subj, pred, obj in g:
    print(subj, pred, obj)

# Виведення трійок, що стосуються лише Емми
print("\nТрійки, що стосуються Емми:")
for subj, pred, obj in g.triples((emma, None, None)):
    print(subj, pred, obj)

# Виведення трійок, що містять імена людей
print("\nТрійки, що містять імена людей:")
for subj, pred, obj in g.triples((None, FOAF.name, None)):
    print(subj, pred, obj)
