# -----------------------------------------------------------------------------
# MIT License
#
# Copyright (c) 2022 Hieu Pham. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# -----------------------------------------------------------------------------

from copy import copy
from threading import Lock
from abc import ABC, abstractmethod


class AbstractNode(ABC):
    """
    This class is abstract interface of all inherited tree nodes.
    ---------
    @author:    Hieu Pham.
    @created:   04.09.2022.
    @updated:   05.09.2022.
    """
    @property
    @abstractmethod
    def parent(self):
        """
        Get parent node of current node.
        """
        raise NotImplemented

    @property
    @abstractmethod
    def leafs(self):
        """
        Get all leaf nodes of current node.
        """
        raise NotImplemented

    @property
    @abstractmethod
    def capacity(self):
        """
        Get leafs capacity of current node. 
        """
        raise NotImplemented
    
    @property
    @abstractmethod
    def root(self):
        """
        Get root node of current tree.
        """
        raise NotImplemented

    @property
    @abstractmethod
    def data(self):
        """
        Get data of current node.
        """
        raise NotImplemented

    @data.setter
    @abstractmethod
    def data(self, data):
        """
        Set data of current node.
        """
        raise NotImplemented
