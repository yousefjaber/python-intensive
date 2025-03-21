# 1️⃣ Single Responsibility Principle (SRP)
class BankAccount:
    """Handles bank account-related operations."""
    
    def __init__(self, account_no: str):
        self.account_no = account_no

    def get_account_number(self) -> str:
        return self.account_no


class BankAccountDB:
    """Handles saving accounts to a database (or list)."""
    
    accounts_list = []

    @classmethod
    def save(cls, account: BankAccount) -> None:
        cls.accounts_list.append(account)
        print("Success, saved to DB")

# 2️⃣ Open/Closed Principle (OCP)
class Discount:
    """Base class for discounts"""
    
    def __init__(self, price: float):
        self.price = price

    def get_discount(self) -> float:
        return self.price


class SilverDiscount(Discount):
    def get_discount(self) -> float:
        return self.price * 0.8


class GoldDiscount(Discount):
    def get_discount(self) -> float:
        return self.price * 0.7


class VIPDiscount(Discount):
    def get_discount(self) -> float:
        return self.price * 0.6

# 3️⃣ Liskov Substitution Principle (LSP)
class Vehicle:
    def start_engine(self) -> None:
        raise NotImplementedError("Subclasses must implement this method")


class EngineVehicle(Vehicle):
    def start_engine(self) -> None:
        print("Starting engine...")


class Car(EngineVehicle):
    def start_engine(self) -> None:
        print("Let's go!")


class Bicycle(Vehicle):
    """Bicycles don’t have engines, so they should not inherit from EngineVehicle."""
    
    def start_engine(self) -> None:
        raise NotImplementedError("Bicycles don't have an engine")

# 4️⃣ Interface Segregation Principle (ISP)
from abc import ABC, abstractmethod

class BuilderInterface(ABC):
    @abstractmethod
    def build_construction(self) -> None:
        pass


class WaiterInterface(ABC):
    @abstractmethod
    def serve_the_table(self) -> None:
        pass


class TeacherInterface(ABC):
    @abstractmethod
    def check_hometask(self) -> None:
        pass


class Builder(BuilderInterface):
    def build_construction(self) -> None:
        print("Building a house!")


class Waiter(WaiterInterface):
    def serve_the_table(self) -> None:
        print("Serving food at the table.")


class Teacher(TeacherInterface):
    def check_hometask(self) -> None:
        print("Checking students' homework.")

# 5️⃣ Dependency Inversion Principle (DIP)
from abc import ABC, abstractmethod

class Publisher(ABC):
    """Abstract base class for all publishers."""
    
    @abstractmethod
    def publish(self, news: str) -> None:
        pass


class NewsPaper(Publisher):
    def publish(self, news: str) -> None:
        print(f"{news} published today")


class Reporter:
    def __init__(self, publisher: Publisher):
        self.publisher = publisher

    def publish(self, news: str) -> None:
        self.publisher.publish(news)
        


