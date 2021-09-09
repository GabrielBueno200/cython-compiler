from core import core
from Symbols.Symbol import Symbol
from Tokens.Variables.VarTypes import VariableTypesTokens
from Tokens.Scope.Scope import ScopeTokens

class SymbolTableInitalTest:

    _symbolsTable = core.SymbolsTable

    def __init__(self):
        pass

    def addSymbolsToTableTest(self):

        symbol = Symbol("number1", VariableTypesTokens.NUMBER.value, ScopeTokens.LOCAL.value)
        symbol2 = Symbol("string1", VariableTypesTokens.STRING.value, ScopeTokens.LOCAL.value)

        self._symbolsTable.StoreSymbol(symbol)
        self._symbolsTable.StoreSymbol(symbol2)

        print("Added Symbols:")
        self._symbolsTable.FindAllSymbols()


    def shouldTableFindSymbol(self, key):

        symbol = self._symbolsTable.FindSymbolByKey(key)

test = SymbolTableInitalTest()
