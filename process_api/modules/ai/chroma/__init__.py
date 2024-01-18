# !pip install chromadb
import chromadb
from chromadb.config import Settings
from process_api.utils.get_value import get_value


class ChromaModel:

    @staticmethod
    def register(api):
        api.add_module("chroma", ChromaModel)
        api.set_variable("chroma_collections", {})


    @staticmethod
    async def init_client(api, step, ctx=None, process=None, item=None):
        args = step["args"]

        client_type = await get_value(args.get("type", "memory"), ctx, process, item)

        if client_type == "file":
            path = await get_value(args.get("path", "default"), ctx, process, item)
            chroma_client = chromadb.PersistentClient(path=path)
        elif client_type == "http":
            host = await get_value(args.get("host", "localhost"), ctx, process, item)
            port = await get_value(args.get("port", 8000), ctx, process, item)
            chroma_client = chromadb.HttpClient(host=host, port=port)
        else:
            chroma_client = chromadb.Client(Settings(anonymized_telemetry=False))

        api.set_variable("chroma_client", chroma_client)
        return True


    @staticmethod
    async def init_collection(api, step, ctx=None, process=None, item=None):
        args = step["args"]

        chroma_client = api.get_variable("chroma_client")
        collections = api.get_variable("chroma_collections")

        name = await get_value(step["args"].get("name", "default"), ctx, process, item)
        action = await get_value(args.get("action", "default"), ctx, process, item)

        if action == "get":
            collection = chroma_client.get_collection(name)
        elif action == "create":
            collection = chroma_client.create_collection(name)
        else:
            collection = chroma_client.get_or_create_collection(name)

        collections[name] = collection

    @staticmethod
    async def add_to_collection(api, step, ctx=None, process=None, item=None):
        collections = api.get_variable("chroma_collections")
        args = step["args"]

        name = await get_value(args.get("name", "default"), ctx, process, item)
        documents = await get_value(args.get("documents", None), ctx, process, item)
        metadatas = await get_value(args.get("metadatas", None), ctx, process, item)
        embeddings = await get_value(args.get("embeddings", None), ctx, process, item)
        ids = await get_value(step["args"].get("ids", None), ctx, process, item)

        collection = collections[name]
        collection.add(documents=documents, metadatas=metadatas, embeddings=embeddings, ids=ids)

        print(collection.peek())

    @staticmethod
    async def delete_collection(api, step, ctx=None, process=None, item=None):
        args = step["args"]
        name = await get_value(args.get("name", "default"), ctx, process, item)
        chroma_client = api.get_variable("chroma_client")
        chroma_client.delete_collection(name)

