import os
from llama_parse import LlamaParse
from llama_index.core.node_parser import MarkdownElementNodeParser
from llama_index.core import VectorStoreIndex



os.environ["LLAMA_CLOUD_API_KEY"] = "llx-RXDLGPhFOaDqYJuCqujCkaKu3V4wZkQloxGc9XzMwT3k6FoE"
os.environ["OPENAI_API_KEY"] = ""


def parse(file, question):
    parser = LlamaParse(
        result_type="markdown",
        verbose=True,
    )
    documents = parser.load_data(file)
    node_parser = MarkdownElementNodeParser()
    nodes = node_parser.get_nodes_from_documents(documents=[documents[0]])
    base_nodes, objects = node_parser.get_nodes_and_objects(nodes)
    index = VectorStoreIndex(nodes=base_nodes+objects)

    engine = index.as_query_engine(verbose = True)
    return engine.query(question)
