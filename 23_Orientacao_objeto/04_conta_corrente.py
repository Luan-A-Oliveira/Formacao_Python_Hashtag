from datetime import datetime
import pytz


class ContaCorrente():

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.conta = num_conta
        self.transacoes = []

    def consultar_saldo(self):
        print('Seu saldo atual é: R${:,.2f}'.format(self.saldo))

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):
        self.limite = -1000
        return self.limite

    def sacar(self, valor):
        if self.saldo - valor > self._limite_conta():
            self.saldo -= valor
            self.transacoes.append((-valor, self.saldo,
                                   ContaCorrente._data_hora()))
        else:
            print('Você não possui saldo suficiente')
            self.consultar_saldo()

    def consultar_limite_chequeespecial(self):
        print('Seu limite do cheque especial é: R${:,.2f}'.format(
            self._limite_conta()))

    def consultar_historico_trasacoes(self):
        print('Historico de Transacoes:')
        for transacoes in self.transacoes:
            print(transacoes)


# programa
conta_luan = ContaCorrente('Luan', '234.234.234-34', 1, 1234)
conta_luan.consultar_saldo()

conta_luan.depositar(2000)
# conta_luan.consultar_saldo()

conta_luan.sacar(2500)
conta_luan.consultar_saldo()

conta_luan.consultar_limite_chequeespecial()

conta_luan.consultar_historico_trasacoes()
