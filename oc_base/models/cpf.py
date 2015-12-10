# -*- encoding: utf-8 -*-
###############################################################################
#                                                                             #
# Copyright (C) 2013  Renato Lima - Akretion                                  #
#                                                                             #
# This program is free software: you can redistribute it and/or modify        #
# it under the terms of the GNU Affero General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or           #
# (at your option) any later version.                                         #
#                                                                             #
# This program is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of              #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
# GNU Affero General Public License for more details.                         #
#                                                                             #
# You should have received a copy of the GNU Affero General Public License    #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
###############################################################################

import re


def validate_cpf(cpf):
    """Rotina para validação do CPF - Cadastro Nacional
    de Pessoa Física.
    :Return: True or False
    :Parameters:
      - 'cpf': CPF to be validate.
    """
    if not cpf.isdigit():
        cpf = re.sub('[^0-9]', '', cpf)

    if len(cpf) != 11:
        return False

    # Pega apenas os 9 primeiros dígitos do CPF e gera os 2 dígitos
    cpf = map(int, cpf)
    novo = cpf[:9]

    while len(novo) < 11:
        r = sum([(len(novo) + 1 - i) * v for i, v in enumerate(novo)]) % 11

        if r > 1:
            f = 11 - r
        else:
            f = 0
        novo.append(f)

    # Se o número gerado coincidir com o número original, é válido
    if novo == cpf:
        return True

    return False
