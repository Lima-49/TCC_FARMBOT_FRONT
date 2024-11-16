class ConfiguracaoTarefaModel:
    def __init__(self, id_cliente=None,
                 tipo_tarefa=None, produto_descr=None, fornecedor_descr=None,
                 qtd_minima=None, oferta_descr=None, fl_ativo=None,
                 fl_execucao=None, id_config_tarefa=None):
        self.id_config_tarefa = id_config_tarefa
        self.id_cliente = id_cliente
        self.tipo_tarefa = tipo_tarefa
        self.produto_descr = produto_descr
        self.fornecedor_descr = fornecedor_descr
        self.qtd_minima = qtd_minima
        self.oferta_descr = oferta_descr
        self.fl_ativo = fl_ativo
        self.fl_execucao = fl_execucao
    
    def enum_execucao(self, tipo):
        enum = {
            0: 'Imediato',
            1: 'Uma vez por dia',
            2: 'Uma vez por semana',
            3: 'Uma vez por mês'
        }
        return enum[tipo]
    
    def enum_tarefa(self, tipo):
        enum = {
            0: 'Orçamento Automatico',
            1: 'Notificação Automatica',
            2: 'Produtos para Campanhas de Marketing'    
        }
        
        return enum[tipo]
    
    def from_dict(self, data):
        return ConfiguracaoTarefaModel(
            id_config_tarefa=data.get('id_config_tarefa'),
            id_cliente = data.get('id_cliente'),
            tipo_tarefa = data.get('tipo_tarefa'),
            produto_descr = data.get('produto_descr'),
            fornecedor_descr = data.get('fornecedor_descr'),
            qtd_minima = data.get('qtd_minima'),
            oferta_descr = data.get('oferta_descr'),
            fl_ativo = data.get('fl_ativo'),
            fl_execucao = data.get('fl_execucao')
        )
    
    def to_dict(self, data):
        
        if data.tipo_tarefa == 0:
            return {
                    "ID": data.id_config_tarefa,
                    "TAREFA": self.enum_tarefa(data.tipo_tarefa),
                    "PRODUTO": data.produto_descr,
                    "FORNECEDOR": data.fornecedor_descr,
                    "QUANTIDADE MINIMA": data.qtd_minima,
                    "ATIVO": data.fl_ativo,
                    "EXECUCAO": self.enum_execucao(data.fl_execucao)
                }
        
        elif data.tipo_tarefa == 1:
            return {
                "ID": data.id_config_tarefa,
                "TAREFA": self.enum_tarefa(data.tipo_tarefa),
                "PRODUTO": data.produto_descr,
                "DESCRICAO DA OFERTA": data.oferta_descr,
                "ATIVO": data.fl_ativo,
                "EXECUCAO": self.enum_execucao(data.fl_execucao)
            }
        
        elif data.tipo_tarefa == 2:
            return {
                "ID": data.id_config_tarefa,
                "TAREFA": self.enum_tarefa(data.tipo_tarefa),
                "ATIVO": data.fl_ativo,
                "EXECUCAO": self.enum_execucao(data.fl_execucao)
            }