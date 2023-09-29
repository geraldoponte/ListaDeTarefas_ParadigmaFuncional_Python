import unittest
from datetime import date
from tarefa import criar_tarefa, eh_tarefa_concluida, eh_tarefa_pendente, concluir_tarefa, tarefa_to_string

class TestTarefa(unittest.TestCase):

    def test_criar_tarefa(self):                    
        tarefa1 = criar_tarefa("Estudar", "Estudar livro do Clean Code", date(2023, 9, 10))        
        self.assertIsNotNone(tarefa1) # verifica se a tarefa criada é um objeto válido (não nulo) 
        
        tarefa2 = criar_tarefa("Estudar", "Estudar livro de Design Patterns", date(2023, 9, 20))
        self.assertIsNotNone(tarefa2) # verifica se a tarefa criada é um objeto válido (não nulo)
        
        tarefa3 = criar_tarefa("Pagar", "Pagar mensalidade da graduação", date(2023, 9, 30))
        self.assertIsNotNone(tarefa3) # verifica se a tarefa criada é um objeto válido (não nulo)
                
        # Teste para criar uma tarefa sem título
        with self.assertRaises(ValueError):
            criar_tarefa("Estudar", "", date(2023, 10, 1))
            
        # Teste para verificar se a tarefa é criada como 'não concluída'
        self.assertTrue(eh_tarefa_pendente(tarefa1))
        self.assertTrue(eh_tarefa_pendente(tarefa2))
        self.assertTrue(eh_tarefa_pendente(tarefa3))


    def test_eh_tarefa_concluida(self):
        tarefa = criar_tarefa("Estudar", "Estudar livro do Clean Code", date(2023, 9, 10))
        self.assertFalse(eh_tarefa_concluida(tarefa))
    
        tarefa = concluir_tarefa(tarefa)        
        self.assertTrue(eh_tarefa_concluida(tarefa))


    def test_eh_tarefa_pendente(self):        
        tarefa = criar_tarefa("Estudar", "Estudar livro do Clean Code", date(2023, 9, 10))        
        self.assertTrue(eh_tarefa_pendente(tarefa))
        
        self.assertFalse(eh_tarefa_pendente(concluir_tarefa(tarefa)))
        

    def test_concluir_tarefa_pendente(self):                
        self.assertTrue(concluir_tarefa( criar_tarefa("Estudar", "Estudar livro do Clean Code", date(2023, 9, 10)) ))

        
    def test_concluir_tarefa_ja_concluida(self):                
        tarefa = criar_tarefa("Estudar", "Estudar livro do Clean Code", date(2023, 9, 10))
        tarefa = concluir_tarefa(tarefa)
        self.assertEqual(tarefa, concluir_tarefa(tarefa))


    def test_tarefa_to_string(self):
        tarefa = criar_tarefa("Estudar", "Estudar livro do Clean Code", date(2023, 9, 10))       
        self.assertEqual(tarefa_to_string(tarefa), "Estudar livro do Clean Code - Vencimento: 2023-09-10 - Concluída: não")        
        

if __name__ == '__main__':
    unittest.main()