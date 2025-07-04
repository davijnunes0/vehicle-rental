from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self,cpf: str,first_name: str, last_name : str, email: str):
        self.__cpf = cpf
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_email(email)
    

    def get_cpf(self) -> str:
        return self.__cpf

    def set_first_name(self,first_name: str) -> None:
        if first_name:
            self.__first_name = first_name
        else:
            raise ValueError("First name is invalid")

    def get_first_name(self) -> str:
        return self.__first_name
    
    def set_last_name(self,last_name : str) -> None:
        if last_name:
            self.__last_name = last_name
        else:
            raise ValueError("Last name is invalid")

    def get_last_name(self) -> str:
        return self.__last_name
    
    def set_email(self,email):
        if email:
            self.__email = email
        else:
            raise ValueError("Emal is invalid")
    
    def get_email(self):
        return self.__email

    # 706.746.661-00
    def cpf_validator(self) -> bool:

        cpf : list[int] = list()

        if len(self.get_cpf()) > 16: 
            return False

        for digit in self.get_cpf():
            if digit != "." and digit != "-": cpf.append(int(digit))


        cpf_copy = cpf[:9]
       
        index : int  = 0
        weigth : int = 10
        sum_d : int = 0
        rest : int = 0
        first_digit : int = 0

        while index < len(cpf_copy):
            sum_d += cpf_copy[index] * weigth
            weigth -= 1
            index += 1
        

        rest = sum_d % 11

        if rest < 2:
            first_digit = 0
        else:
            first_digit = 11 - rest

        print(f"First digit = {first_digit}")
        
        cpf_copy.append(first_digit)

        index = 0
        weigth  = 11
        sum_d  = 0
        rest = 0
        first_digit = 0
        second_digit : int = 0

        while index < len(cpf_copy):
            sum_d += cpf_copy[index] * weigth
            index += 1
            weigth -= 1
        
        rest = sum_d % 11
        second_digit = 0 if rest < 2 else 11 - rest
        print(f"Second digit = {second_digit}")

        cpf_copy.append(second_digit)
        

        if cpf_copy[9] == cpf[9] and cpf_copy[10] == cpf[10]: return True

        return False


