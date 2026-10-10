from pathlib import Path

from langchain_community.document_loaders import DirectoryLoader, TextLoader

def load_documents(knowledge_dir: str):
    """
    Load Markdown documents from the knowledge directory.
    """

    path = Path(knowledge_dir)

    if not path.exists():
        raise FileNotFoundError(
            f"Knowledge directory does not exist: {knowledge_dir}"
        )

    loader = DirectoryLoader(
        str(path),
        glob="**/*.md",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"}
    )

    documents = loader.load()
    return documents

