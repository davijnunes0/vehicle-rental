from src.model.entities.person import Person
from src.test.personTest import test_cpf

def main():
   
   pessoa = Person("706.746.661-00","Davi","Nunes","davijnunesdeveloper@gmail.com")

   print(pessoa.cpf_validator())

   print(test_cpf())

if __name__ == "__main__":
    main()