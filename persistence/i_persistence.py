from abc import ABC, abstractmethod

"""
Persistence Interface an abstract class or interface
which outlines methods for saving, retrieving, updating,
deleting entities.
Includes method siganturesto handle various data types
"""


class IPersistenceManager(ABC):
    """
    Interface for defining abstract methods
    """
    @abstractmethod
    def save(self, entity):
        """
        Save entity to the storage
        """
        pass

    @abstractmethod
    def get(self, entity_id, entity_type):
        """
        Retrieve the entity from the storage
        """
        pass

    @abstractmethod
    def update(self, entity):
        """
        Update the entity in the storage
        """
        pass

    @abstractmethod
    def delete(self, entity_id, entity_type):
        """
        Delete the entity from the storage
        """
        pass
