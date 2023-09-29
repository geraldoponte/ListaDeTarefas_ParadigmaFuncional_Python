import unittest
from datetime import date
from tarefa import criar_tarefa, concluir_tarefa
from tarefas import excluir_categoria, categoria_existe, obter_categoria_existente, incluir_categoria,\
 obter_categorias, adicionar_tarefa, criar_lista_de_tarefas, contar_total_de_tarefas,\
 contar_tarefas_da_categoria, excluir_tarefa, filtrar_tarefas_pendentes, filtrar_tarefas_concluidas,\
 imprimir_tarefas


class TestTarefas(unittest.TestCase):

    def gerar_amostra(self):
        amostra = criar_lista_de_tarefas()     
        
        tarefa1 = criar_tarefa("Pagar", "Pagar mensalidade da graduação", date(2023, 9, 30))
        self.assertIsNotNone(tarefa1) # verifica se a tarefa criada é um objeto válido (não nulo)
        adicionar_tarefa(amostra, tarefa1)
        
        tarefa2 = criar_tarefa("Estudar", "Estudar livro de Design Patterns", date(2023, 9, 20))        
        self.assertIsNotNone(tarefa2) # verifica se a tarefa criada é um objeto válido (não nulo)
        adicionar_tarefa(amostra, tarefa2)
         
        tarefa3 = criar_tarefa("Estudar", "Estudar livro de Clean Code", date(2023, 9, 10))        
        self.assertIsNotNone(tarefa3) # verifica se a tarefa criada é um objeto válido (não nulo)
        adicionar_tarefa(amostra, tarefa3)                               
        
        amostra = incluir_categoria(amostra, "Reparar")            
                        
        return amostra        
    

    def test_categoria_existe(self):
        mapa = self.gerar_amostra()        
        self.assertTrue(categoria_existe(mapa, "estudar"))
        self.assertTrue(categoria_existe(mapa, "PAGAR"))
        self.assertTrue(categoria_existe(mapa, "REpaRAr"))
        self.assertFalse(categoria_existe(mapa, "XYZ"))
        
    
    def test_obter_categoria_existente(self):
        mapa = self.gerar_amostra()
        self.assertEqual(obter_categoria_existente(mapa, "rEpArAr"), "Reparar")
        self.assertTrue(obter_categoria_existente(mapa, "estudar"), "Estudar")
        self.assertTrue(obter_categoria_existente(mapa, "PAGAR"), "Pagar")
        self.assertTrue(obter_categoria_existente(mapa, "XYZ"), "XYZ") # deve retornar a categoria_procurada se ela não existe no dicionário
        

    def test_obter_categorias(self):    
        amostra = self.gerar_amostra()                    
        self.assertEqual(obter_categorias(amostra), ["Estudar", "Pagar", "Reparar"])        


    def test_incluir_categoria_valida(self):        
        mapa = criar_lista_de_tarefas()
        mapa = incluir_categoria(mapa, "Estudar")
        self.assertEqual(obter_categorias(mapa), ["Estudar"])        
        
        
    def test_incluir_categoria_invalida(self):
        mapa = criar_lista_de_tarefas()      
        mapa = incluir_categoria(mapa, 123)        
        self.assertEqual(obter_categorias(mapa), [])
        mapa = incluir_categoria(mapa, True)
        self.assertEqual(obter_categorias(mapa), [])
        
    
    def test_incluir_categoria_vazia(self):        
        mapa = criar_lista_de_tarefas() 
        mapa = incluir_categoria(mapa, "")       
        self.assertEqual(obter_categorias(mapa), [])
                    
        mapa = incluir_categoria(mapa, " ")
        self.assertEqual(obter_categorias(mapa), [])            
            
    
    def test_incluir_categoria_ja_existente(self):
        mapa = criar_lista_de_tarefas()
        mapa = incluir_categoria(mapa, "Estudar")
        mapa = incluir_categoria(mapa, "Pagar")
        mapa = incluir_categoria(mapa, "eStUdAr")
        mapa = incluir_categoria(mapa, "Reparar")
        self.assertEqual(obter_categorias(mapa), ["Estudar", "Pagar", "Reparar"])
    
    
    def test_ao_excluir_categoria_com_tarefas_fazer_nada(self):
        mapa = self.gerar_amostra()              
        mapa = excluir_categoria(mapa, "Estudar")
        self.assertEqual(obter_categorias(mapa), ['Estudar', 'Pagar', 'Reparar'])
    
    
    def test_ao_excluir_categoria_sem_tarefas_excluir_categoria(self):
        mapa = self.gerar_amostra()              
        mapa = excluir_categoria(mapa, "Reparar")
        self.assertEqual(obter_categorias(mapa), ['Estudar', 'Pagar'])
        
    
    def test_ao_excluir_categoria_inexistente_fazer_nada(self):
        mapa = self.gerar_amostra()       
        mapa = excluir_categoria(mapa, "XYZ")
        self.assertEqual(obter_categorias(mapa), ['Estudar', 'Pagar', 'Reparar'])    

    
    def test_excluir_categoria_invalida(self):
        mapa = self.gerar_amostra()
        with self.assertRaises(TypeError) as context:
            excluir_categoria(mapa, 123)
        self.assertEqual(str(context.exception), 'Uma categoria deve ser um texto.')



    def test_contar_total_de_tarefas(self):
        mapa_de_tarefas = self.gerar_amostra()
        self.assertTrue(contar_total_de_tarefas(mapa_de_tarefas), 3)        
        # print(imprimir_tarefas(mapa_de_tarefas))        
        
        
    def test_contar_tarefas_da_categoria(self):
        mapa_de_tarefas = self.gerar_amostra()
        self.assertTrue(contar_tarefas_da_categoria(mapa_de_tarefas, "Estudar"), 2)
        self.assertTrue(contar_tarefas_da_categoria(mapa_de_tarefas, "Pagar"), 1)
        self.assertEqual(contar_tarefas_da_categoria(mapa_de_tarefas, "XYZ"), 0)
      
    
    def test_excluir_tarefa(self):
        mapa_de_tarefas = self.gerar_amostra()
        self.assertEqual(contar_total_de_tarefas(mapa_de_tarefas), 3)
        # print("Teste de Exclusão de Tarefa")        
        # print(imprimir_tarefas(mapa_de_tarefas))        
                    
        # print("\n...excluindo a segunda tarefa (índice 1) da categoria 'Estudar'...")
        tarefa_para_excluir = mapa_de_tarefas["Estudar"][1] #excluir: "Estudar livro de Design Patterns"
        excluir_tarefa(mapa_de_tarefas, tarefa_para_excluir)        
        # print(imprimir_tarefas(mapa_de_tarefas))
        self.assertEqual(contar_total_de_tarefas(mapa_de_tarefas), 2)

        # print("\n...excluindo a primeira e única tarefa (índice 0) da categoria 'Pagar'...")
        tarefa_para_excluir = mapa_de_tarefas["Pagar"][0] #excluir: "Pagar mensalidade da graduação"
        excluir_tarefa(mapa_de_tarefas, tarefa_para_excluir)
        # print(imprimir_tarefas(mapa_de_tarefas))
        self.assertEqual(contar_total_de_tarefas(mapa_de_tarefas), 1)
   
    
    def test_filtrar_tarefas_pendentes(self):    
        amostra = criar_lista_de_tarefas()     
         
        tarefa1 = criar_tarefa("Estudar", "Estudar livro do Clean Code", date(2023, 9, 10))        
        adicionar_tarefa(amostra, tarefa1)
        
        tarefa2 = concluir_tarefa(criar_tarefa("Estudar", "Estudar livro de Design Patterns", date(2023, 9, 20)))        
        adicionar_tarefa(amostra, tarefa2)        
        
        tarefa3 = criar_tarefa("Pagar", "Pagar mensalidade da graduação", date(2023, 9, 30))
        adicionar_tarefa(amostra, tarefa3)
        
        # print("todas as tarefas")
        # print(imprimir_tarefas(amostra))
        # print("\n apenas as tarefas pendentes ")
        # print(imprimir_tarefas(filtrar_tarefas_pendentes(amostra)))
        
        self.assertEqual(contar_total_de_tarefas(amostra), 3)
        self.assertEqual(contar_total_de_tarefas(filtrar_tarefas_pendentes(amostra)), 2)
                
        
    def test_filtrar_tarefas_concluidas(self):    
        amostra = criar_lista_de_tarefas()     
         
        tarefa1 = criar_tarefa("Estudar", "Estudar livro do Clean Code", date(2023, 9, 10))        
        adicionar_tarefa(amostra, tarefa1)
        
        tarefa2 = concluir_tarefa(criar_tarefa("Estudar", "Estudar livro de Design Patterns", date(2023, 9, 20)))        
        adicionar_tarefa(amostra, tarefa2)        
        
        tarefa3 = criar_tarefa("Pagar", "Pagar mensalidade da graduação", date(2023, 9, 30))
        adicionar_tarefa(amostra, tarefa3)
        
        # print("todas as tarefas")
        # print(imprimir_tarefas(amostra))
        # print("\n apenas as tarefas pendentes ")
        # print(imprimir_tarefas(filtrar_tarefas_pendentes(amostra)))
        
        self.assertEqual(contar_total_de_tarefas(amostra), 3)
        self.assertEqual(contar_total_de_tarefas(filtrar_tarefas_concluidas(amostra)), 1)      


    def test_imprimir_amostra(self):
        amostra = self.gerar_amostra()
        print("\nAmostra\n=======\n"+imprimir_tarefas(amostra))

        

if __name__ == '__main__':
    unittest.main()