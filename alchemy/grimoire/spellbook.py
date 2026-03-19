#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  spellbook.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/19 13:04:34 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/19 14:59:10 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .validator import validate_ingredients


def record_spell(spell_name: str, ingredients: str) -> str:
    if "VALID" in validate_ingredients(ingredients):
        return (f"Spell recorded: {spell_name} {ingredients}")
    else:
        return (f"Spell rejected: {spell_name} {ingredients}")
