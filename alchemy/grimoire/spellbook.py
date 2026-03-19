#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  spellbook.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/19 13:04:34 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/19 15:17:06 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients

    validation_result = validate_ingredients(ingredients)
    if "VALID" in validate_ingredients(ingredients):
        return (f"Spell recorded: {spell_name} {ingredients}")
    else:
        return (f"Spell rejected: {spell_name} ({validation_result})")
