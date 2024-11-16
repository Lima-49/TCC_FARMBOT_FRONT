class ConfigOrcamento:
    def __init__(self, id_config_tarefa=None,id_cliente=None,
                 produto_descr = None, tipo_tarefa=None, fornecedor_descr=None,
                 qtd_minina=None, fl_ativo=None,
                 fl_execucao=None):
        
        self.id_config_tarefa = id_config_tarefa
        self.id_cliente = id_cliente
        self.tipo_tarefa = tipo_tarefa
        self.produto_descr = produto_descr
        self.fornecedor_descr = fornecedor_descr
        self.qtd_minina = qtd_minina
        self.fl_ativo = fl_ativo
        self.fl_execucao = fl_execucao
    
    def from_dict(self, data):
        return ConfigOrcamento(
            id_config_tarefa=data.get('id_config_tarefa'),
            id_cliente = data.get('id_cliente'),
            tipo_tarefa = data.get('tipo_tarefa'),
            produto_descr = data.get('produto_descr'),
            fornecedor_descr = data.get('fornecedor_descr'),
            qtd_minina = data.get('qtd_minina'),
            fl_ativo = data.get('fl_ativo'),
            fl_execucao = data.get('fl_execucao')
        )
    
class ConfigNotificacoOferta:
    def __init__(self, id_config_tarefa=None, id_cliente=None, tipo_tarefa=None, produto_descr=None, oferta_desc=None, fl_ativo=None, fl_execucao=None):
        self.id_config_tarefa = id_config_tarefa
        self.id_cliente = id_cliente
        self.tipo_tarefa = tipo_tarefa
        self.produto_descr = produto_descr
        self.oferta_desc = oferta_desc
        self.fl_ativo = fl_ativo
        self.fl_execucao = fl_execucao
        
    def from_dict(self, data):
        return ConfigNotificacoOferta(
            id_config_tarefa = data.get('id_config_tarefa'),
            id_cliente = data.get('id_cliente'),
            tipo_tarefa = data.get('tipo_tarefa'),
            produto_descr = data.get('produto_descr'),
            oferta_desc = data.get('oferta_desc'),
            fl_ativo = data.get('fl_ativo'),
            fl_execucao = data.get('fl_execucao')
        )
        
class ConfiguracaoProdutosCamapanhas:
    def __init__(self, id_config_tarefa=None, id_cliente=None, tipo_tarefa=None, fl_ativo=None, fl_execucao=None):
        self.id_config_tarefa = id_config_tarefa
        self.id_cliente = id_cliente
        self.tipo_tarefa = tipo_tarefa
        self.fl_ativo = fl_ativo
        self.fl_execucao = fl_execucao
        
    def from_dict(self, data):
        return ConfiguracaoProdutosCamapanhas(
            id_config_tarefa = data.get("id_config_tarefa"),
            id_cliente = data.get("id_cliente"),
            tipo_tarefa = data.get('tipo_tarefa'),
            fl_ativo = data.get("fl_ativo"),
            fl_execucao = data.get("fl_execucao")
        )
        

class ConfiguracaoTarefaModel:
    def __init__(self, id_cliente=None,
                 tipo_tarefa=None, produto_descr=None, fornecedor_descr=None,
                 qtd_minima=None, oferta_descr=None, fl_ativo=None,
                 fl_execucao=None, id_config_tarefa=None):
        self.id_config_tarefa = id_config_tarefa
        self.id_cliente = id_cliente
        self.tipo_tarefa = tipo_tarefa
        self.produto_descr = produto_descr  # Aqui estava correto
        self.fornecedor_descr = fornecedor_descr
        self.qtd_minima = qtd_minima
        self.oferta_descr = oferta_descr
        self.fl_ativo = fl_ativo
        self.fl_execucao = fl_execucao
    
    def aloc_object(self,data):
        
        if data.get('tipo_tarefa') == 0:
            return ConfigOrcamento().from_dict(data)
        elif data.get('tipo_tarefa') == 1:
            return ConfigNotificacoOferta().from_dict(data)
        elif data.get('tipo_tarefa') == 2:
            return ConfiguracaoProdutosCamapanhas().from_dict(data)
                
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
    