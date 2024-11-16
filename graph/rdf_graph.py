from rdflib import Graph, Literal, RDF, Namespace, URIRef
from rdflib.namespace import FOAF, XSD

def create_graph():
    # Ініціалізація графу
    g = Graph()

    # Визначення власного простору імен
    EX = Namespace("http://example.org/")

    # Додавання простору імен до графу
    g.bind("ex", EX)
    g.bind("foaf", FOAF)

    # URI для Кейда та Емми
    cade = URIRef(EX.Cade)
    emma = URIRef(EX.Emma)

    # Інформація про Кейда
    g.add((cade, RDF.type, FOAF.Person))
    g.add((cade, FOAF.name, Literal("Cade", datatype=XSD.string)))
    g.add((cade, EX.homeAddress, Literal("1516 Henry Street, Berkeley, California 94709, USA", datatype=XSD.string)))
    g.add((cade, EX.degree, Literal("Bachelor of Biology, University of California, 2011", datatype=XSD.string)))
    g.add((cade, FOAF.interest, Literal("Birds", datatype=XSD.string)))
    g.add((cade, FOAF.interest, Literal("Ecology", datatype=XSD.string)))
    g.add((cade, FOAF.interest, Literal("Environment", datatype=XSD.string)))
    g.add((cade, FOAF.interest, Literal("Photography", datatype=XSD.string)))
    g.add((cade, FOAF.interest, Literal("Travel", datatype=XSD.string)))
    g.add((cade, EX.visited, Literal("Canada", datatype=XSD.string)))
    g.add((cade, EX.visited, Literal("France", datatype=XSD.string)))

    # Інформація про Емму
    g.add((emma, RDF.type, FOAF.Person))
    g.add((emma, FOAF.name, Literal("Emma", datatype=XSD.string)))
    g.add((emma, EX.homeAddress, Literal("Carrer de la Guardia Civil 20, 46020 Valencia, Spain", datatype=XSD.string)))
    g.add((emma, EX.degree, Literal("Master of Chemistry, University of Valencia, 2015", datatype=XSD.string)))
    g.add((emma, FOAF.topic_interest, Literal("Waste Management", datatype=XSD.string)))
    g.add((emma, FOAF.topic_interest, Literal("Toxic Waste", datatype=XSD.string)))
    g.add((emma, FOAF.topic_interest, Literal("Air Pollution", datatype=XSD.string)))
    g.add((emma, FOAF.interest, Literal("Cycling", datatype=XSD.string)))
    g.add((emma, FOAF.interest, Literal("Music", datatype=XSD.string)))
    g.add((emma, FOAF.interest, Literal("Travel", datatype=XSD.string)))
    g.add((emma, EX.visited, Literal("Portugal", datatype=XSD.string)))
    g.add((emma, EX.visited, Literal("Italy", datatype=XSD.string)))
    g.add((emma, EX.visited, Literal("France", datatype=XSD.string)))
    g.add((emma, EX.visited, Literal("Germany", datatype=XSD.string)))
    g.add((emma, EX.visited, Literal("Denmark", datatype=XSD.string)))
    g.add((emma, EX.visited, Literal("Sweden", datatype=XSD.string)))

    # Взаємозв’язок між Кейдом та Еммою
    g.add((cade, FOAF.knows, emma))
    g.add((emma, FOAF.knows, cade))
    g.add((cade, EX.met, Literal("Paris, August 2014", datatype=XSD.string)))

    return g, cade, emma, EX

def save_graph(g, file_path):
    # Сериалізація графу у файл
    g.serialize(destination=file_path, format="turtle")
    print(f"Граф збережено у файл: {file_path}")

def edit_graph(g, cade, emma, EX):
    # Редагування графу
    g.add((cade, EX.visited, Literal("Germany", datatype=XSD.string)))  # Додати Німеччину Кейду
    g.set((emma, FOAF.age, Literal(36, datatype=XSD.integer)))  # Додати вік Емми

def print_all_triples(g):
    print("Усі трійки графу:")
    for s, p, o in g:
        print(s, p, o)

def print_triples_about_emma(g, emma):
    print("\nТрійки про Емму:")
    for s, p, o in g.triples((emma, None, None)):
        print(s, p, o)

def print_triples_with_names(g):
    print("\nТрійки з іменами людей:")
    for s, p, o in g.triples((None, FOAF.name, None)):
        print(s, p, o)

def main():
    # Створення графу
    g, cade, emma, EX = create_graph()

    # Збереження графу
    save_graph(g, "graph.ttl")

    # Редагування графу
    edit_graph(g, cade, emma, EX)

    # Виведення всіх трійок
    print_all_triples(g)

    # Виведення трійок, що стосуються Емми
    print_triples_about_emma(g, emma)

    # Виведення трійок з іменами людей
    print_triples_with_names(g)

if __name__ == "__main__":
    main()
