from document_types import DocumentTypes

class Document:
  """
  Entidade para reprentar um documento
  """
  def __init__(self, doc_type: DocumentTypes, number: str):
    self.doc_type = doc_type
    self.number = number