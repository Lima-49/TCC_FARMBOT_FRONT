class ClientArquivos:
    def __init__(self, id_cliente=None, tipo_arquivo=None, descricao_arquivo=None, url_bucket=None, nome_arquivo=None, id_arquivo=None):
        self.id_arquivo = id_arquivo
        self.id_cliente = id_cliente,
        self.tipo_arquivo = tipo_arquivo,
        self.descricao_arquivo = descricao_arquivo
        self.url_bucket = url_bucket
        self.nome_arquivo = nome_arquivo
        

    def enum_tipo_arquivo(self, tipo):
        obj = {
            0: 'CLIENTES',
            1: 'FORNECEDORES',
            2: 'VENDAS',
            3: 'ESTOQUE'
        }
        
        return obj[tipo]
    
    def from_dict(self, data):
        return ClientArquivos(
            id_arquivo = data.get('id_arquivo'),
            id_cliente = data.get('id_cliente'),
            tipo_arquivo = data.get('tipo_arquivo'),
            descricao_arquivo = data.get('descricao_arquivo'),
            url_bucket = data.get('url_bucket'),
            nome_arquivo = data.get('nome_arquivo')
        )
        