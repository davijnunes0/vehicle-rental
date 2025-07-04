from ..model.entities.person import Person

pessoa = Person("706.746.661-00","Davi","Nunes","davijnunesdeveloper@gmail.com")

def test_cpf():
    assert pessoa.cpf_validator() == True
    assert len(pessoa.get_cpf()) == 14