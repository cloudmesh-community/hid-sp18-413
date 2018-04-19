import connexion
import six

from swagger_server.models.memory import MEMORY  # noqa: E501
from swagger_server.models.swap import SWAP  # noqa: E501
from swagger_server import util
import platform
import psutil
import os

def memorydetails_get():  # noqa: E501
    virtualmem=psutil.virtual_memory()
    return(virtualmem)

def swap_get():  # noqa: E501
    swapmem=psutil.swap_memory()
    return(swapmem)
